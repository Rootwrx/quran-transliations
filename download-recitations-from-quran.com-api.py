import os
import json
import time
import shutil
import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from pathlib import Path
from tqdm import tqdm

class QuranAudioDownloader:
    """Download and organize Quran audio files from the Quran API to create a static API."""

    API_BASE_URL = "https://api.quran.com/api/v4"
    AUDIO_BASE_URL = "https://verses.quran.foundation"
    DOWNLOAD_URL = "https://download.quranicaudio.com"

    def __init__(self, output_dir="quran-audio-api", max_workers=5, delay=0.5):
        """
        Initialize the downloader with configuration parameters.

        Args:
            output_dir (str): Directory to store the static API files
            max_workers (int): Maximum number of concurrent download threads
            delay (float): Delay between API requests to avoid rate limiting
        """
        self.output_dir = Path(output_dir)
        self.max_workers = max_workers
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "QuranAudioDownloader/1.0"
        })

    def _make_request(self, endpoint, params=None):
        """Make an API request with retry logic."""
        url = f"{self.API_BASE_URL}/{endpoint}"
        for attempt in range(3):
            try:
                response = self.session.get(url, params=params)
                response.raise_for_status()
                time.sleep(self.delay)  # Be nice to the API
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Request failed (attempt {attempt+1}/3): {e}")
                time.sleep(2 ** attempt)  # Exponential backoff

        print(f"Failed to fetch data from {url}")
        return None

    def _download_file(self, url, output_path):
        """Download a file from URL to the specified path."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_path.exists():
            return True  # Skip if file already exists

        try:
            response = self.session.get(url, stream=True)
            response.raise_for_status()

            temp_path = output_path.with_suffix('.tmp')
            with open(temp_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Rename once download is complete
            shutil.move(temp_path, output_path)
            return True
        except Exception as e:
            print(f"Failed to download {url}: {e}")
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
        chapter_dir = self.output_dir / "reciters" / str(reciter_id) / "chapters"
        chapter_dir.mkdir(parents=True, exist_ok=True)

        chapter_list = {
            "recitation_id": reciter_id,
            "reciter_name": reciter_info["reciter_name"],
            "style": reciter_info["style"],
            "chapters": []
        }

        for chapter_file in chapter_files:
            chapter_number = chapter_file["chapter_id"]
            file_url = chapter_file["audio_url"]
            relative_path = f"/reciters/{reciter_id}/chapters/{chapter_number}.mp3"

            chapter_list["chapters"].append({
                "chapter_id": chapter_number,
                "file_size": chapter_file["file_size"],
                "format": chapter_file["format"],
                "audio_path": relative_path
            })

            # Download chapter audio file
            output_path = self.output_dir / f"reciters/{reciter_id}/chapters/{chapter_number}.mp3"
            self.download_queue.append((file_url, output_path))

        # Sort chapters by chapter_id
        chapter_list["chapters"].sort(key=lambda x: x["chapter_id"])

        # Save chapter list
        with open(chapter_dir / "chapter_list.json", "w", encoding="utf-8") as f:
            json.dump(chapter_list, f, ensure_ascii=False, indent=2)

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
            output_path = self.output_dir / f"reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
            self.download_queue.append((audio_url, output_path))

        # Create chapter JSON files
        chapter_dir = self.output_dir / f"reciters/{reciter_id}/verses/chapter"
        chapter_dir.mkdir(parents=True, exist_ok=True)

        for chapter_num, verses in chapters.items():
            chapter_data = {
                "chapter_number": chapter_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            with open(chapter_dir / f"{chapter_num}.json", "w", encoding="utf-8") as f:
                json.dump(chapter_data, f, ensure_ascii=False, indent=2)

        # Create files for juz, page, hizb, and rub
        self._create_juz_files(reciter_id, reciter_info)
        self._create_page_files(reciter_id, reciter_info)
        self._create_hizb_files(reciter_id, reciter_info)
        self._create_rub_files(reciter_id, reciter_info)

    def _create_juz_files(self, reciter_id, reciter_info):
        """Create JSON files for each juz."""
        juz_dir = self.output_dir / f"reciters/{reciter_id}/verses/juz"
        juz_dir.mkdir(parents=True, exist_ok=True)

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
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            with open(juz_dir / f"{juz_num}.json", "w", encoding="utf-8") as f:
                json.dump(juz_info, f, ensure_ascii=False, indent=2)

    def _create_page_files(self, reciter_id, reciter_info):
        """Create JSON files for each page."""
        page_dir = self.output_dir / f"reciters/{reciter_id}/verses/page"
        page_dir.mkdir(parents=True, exist_ok=True)

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
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            with open(page_dir / f"{page_num}.json", "w", encoding="utf-8") as f:
                json.dump(page_info, f, ensure_ascii=False, indent=2)

    def _create_hizb_files(self, reciter_id, reciter_info):
        """Create JSON files for each hizb."""
        hizb_dir = self.output_dir / f"reciters/{reciter_id}/verses/hizb"
        hizb_dir.mkdir(parents=True, exist_ok=True)

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
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            with open(hizb_dir / f"{hizb_num}.json", "w", encoding="utf-8") as f:
                json.dump(hizb_info, f, ensure_ascii=False, indent=2)

    def _create_rub_files(self, reciter_id, reciter_info):
        """Create JSON files for each rub el hizb."""
        rub_dir = self.output_dir / f"reciters/{reciter_id}/verses/rub"
        rub_dir.mkdir(parents=True, exist_ok=True)

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
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            with open(rub_dir / f"{rub_num}.json", "w", encoding="utf-8") as f:
                json.dump(rub_info, f, ensure_ascii=False, indent=2)

    def process_reciter(self, reciter):
        """Process all data for a single reciter."""
        reciter_id = reciter["id"]
        print(f"Processing reciter {reciter_id}: {reciter['reciter_name']} ({reciter['style']})")

        # Create reciter info file
        reciter_dir = self.output_dir / "reciters" / str(reciter_id)
        reciter_dir.mkdir(parents=True, exist_ok=True)

        with open(reciter_dir / "info.json", "w", encoding="utf-8") as f:
            json.dump(reciter, f, ensure_ascii=False, indent=2)

        # Create all necessary directories
        for subdir in ["chapters", "verses/ayah", "verses/chapter", "verses/juz",
                       "verses/page", "verses/hizb", "verses/rub"]:
            (reciter_dir / subdir).mkdir(parents=True, exist_ok=True)

        # Reset download queue
        self.download_queue = []

        # Create metadata files
        self._create_chapter_audio_json(reciter_id, reciter)
        self._create_verse_audio_metadata(reciter_id, reciter)

        # Download all queued files
        self._process_download_queue(f"Downloading files for {reciter['reciter_name']} ({reciter['style']})")

    def _process_download_queue(self, description):
        """Process all files in the download queue using thread pool."""
        if not self.download_queue:
            print("No files to download.")
            return

        print(f"Downloading {len(self.download_queue)} files...")

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            list(tqdm(
                executor.map(lambda x: self._download_file(*x), self.download_queue),
                total=len(self.download_queue),
                desc=description
            ))

    def create_static_api(self, selected_reciters=None):
        """
        Create the complete static API structure.

        Args:
            selected_reciters (list): Optional list of reciter IDs to process
                                     If None, all reciters will be processed
        """
        # Create base directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

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
        reciters_dir = self.output_dir / "reciters"
        reciters_dir.mkdir(parents=True, exist_ok=True)

        with open(reciters_dir / "reciter_list.json", "w", encoding="utf-8") as f:
            json.dump({"reciters": reciters}, f, ensure_ascii=False, indent=2)

        # Process each reciter
        for reciter in reciters:
            self.process_reciter(reciter)

        # Create API index and readme
        self._create_api_index()
        self._create_readme()

        print(f"Static API created successfully at: {self.output_dir}")

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

        with open(self.output_dir / "api_index.json", "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, indent=2)

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

When hosting on GitHub, use raw URLs:

```
https://raw.githubusercontent.com/username/repo/main/reciters/1/verses/ayah/1_1.mp3
```

## Data Source

The data in this static API was downloaded from the Quran API (https://api.quran.com/api/v4).
"""

        with open(self.output_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(readme)


def main():
    """Main function to run the downloader."""
    import argparse

    parser = argparse.ArgumentParser(description="Download Quran audio files and create a static API")
    parser.add_argument("--output", "-o", default="quran-audio-api",
                        help="Output directory for the static API")
    parser.add_argument("--reciters", "-r", type=int, nargs="+",
                        help="List of reciter IDs to download (default: all reciters)")
    parser.add_argument("--workers", "-w", type=int, default=5,
                        help="Maximum number of concurrent download threads")
    parser.add_argument("--delay", "-d", type=float, default=0.5,
                        help="Delay between API requests to avoid rate limiting")

    args = parser.parse_args()

    downloader = QuranAudioDownloader(
        output_dir=args.output,
        max_workers=args.workers,
        delay=args.delay
    )

    try:
        downloader.create_static_api(selected_reciters=args.reciters)
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")


if __name__ == "__main__":
    main()
