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
        self.download_json = True  # Default to downloading JSON files
        self.download_mp3 = True   # Default to downloading MP3 files
        self.stats = {
            "total_files": 0,
            "skipped_files": 0,
            "downloaded_files": 0,
            "failed_files": 0
        }

    def set_download_options(self, download_json=True, download_mp3=True):
        """
        Set which file types to download.

        Args:
            download_json (bool): Whether to download JSON metadata files
            download_mp3 (bool): Whether to download MP3 audio files
        """
        self.download_json = download_json
        self.download_mp3 = download_mp3

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

    def _get_full_audio_url(self, url):
        """
        Convert relative or protocol-relative URLs to absolute URLs.

        Args:
            url (str): The URL from the API response

        Returns:
            str: The full, absolute URL
        """
        # Handle protocol-relative URLs (starting with //)
        if url.startswith('//'):
            return f"https:{url}"

        # Handle relative URLs that need the verses.quran.foundation base
        elif not url.startswith('http'):
            # Check if the URL already has a domain part
            if '/' in url and not url.startswith('/'):
                # This is likely a relative URL for verses.quran.foundation
                return f"{self.AUDIO_BASE_URL}/{url}"
            # URLs that start with / but don't have a domain
            elif url.startswith('/'):
                return f"https:{url}"
            else:
                # Default case - use the AUDIO_BASE_URL
                return f"{self.AUDIO_BASE_URL}/{url}"

        # URL is already absolute
        return url

    def _download_file(self, url, output_path):
        """Download a file from URL to the specified path."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        self.stats["total_files"] += 1

        if output_path.exists():
            self.stats["skipped_files"] += 1
            return True  # Skip if file already exists

        # Convert to full URL if needed
        full_url = self._get_full_audio_url(url)

        try:
            response = self.session.get(full_url, stream=True)
            response.raise_for_status()

            temp_path = output_path.with_suffix('.tmp')
            with open(temp_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Rename once download is complete
            shutil.move(temp_path, output_path)
            self.stats["downloaded_files"] += 1
            return True
        except Exception as e:
            print(f"Failed to download {full_url}: {e}")
            self.stats["failed_files"] += 1
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

            # Download chapter audio file if MP3 downloads are enabled
            if self.download_mp3:
                output_path = self.output_dir / f"reciters/{reciter_id}/chapters/{chapter_number}.mp3"
                self.download_queue.append((file_url, output_path))

        # Sort chapters by chapter_id
        chapter_list["chapters"].sort(key=lambda x: x["chapter_id"])

        # Save chapter list if JSON downloads are enabled
        if self.download_json:
            json_path = chapter_dir / "chapter_list.json"
            if not json_path.exists() or self._should_update_json():
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(chapter_list, f, ensure_ascii=False, indent=2)

    def _should_update_json(self):
        """Determine if JSON files should be updated even if they exist."""
        # Always update JSON files in this implementation
        # You could add a parameter to control this behavior
        return True

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

            # Add to download queue if MP3 downloads are enabled
            if self.download_mp3:
                # Use the URL directly - it will be processed by _get_full_audio_url in _download_file
                output_path = self.output_dir / f"reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                self.download_queue.append((audio_file['url'], output_path))

        # Skip JSON creation if JSON downloads are disabled
        if not self.download_json:
            return

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

            json_path = chapter_dir / f"{chapter_num}.json"
            if not json_path.exists() or self._should_update_json():
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(chapter_data, f, ensure_ascii=False, indent=2)

        # Create files for juz, page, hizb, and rub
        self._create_juz_files(reciter_id, reciter_info)
        self._create_page_files(reciter_id, reciter_info)
        self._create_hizb_files(reciter_id, reciter_info)
        self._create_rub_files(reciter_id, reciter_info)

    def _create_juz_files(self, reciter_id, reciter_info):
        """Create JSON files for each juz."""
        # Skip if JSON downloads are disabled
        if not self.download_json:
            return

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

                # Add to download queue if MP3 downloads are enabled
                if self.download_mp3:
                    output_path = self.output_dir / f"reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                    self.download_queue.append((audio_file['url'], output_path))

            juz_info = {
                "juz_number": juz_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "total_verses": len(verses),
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            json_path = juz_dir / f"{juz_num}.json"
            if not json_path.exists() or self._should_update_json():
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(juz_info, f, ensure_ascii=False, indent=2)

    def _create_page_files(self, reciter_id, reciter_info):
        """Create JSON files for each page."""
        # Skip if JSON downloads are disabled
        if not self.download_json:
            return

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

                # Add to download queue if MP3 downloads are enabled
                if self.download_mp3:
                    output_path = self.output_dir / f"reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                    self.download_queue.append((audio_file['url'], output_path))

            page_info = {
                "page_number": page_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "total_verses": len(verses),
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            json_path = page_dir / f"{page_num}.json"
            if not json_path.exists() or self._should_update_json():
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(page_info, f, ensure_ascii=False, indent=2)

    def _create_hizb_files(self, reciter_id, reciter_info):
        """Create JSON files for each hizb."""
        # Skip if JSON downloads are disabled
        if not self.download_json:
            return

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

                # Add to download queue if MP3 downloads are enabled
                if self.download_mp3:
                    output_path = self.output_dir / f"reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                    self.download_queue.append((audio_file['url'], output_path))

            hizb_info = {
                "hizb_number": hizb_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "total_verses": len(verses),
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            json_path = hizb_dir / f"{hizb_num}.json"
            if not json_path.exists() or self._should_update_json():
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(hizb_info, f, ensure_ascii=False, indent=2)

    def _create_rub_files(self, reciter_id, reciter_info):
        """Create JSON files for each rub el hizb."""
        # Skip if JSON downloads are disabled
        if not self.download_json:
            return

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

                # Add to download queue if MP3 downloads are enabled
                if self.download_mp3:
                    output_path = self.output_dir / f"reciters/{reciter_id}/verses/ayah/{chapter_num}_{verse_num}.mp3"
                    self.download_queue.append((audio_file['url'], output_path))

            rub_info = {
                "rub_number": rub_num,
                "recitation_id": reciter_id,
                "reciter_name": reciter_info["reciter_name"],
                "style": reciter_info["style"],
                "total_verses": len(verses),
                "verses": sorted(verses, key=self._verse_key_sort_key) # Using proper verse key sorting
            }

            json_path = rub_dir / f"{rub_num}.json"
            if not json_path.exists() or self._should_update_json():
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(rub_info, f, ensure_ascii=False, indent=2)

    def process_reciter(self, reciter):
        """Process all data for a single reciter."""
        reciter_id = reciter["id"]
        print(f"Processing reciter {reciter_id}: {reciter['reciter_name']} ({reciter['style']})")

        # Create reciter info file if JSON downloads are enabled
        reciter_dir = self.output_dir / "reciters" / str(reciter_id)
        reciter_dir.mkdir(parents=True, exist_ok=True)

        if self.download_json:
            json_path = reciter_dir / "info.json"
            if not json_path.exists() or self._should_update_json():
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(reciter, f, ensure_ascii=False, indent=2)

        # Create all necessary directories based on what we're downloading
        subdirs = []
        if self.download_json:
            subdirs.extend(["chapters", "verses/chapter", "verses/juz",
                          "verses/page", "verses/hizb", "verses/rub"])
        if self.download_mp3:
            subdirs.extend(["chapters", "verses/ayah"])

        # Create unique subdirectories (removing duplicates)
        for subdir in set(subdirs):
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

        # Skip processing if we're not supposed to download MP3s
        if not self.download_mp3 and all("mp3" in str(path).lower() for _, path in self.download_queue):
            print("Skipping MP3 downloads as requested.")
            self.download_queue = []  # Clear the queue
            return

        # Remove duplicates from download queue (same destination path)
        unique_queue = {}
        for url, path in self.download_queue:
            unique_queue[str(path)] = (url, path)

        self.download_queue = list(unique_queue.values())
        print(f"Downloading {len(self.download_queue)} files (after removing duplicates)...")

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
        # Reset stats
        self.stats = {
            "total_files": 0,
            "skipped_files": 0,
            "downloaded_files": 0,
            "failed_files": 0
        }

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

        # Create reciters list file if JSON downloads are enabled
        if self.download_json:
            reciters_dir = self.output_dir / "reciters"
            reciters_dir.mkdir(parents=True, exist_ok=True)

            json_path = reciters_dir / "reciter_list.json"
            if not json_path.exists() or self._should_update_json():
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump({"reciters": reciters}, f, ensure_ascii=False, indent=2)

        # Process each reciter
        for reciter in reciters:
            self.process_reciter(reciter)

        # Create API index if JSON downloads are enabled
        if self.download_json:
            self._create_api_index()

        print(f"Static API created successfully at: {self.output_dir}")

        # Print summary of what was downloaded
        print(f"Download summary:")
        print(f"- JSON metadata files: {'Yes' if self.download_json else 'No'}")
        print(f"- MP3 audio files: {'Yes' if self.download_mp3 else 'No'}")
        print(f"- Total files processed: {self.stats['total_files']}")
        print(f"- Files already existing (skipped): {self.stats['skipped_files']}")
        print(f"- Files downloaded: {self.stats['downloaded_files']}")
        print(f"- Files failed: {self.stats['failed_files']}")

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

        json_path = self.output_dir / "api_index.json"
        if not json_path.exists() or self._should_update_json():
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(index, f, ensure_ascii=False, indent=2)


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
    parser.add_argument("--files", choices=["json", "mp3", "both"], default="both",
                        help="File types to download: 'json' for metadata only, 'mp3' for audio only, 'both' for all files (default: both)")

    args = parser.parse_args()

    downloader = QuranAudioDownloader(
        output_dir=args.output,
        max_workers=args.workers,
        delay=args.delay
    )

    # Set download options based on user input
    if args.files == "json":
        downloader.set_download_options(download_json=True, download_mp3=False)
        print("Downloading JSON metadata files only")
    elif args.files == "mp3":
        downloader.set_download_options(download_json=False, download_mp3=True)
        print("Downloading MP3 audio files only")
    else:  # "both"
        downloader.set_download_options(download_json=True, download_mp3=True)
        print("Downloading both JSON metadata and MP3 audio files")

    try:
        downloader.create_static_api(selected_reciters=args.reciters)
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")


if __name__ == "__main__":
    main()
