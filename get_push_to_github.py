import os
import io
import json
import time
import base64
import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from pathlib import Path
from tqdm import tqdm

class QuranAudioDownloaderToGitHub:
    """Download Quran audio files and push directly to GitHub without local storage."""

    API_BASE_URL = "https://api.quran.com/api/v4"
    AUDIO_BASE_URL = "https://verses.quran.foundation"
    DOWNLOAD_URL = "https://download.quranicaudio.com"
    GITHUB_API_URL = "https://api.github.com"

    def __init__(self, github_token, repo_owner, repo_name, branch="main", max_workers=5, delay=0.5):
        """
        Initialize the downloader with configuration parameters.

        Args:
            github_token (str): Personal access token for GitHub API
            repo_owner (str): GitHub username/organization
            repo_name (str): Repository name
            branch (str): Branch to push to (default: main)
            max_workers (int): Maximum number of concurrent download threads
            delay (float): Delay between API requests to avoid rate limiting
        """
        self.github_token = github_token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.branch = branch
        self.max_workers = max_workers
        self.delay = delay

        # Set up sessions
        self.quran_session = requests.Session()
        self.quran_session.headers.update({
            "User-Agent": "QuranAudioDownloader/1.0"
        })

        self.github_session = requests.Session()
        self.github_session.headers.update({
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        })

        # Check if repository exists and create if needed
        self._check_repository()

        # Keep track of created directories to avoid redundant checks
        self.created_dirs = set()

        # Queue for file uploads
        self.upload_queue = []

    def _check_repository(self):
        """Check if repository exists, create if it doesn't."""
        url = f"{self.GITHUB_API_URL}/repos/{self.repo_owner}/{self.repo_name}"
        response = self.github_session.get(url)

        if response.status_code == 404:
            # Create repository
            create_url = f"{self.GITHUB_API_URL}/user/repos"
            data = {
                "name": self.repo_name,
                "description": "Quran Audio Static API",
                "private": False,
                "auto_init": True  # Initialize with README
            }
            response = self.github_session.post(create_url, json=data)
            if response.status_code not in (201, 200):
                print(f"Failed to create repository: {response.status_code}")
                print(response.text)
                raise Exception("Failed to create repository")
            print(f"Created new repository: {self.repo_owner}/{self.repo_name}")
            time.sleep(2)  # Give GitHub time to initialize
        elif response.status_code != 200:
            print(f"Failed to check repository: {response.status_code}")
            print(response.text)
            raise Exception("Failed to check repository")

    def _make_request(self, endpoint, params=None):
        """Make an API request with retry logic."""
        url = f"{self.API_BASE_URL}/{endpoint}"
        for attempt in range(3):
            try:
                response = self.quran_session.get(url, params=params)
                response.raise_for_status()
                time.sleep(self.delay)  # Be nice to the API
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Request failed (attempt {attempt+1}/3): {e}")
                time.sleep(2 ** attempt)  # Exponential backoff

        print(f"Failed to fetch data from {url}")
        return None

    def _upload_to_github(self, file_path, content, is_binary=False):
        """
        Upload a file to GitHub repository.

        Args:
            file_path (str): Path to file in repository
            content: File content (bytes for binary, str for text)
            is_binary (bool): Whether the content is binary
        """
        # First, check if file exists to get its SHA (needed for update)
        url = f"{self.GITHUB_API_URL}/repos/{self.repo_owner}/{self.repo_name}/contents/{file_path}"
        response = self.github_session.get(url, params={"ref": self.branch})

        if is_binary:
            encoded_content = base64.b64encode(content).decode('utf-8')
        else:
            # For text content, ensure it's encoded to bytes first
            if isinstance(content, str):
                content = content.encode('utf-8')
            encoded_content = base64.b64encode(content).decode('utf-8')

        data = {
            "message": f"Add {file_path}",
            "content": encoded_content,
            "branch": self.branch
        }

        # If file exists, we need to include its SHA
        if response.status_code == 200:
            data["sha"] = response.json()["sha"]
            data["message"] = f"Update {file_path}"

        # Create/update the file
        response = self.github_session.put(url, json=data)

        if response.status_code not in (200, 201):
            print(f"Failed to upload {file_path}: {response.status_code}")
            print(response.text)
            return False

        return True

    def _download_and_upload(self, url, repo_path):
        """Download a file from URL and upload it directly to GitHub."""
        try:
            # Download file
            response = self.quran_session.get(url, stream=True)
            response.raise_for_status()

            # Read file content into memory
            content = io.BytesIO()
            for chunk in response.iter_content(chunk_size=8192):
                content.write(chunk)

            # Upload to GitHub
            return self._upload_to_github(repo_path, content.getvalue(), is_binary=True)
        except Exception as e:
            print(f"Failed to process {url} -> {repo_path}: {e}")
            return False

    def _verse_key_sort_key(self, verse_item):
        """Create a proper sort key for verse_key (e.g., "2:10")."""
        chapter, verse = verse_item["verse_key"].split(":")
        return (int(chapter), int(verse))

    def get_reciters(self):
        """Get list of all available reciters."""
        data = self._make_request("resources/recitations")
        if not data:
            return []
        return data.get("recitations", [])

    def get_chapter_recitations(self, reciter_id):
        """Get all chapter audio files for a reciter."""
        data = self._make_request(f"chapter_recitations/{reciter_id}")
        if not data:
            return []
        return data.get("audio_files", [])

    def get_verse_recitations(self, reciter_id):
        """Get all verse audio files for a reciter."""
        data = self._make_request(f"quran/recitations/{reciter_id}")
        if not data:
            return {"audio_files": [], "meta": {}}
        return data

    def get_verses_by_chapter(self, reciter_id, chapter_number):
        """Get all verse audio files for a specific chapter."""
        data = self._make_request(f"recitations/{reciter_id}/by_chapter/{chapter_number}",
                                  {"per_page": 1000})
        if not data:
            return {"audio_files": [], "pagination": {}}
        return data

    def get_verses_by_juz(self, reciter_id, juz_number):
        """Get all verse audio files for a specific juz."""
        data = self._make_request(f"recitations/{reciter_id}/by_juz/{juz_number}",
                                  {"per_page": 1000})
        if not data:
            return {"audio_files": [], "pagination": {}}
        return data

    def get_verses_by_page(self, reciter_id, page_number):
        """Get all verse audio files for a specific page."""
        data = self._make_request(f"recitations/{reciter_id}/by_page/{page_number}",
                                  {"per_page": 1000})
        if not data:
            return {"audio_files": [], "pagination": {}}
        return data

    def get_verses_by_hizb(self, reciter_id, hizb_number):
        """Get all verse audio files for a specific hizb."""
        data = self._make_request(f"recitations/{reciter_id}/by_hizb/{hizb_number}",
                                  {"per_page": 1000})
        if not data:
            return {"audio_files": [], "pagination": {}}
        return data

    def get_verses_by_rub(self, reciter_id, rub_number):
        """Get all verse audio files for a specific rub el hizb."""
        data = self._make_request(f"recitations/{reciter_id}/by_rub/{rub_number}",
                                  {"per_page": 1000})
        if not data:
            return {"audio_files": [], "pagination": {}}
        return data

    def _create_chapter_audio_json(self, reciter_id, reciter_info):
        """Create chapter audio files JSON for a reciter."""
        chapter_files = self.get_chapter_recitations(reciter_id)

        # Create chapter list file
        chapter_dir_path = f"reciters/{reciter_id}/chapters"

        chapter_list = {
            "recitation_id": reciter_id,
            "reciter_name": reciter_info["reciter_name"],
            "style": reciter_info["style"],
            "chapters": []
        }

        for chapter_file in chapter_files:
            # Skip if chapter_id is None
            if chapter_file["chapter_id"] is None:
                print(f"Skipping chapter with None ID for reciter {reciter_id}")
                continue

            chapter_number = chapter_file["chapter_id"]
            file_url = chapter_file["audio_url"]
            relative_path = f"/reciters/{reciter_id}/chapters/{chapter_number}.mp3"

            chapter_list["chapters"].append({
                "chapter_id": chapter_number,
                "file_size": chapter_file["file_size"],
                "format": chapter_file["format"],
                "audio_path": relative_path
            })

            # Add chapter audio file to download queue
            repo_path = f"reciters/{reciter_id}/chapters/{chapter_number}.mp3"
            self.upload_queue.append((file_url, repo_path))

        # Sort chapters by chapter_id
        chapter_list["chapters"].sort(key=lambda x: x["chapter_id"])

        # Upload chapter list
        list_path = f"{chapter_dir_path}/chapter_list.json"
        self._upload_to_github(
            list_path,
            json.dumps(chapter_list, ensure_ascii=False, indent=2)
        )

    def _create_verse_audio_metadata(self, reciter_id, reciter_info):
        """Create verse audio metadata files for various divisions."""
        # Get all verses for this reciter
        verse_data = self.get_verse_recitations(reciter_id)
        audio_files = verse_data.get("audio_files", [])
        meta = verse_data.get("meta", {})

        # Organize verses by chapter
        chapters = {}
        for audio_file in audio_files:
            verse_key = audio_file["verse_key"]
            chapter_num, verse_num = map(int, verse_key.split(":"))

            if chapter_num not in chapters:
                chapters[chapter_num] = []

            chapters[chapter_num].append({
                "verse_key": verse_key,
                "url": audio_file["url"],
                "audio_path": f"/reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
            })

            # Add to download queue
            audio_url = f"{self.AUDIO_BASE_URL}/{audio_file['url']}"
            repo_path = f"reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
            self.upload_queue.append((audio_url, repo_path))

        # Create chapter JSON files
        for chapter_num, verses in chapters.items():
            chapter_data = {
                "chapter_number": chapter_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "verses": sorted(verses, key=self._verse_key_sort_key)
            }

            chapter_path = f"reciters/{reciter_id}/verses/chapter/{chapter_num}.json"
            self._upload_to_github(
                chapter_path,
                json.dumps(chapter_data, ensure_ascii=False, indent=2)
            )

        # Create files for juz, page, hizb, and rub
        self._create_juz_files(reciter_id, reciter_info)
        self._create_page_files(reciter_id, reciter_info)
        self._create_hizb_files(reciter_id, reciter_info)
        self._create_rub_files(reciter_id, reciter_info)

    def _create_juz_files(self, reciter_id, reciter_info):
        """Create JSON files for each juz."""
        for juz_num in range(1, 31):  # Quran has 30 juz
            juz_data = self.get_verses_by_juz(reciter_id, juz_num)
            audio_files = juz_data.get("audio_files", [])

            if not audio_files:
                continue

            verses = []
            for audio_file in audio_files:
                verse_key = audio_file["verse_key"]
                chapter_num, verse_num = map(int, verse_key.split(":"))

                verses.append({
                    "verse_key": verse_key,
                    "audio_path": f"/reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                })

            juz_info = {
                "juz_number": juz_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "total_verses": len(verses),
                "verses": sorted(verses, key=self._verse_key_sort_key)
            }

            juz_path = f"reciters/{reciter_id}/verses/juz/{juz_num}.json"
            self._upload_to_github(
                juz_path,
                json.dumps(juz_info, ensure_ascii=False, indent=2)
            )

    def _create_page_files(self, reciter_id, reciter_info):
        """Create JSON files for each page."""
        # Quran has 604 pages in standard Madani mushaf
        for page_num in range(1, 605):
            page_data = self.get_verses_by_page(reciter_id, page_num)
            audio_files = page_data.get("audio_files", [])

            if not audio_files:
                continue

            verses = []
            for audio_file in audio_files:
                verse_key = audio_file["verse_key"]
                chapter_num, verse_num = map(int, verse_key.split(":"))

                verses.append({
                    "verse_key": verse_key,
                    "audio_path": f"/reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                })

            page_info = {
                "page_number": page_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "total_verses": len(verses),
                "verses": sorted(verses, key=self._verse_key_sort_key)
            }

            page_path = f"reciters/{reciter_id}/verses/page/{page_num}.json"
            self._upload_to_github(
                page_path,
                json.dumps(page_info, ensure_ascii=False, indent=2)
            )

    def _create_hizb_files(self, reciter_id, reciter_info):
        """Create JSON files for each hizb."""
        for hizb_num in range(1, 61):  # Quran has 60 hizbs
            hizb_data = self.get_verses_by_hizb(reciter_id, hizb_num)
            audio_files = hizb_data.get("audio_files", [])

            if not audio_files:
                continue

            verses = []
            for audio_file in audio_files:
                verse_key = audio_file["verse_key"]
                chapter_num, verse_num = map(int, verse_key.split(":"))

                verses.append({
                    "verse_key": verse_key,
                    "audio_path": f"/reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                })

            hizb_info = {
                "hizb_number": hizb_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "total_verses": len(verses),
                "verses": sorted(verses, key=self._verse_key_sort_key)
            }

            hizb_path = f"reciters/{reciter_id}/verses/hizb/{hizb_num}.json"
            self._upload_to_github(
                hizb_path,
                json.dumps(hizb_info, ensure_ascii=False, indent=2)
            )

    def _create_rub_files(self, reciter_id, reciter_info):
        """Create JSON files for each rub el hizb."""
        for rub_num in range(1, 241):  # Quran has 240 rub el hizbs (4 per hizb * 60 hizbs)
            rub_data = self.get_verses_by_rub(reciter_id, rub_num)
            audio_files = rub_data.get("audio_files", [])

            if not audio_files:
                continue

            verses = []
            for audio_file in audio_files:
                verse_key = audio_file["verse_key"]
                chapter_num, verse_num = map(int, verse_key.split(":"))

                verses.append({
                    "verse_key": verse_key,
                    "audio_path": f"/reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                })

            rub_info = {
                "rub_number": rub_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "total_verses": len(verses),
                "verses": sorted(verses, key=self._verse_key_sort_key)
            }

            rub_path = f"reciters/{reciter_id}/verses/rub/{rub_num}.json"
            self._upload_to_github(
                rub_path,
                json.dumps(rub_info, ensure_ascii=False, indent=2)
            )

    def process_reciter(self, reciter):
        """Process all data for a single reciter."""
        reciter_id = reciter["id"]
        print(f"Processing reciter {reciter_id}: {reciter['reciter_name']} ({reciter['style']})")

        # Create reciter info file
        reciter_info_path = f"reciters/{reciter_id}/info.json"
        self._upload_to_github(
            reciter_info_path,
            json.dumps(reciter, ensure_ascii=False, indent=2)
        )

        # Reset upload queue
        self.upload_queue = []

        # Create metadata files
        self._create_chapter_audio_json(reciter_id, reciter)
        self._create_verse_audio_metadata(reciter_id, reciter)

        # Process upload queue
        self._process_upload_queue(f"Uploading files for {reciter['reciter_name']} ({reciter['style']})")

    def _process_upload_queue(self, description):
        """Process all files in the upload queue using thread pool."""
        if not self.upload_queue:
            print("No files to upload.")
            return

        print(f"Uploading {len(self.upload_queue)} files to GitHub...")

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            list(tqdm(
                executor.map(lambda x: self._download_and_upload(*x), self.upload_queue),
                total=len(self.upload_queue),
                desc=description
            ))

    def create_static_api(self, selected_reciters=None):
        """
        Create the complete static API structure on GitHub.

        Args:
            selected_reciters (list): Optional list of reciter IDs to process
                                     If None, all reciters will be processed
        """
        # Get all reciters
        reciters = self.get_reciters()
        if not reciters:
            print("Failed to fetch reciters list")
            return

        print(f"Found {len(reciters)} reciters")

        # Filter reciters if specified
        if selected_reciters:
            reciters = [r for r in reciters if r["id"] in selected_reciters]
            print(f"Filtered to {len(reciters)} selected reciters")

        # Create reciters list file
        reciter_list_path = "reciters/reciter_list.json"
        self._upload_to_github(
            reciter_list_path,
            json.dumps({"reciters": reciters}, ensure_ascii=False, indent=2)
        )

        # Process each reciter
        for reciter in reciters:
            self.process_reciter(reciter)

        # Create API index and readme
        self._create_api_index()
        self._create_readme()

        print(f"Static API created successfully on GitHub: https://github.com/{self.repo_owner}/{self.repo_name}")

    def _create_api_index(self):
        """Create an index file with API documentation."""
        index = {
            "name": "Quran Audio Static API",
            "version": "1.0.0",
            "description": "Static API for Quran audio recitations",
            "endpoints": {
                "reciters": "/reciters/reciter_list.json",
                "reciter_info": "/reciters/{reciter_id}/info.json",
                "chapter_list": "/reciters/{reciter_id}/chapters/chapter_list.json",
                "chapter_audio": "/reciters/{reciter_id}/chapters/{chapter_number}.mp3",
                "verses_by_chapter": "/reciters/{reciter_id}/verses/chapter/{chapter_number}.json",
                "verses_by_juz": "/reciters/{reciter_id}/verses/juz/{juz_number}.json",
                "verses_by_page": "/reciters/{reciter_id}/verses/page/{page_number}.json",
                "verses_by_hizb": "/reciters/{reciter_id}/verses/hizb/{hizb_number}.json",
                "verses_by_rub": "/reciters/{reciter_id}/verses/rub/{rub_number}.json",
                "verse_audio": "/reciters/{reciter_id}/verses/ayah/{chapter_number}_{verse_number}.mp3"
            }
        }

        self._upload_to_github(
            "api_index.json",
            json.dumps(index, ensure_ascii=False, indent=2)
        )

    def _create_readme(self):
        """Create a README.md file with usage instructions."""
        readme = """# Quran Audio Static API

A static API for Quran audio recitations, organized for easy access and distribution.

## API Structure

- `/reciters/reciter_list.json` - List of all available reciters
- `/reciters/{reciter_id}/info.json` - Information about a specific reciter
- `/reciters/{reciter_id}/chapters/chapter_list.json` - List of all chapter audio files for a reciter
- `/reciters/{reciter_id}/chapters/{chapter_number}.mp3` - Audio file for a complete chapter
- `/reciters/{reciter_id}/verses/chapter/{chapter_number}.json` - Metadata for verses in a chapter
- `/reciters/{reciter_id}/verses/juz/{juz_number}.json` - Metadata for verses in a juz
- `/reciters/{reciter_id}/verses/page/{page_number}.json` - Metadata for verses on a page
- `/reciters/{reciter_id}/verses/hizb/{hizb_number}.json` - Metadata for verses in a hizb
- `/reciters/{reciter_id}/verses/rub/{rub_number}.json` - Metadata for verses in a rub el hizb
- `/reciters/{reciter_id}/verses/ayah/{chapter_number}_{verse_number}.mp3` - Audio file for a specific verse

## Usage Examples

### Get list of all reciters

```
GET /reciters/reciter_list.json
```

### Get audio file for a complete chapter (surah)

```
GET /reciters/1/chapters/1.mp3
```

### Get metadata for verses on a specific page

```
GET /reciters/1/verses/page/604.json
```

Then access individual verse audio files:

```
GET /reciters/1/verses/ayah/112_1.mp3
```

## GitHub Raw URLs

Access this content using raw GitHub URLs:

```
https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/reciters/1/verses/ayah/1_1.mp3
```

## Data Source

The data in this static API was downloaded from the Quran API (https://api.quran.com/api/v4).
"""

        self._upload_to_github("README.md", readme)


def main():
    """Main function to run the downloader."""
    import argparse

    parser = argparse.ArgumentParser(description="Download Quran audio files and create a static API on GitHub")
    parser.add_argument("--token", "-t", required=True,
                        help="GitHub personal access token with repo scope")
    parser.add_argument("--owner", "-o", required=True,
                        help="GitHub username/organization")
    parser.add_argument("--repo", "-r", required=True,
                        help="GitHub repository name (will be created if doesn't exist)")
    parser.add_argument("--branch", "-b", default="main",
                        help="Branch to push to (default: main)")
    parser.add_argument("--reciters", "-R", type=int, nargs="+",
                        help="List of reciter IDs to download (default: all reciters)")
    parser.add_argument("--workers", "-w", type=int, default=5,
                        help="Maximum number of concurrent upload threads")
    parser.add_argument("--delay", "-d", type=float, default=0.5,
                        help="Delay between API requests to avoid rate limiting")

    args = parser.parse_args()

    downloader = QuranAudioDownloaderToGitHub(
        github_token=args.token,
        repo_owner=args.owner,
        repo_name=args.repo,
        branch=args.branch,
        max_workers=args.workers,
        delay=args.delay
    )

    try:
        downloader.create_static_api(selected_reciters=args.reciters)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")


if __name__ == "__main__":
    main()
