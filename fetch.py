import os
import json
import time
import requests
from pathlib import Path
from typing import Dict, List, Any
import shutil

# Base URL for the QuranEnc API
BASE_URL = "https://quranenc.com/api/v1"

# Number of surahs in the Quran
TOTAL_SURAHS = 114

# Dictionary mapping surah numbers to their ayah counts
SURAH_AYAH_COUNT = {
    1: 7, 2: 286, 3: 200, 4: 176, 5: 120, 6: 165, 7: 206, 8: 75, 9: 129, 10: 109,
    11: 123, 12: 111, 13: 43, 14: 52, 15: 99, 16: 128, 17: 111, 18: 110, 19: 98, 20: 135,
    21: 112, 22: 78, 23: 118, 24: 64, 25: 77, 26: 227, 27: 93, 28: 88, 29: 69, 30: 60,
    31: 34, 32: 30, 33: 73, 34: 54, 35: 45, 36: 83, 37: 182, 38: 88, 39: 75, 40: 85,
    41: 54, 42: 53, 43: 89, 44: 59, 45: 37, 46: 35, 47: 38, 48: 29, 49: 18, 50: 45,
    51: 60, 52: 49, 53: 62, 54: 55, 55: 78, 56: 96, 57: 29, 58: 22, 59: 24, 60: 13,
    61: 14, 62: 11, 63: 11, 64: 18, 65: 12, 66: 12, 67: 30, 68: 52, 69: 52, 70: 44,
    71: 28, 72: 28, 73: 20, 74: 56, 75: 40, 76: 31, 77: 50, 78: 40, 79: 46, 80: 42,
    81: 29, 82: 19, 83: 36, 84: 25, 85: 22, 86: 17, 87: 19, 88: 26, 89: 30, 90: 20,
    91: 15, 92: 21, 93: 11, 94: 8, 95: 8, 96: 19, 97: 5, 98: 8, 99: 8, 100: 11,
    101: 11, 102: 8, 103: 3, 104: 9, 105: 5, 106: 4, 107: 7, 108: 3, 109: 6, 110: 3,
    111: 5, 112: 4, 113: 5, 114: 6
}

class QuranStaticApiGenerator:
    def __init__(self, base_path="quran-api"):
        self.base_path = Path(base_path)
        self.api_path = self.base_path / "api"

        # Clean any existing data
        if os.path.exists(self.base_path):
            choice = input(f"Directory {self.base_path} already exists. Delete and recreate? (y/n): ")
            if choice.lower() == 'y':
                shutil.rmtree(self.base_path)
            else:
                print("Using existing directory. Some files may be overwritten.")

        # Create directories
        os.makedirs(self.base_path, exist_ok=True)
        os.makedirs(self.api_path, exist_ok=True)

        # Translations metadata storage
        self.translations_metadata = {}

    def fetch_data(self, url: str) -> Dict:
        """
        Fetch data from the API with error handling and rate limiting.
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: Received status code {response.status_code} from {url}")
                return {}
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return {}
        finally:
            # Add a small delay to avoid hitting rate limits
            time.sleep(0.5)

    def download_languages_and_isocodes(self):
        """
        Download the languages and isocodes JSON files and create API endpoints for them.
        """
        # Fetch languages data
        languages_url = f"{BASE_URL}/translations/languages"
        languages_data = self.fetch_data(languages_url)

        if languages_data:
            # Create API endpoint
            languages_api_dir = self.api_path / "languages"
            os.makedirs(languages_api_dir, exist_ok=True)

            with open(languages_api_dir / "index.json", "w", encoding="utf-8") as f:
                json.dump(languages_data, f, ensure_ascii=False, indent=2)

            print("Downloaded languages data and created API endpoint")

        # Fetch isocodes data
        isocodes_url = f"{BASE_URL}/translations/isocodes"
        isocodes_data = self.fetch_data(isocodes_url)

        if isocodes_data:
            # Create API endpoint
            isocodes_api_dir = self.api_path / "isocodes"
            os.makedirs(isocodes_api_dir, exist_ok=True)

            with open(isocodes_api_dir / "index.json", "w", encoding="utf-8") as f:
                json.dump(isocodes_data, f, ensure_ascii=False, indent=2)

            print("Downloaded isocodes data and created API endpoint")

        return languages_data, isocodes_data

    def download_translations_metadata(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Download the list of available translations and organize them by language.
        Creates API endpoints for translations.
        """
        translations_by_language = {}

        # Fetch all translations
        translations_url = f"{BASE_URL}/translations/list"
        translations_data = self.fetch_data(translations_url)

        if not translations_data or "translations" not in translations_data:
            print("Failed to fetch translations data")
            return translations_by_language

        # Create API endpoint for all translations
        translations_api_dir = self.api_path / "translations"
        os.makedirs(translations_api_dir, exist_ok=True)

        with open(translations_api_dir / "index.json", "w", encoding="utf-8") as f:
            json.dump(translations_data, f, ensure_ascii=False, indent=2)

        # Organize translations by language and create language-specific endpoints
        for translation in translations_data["translations"]:
            language_code = translation["language_iso_code"]
            if language_code not in translations_by_language:
                translations_by_language[language_code] = []
            translations_by_language[language_code].append(translation)

            # Store metadata for later use
            self.translations_metadata[translation["key"]] = translation

        # Create language-specific translation endpoints
        for lang_code, translations in translations_by_language.items():
            lang_dir = translations_api_dir / lang_code
            os.makedirs(lang_dir, exist_ok=True)

            lang_data = {"translations": translations}
            with open(lang_dir / "index.json", "w", encoding="utf-8") as f:
                json.dump(lang_data, f, ensure_ascii=False, indent=2)

        print(f"Downloaded translations metadata and created API endpoints for {len(translations_by_language)} languages")
        return translations_by_language

    def download_translation(self, language_code: str, translation_key: str, translation_metadata: Dict) -> None:
        """
        Download a specific translation and create API endpoints for it.
        """
        print(f"Downloading translation: {translation_key} ({language_code})")

        # Create directories for this translation
        translation_api_dir = self.api_path / language_code / translation_key
        os.makedirs(translation_api_dir, exist_ok=True)

        # Save translation metadata
        with open(translation_api_dir / "info.json", "w", encoding="utf-8") as f:
            json.dump(translation_metadata, f, ensure_ascii=False, indent=2)

        # Create surahs directory
        surahs_api_dir = translation_api_dir / "surah"
        os.makedirs(surahs_api_dir, exist_ok=True)

        # Download each surah
        for surah_number in range(1, TOTAL_SURAHS + 1):
            print(f"  Downloading Surah {surah_number}...")

            surah_api_dir = surahs_api_dir / str(surah_number)
            os.makedirs(surah_api_dir, exist_ok=True)

            # Fetch the entire surah at once
            surah_url = f"{BASE_URL}/translation/sura/{translation_key}/{surah_number}"
            surah_data = self.fetch_data(surah_url)

            if not surah_data or "result" not in surah_data:
                print(f"  Failed to fetch Surah {surah_number}")
                continue

            # Create API endpoint for the full surah
            with open(surah_api_dir / "index.json", "w", encoding="utf-8") as f:
                json.dump(surah_data, f, ensure_ascii=False, indent=2)

            # Process each ayah
            for ayah_data in surah_data["result"]:
                ayah_number = int(ayah_data["aya"])

                # Create API endpoint for this ayah
                ayah_result = {"result": ayah_data}
                with open(surah_api_dir / f"{ayah_number}.json", "w", encoding="utf-8") as f:
                    json.dump(ayah_result, f, ensure_ascii=False, indent=2)

            print(f"  Completed Surah {surah_number} ({len(surah_data['result'])} ayahs)")

    def create_default_quran_structure(self):
        """
        Create the default Quran structure without translations for direct access to surahs and ayahs.
        """
        print("Creating default Quran structure...")

        # Create directories
        quran_api_dir = self.api_path / "surah"
        os.makedirs(quran_api_dir, exist_ok=True)

        # We'll use the first translation we can find as the default structure
        default_translation = None
        for translation_key, metadata in self.translations_metadata.items():
            if metadata.get("language_iso_code") == "ar":  # Prefer Arabic
                default_translation = translation_key
                break
            elif default_translation is None:
                default_translation = translation_key

        if default_translation is None:
            print("No translations found to create default structure")
            return

        print(f"Using {default_translation} as template for default structure")

        # Download each surah
        for surah_number in range(1, TOTAL_SURAHS + 1):
            print(f"  Processing Surah {surah_number}...")

            surah_dir = quran_api_dir / str(surah_number)
            os.makedirs(surah_dir, exist_ok=True)

            # Fetch the surah data
            surah_url = f"{BASE_URL}/translation/sura/{default_translation}/{surah_number}"
            surah_data = self.fetch_data(surah_url)

            if not surah_data or "result" not in surah_data:
                print(f"  Failed to fetch Surah {surah_number}")
                continue

            # Extract just the structure (removing translation-specific content)
            surah_structure = {
                "surah": surah_number,
                "ayahs": []
            }

            for ayah_data in surah_data["result"]:
                ayah_number = int(ayah_data["aya"])

                # Extract core ayah data
                ayah_structure = {
                    "number": ayah_number,
                    "arabic_text": ayah_data["arabic_text"]
                }

                surah_structure["ayahs"].append(ayah_structure)

                # Create ayah endpoint
                ayah_endpoint = {"ayah": ayah_structure}
                with open(surah_dir / f"{ayah_number}.json", "w", encoding="utf-8") as f:
                    json.dump(ayah_endpoint, f, ensure_ascii=False, indent=2)

            # Create surah endpoint
            with open(surah_dir / "index.json", "w", encoding="utf-8") as f:
                json.dump({"surah": surah_structure}, f, ensure_ascii=False, indent=2)

            print(f"  Completed Surah {surah_number}")

    def create_readme(self):
        """
        Create a README file with API documentation.
        """
        readme_content = """# Quran Static API

This is a static API for the Quran that can be hosted without a backend server.

## API Endpoints

### Languages and Translations

- **Get all available languages:**
  - `/api/languages/index.json`

- **Get language ISO codes:**
  - `/api/isocodes/index.json`

- **Get all translations:**
  - `/api/translations/index.json`

- **Get translations for a specific language:**
  - `/api/{language_code}/index.json`

### Default Quran Structure

- **Get a specific surah:**
  - `/api/surah/{surah_number}/index.json`

- **Get a specific ayah:**
  - `/api/surah/{surah_number}/{ayah_number}.json`

### Translations

- **Get translation information:**
  - `/api/{language_code}/{translation_key}/info.json`

- **Get a surah in a specific translation:**
  - `/api/{language_code}/{translation_key}/surah/{surah_number}/index.json`

- **Get an ayah in a specific translation:**
  - `/api/{language_code}/{translation_key}/surah/{surah_number}/{ayah_number}.json`

## Examples

1. Get Surah Al-Fatiha (Surah 1):
   - `/api/surah/1/index.json`

2. Get Ayah 1 of Surah Al-Baqarah (Surah 2):
   - `/api/surah/2/1.json`

3. Get Surah Al-Ikhlas (Surah 112) in English (Saheeh International):
   - `/api/en/english_saheeh/surah/112/index.json`

4. Get Ayah 1 of Surah Al-Ikhlas in English:
   - `/api/en/english_saheeh/surah/112/1.json`

## Hosting Options

This static API can be hosted on:
- GitHub Pages
- jsDelivr (directly from a GitHub repository)
- Any static file hosting service
- Local file server

## Data Source

The data is sourced from the QuranEnc API.
"""

        with open(self.base_path / "README.md", "w", encoding="utf-8") as f:
            f.write(readme_content)

        print("Created README with API documentation")

    def create_html_explorer(self):
        """
        Create a simple HTML explorer for the API.
        """
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quran Static API Explorer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        h2 {
            color: #3498db;
            margin-top: 30px;
        }
        .endpoint {
            background-color: #f5f5f5;
            padding: 15px;
            border-left: 4px solid #3498db;
            margin-bottom: 15px;
        }
        .endpoint h3 {
            margin-top: 0;
        }
        .endpoint-url {
            font-family: monospace;
            background-color: #e0e0e0;
            padding: 5px 10px;
            border-radius: 3px;
        }
        .examples {
            margin-top: 40px;
        }
        .example {
            background-color: #f9f9f9;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        .example h4 {
            margin-top: 0;
            color: #2c3e50;
        }
        .try-button {
            display: inline-block;
            padding: 5px 10px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 3px;
            margin-top: 10px;
        }
        #response-container {
            margin-top: 30px;
            display: none;
        }
        #response {
            background-color: #2c3e50;
            color: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Quran Static API Explorer</h1>

        <p>This is an explorer for the Quran Static API. Use the examples below to see how the API works.</p>

        <h2>Endpoints</h2>

        <div class="endpoint">
            <h3>Languages and Translations</h3>
            <p><strong>Get all available languages:</strong></p>
            <div class="endpoint-url">/api/languages/index.json</div>
            <a href="api/languages/index.json" class="try-button" onclick="fetchEndpoint(event, this.href)">Try it</a>

            <p><strong>Get language ISO codes:</strong></p>
            <div class="endpoint-url">/api/isocodes/index.json</div>
            <a href="api/isocodes/index.json" class="try-button" onclick="fetchEndpoint(event, this.href)">Try it</a>

            <p><strong>Get all translations:</strong></p>
            <div class="endpoint-url">/api/translations/index.json</div>
            <a href="api/translations/index.json" class="try-button" onclick="fetchEndpoint(event, this.href)">Try it</a>
        </div>

        <div class="endpoint">
            <h3>Default Quran Structure</h3>
            <p><strong>Get a specific surah:</strong></p>
            <div class="endpoint-url">/api/surah/{surah_number}/index.json</div>

            <p><strong>Get a specific ayah:</strong></p>
            <div class="endpoint-url">/api/surah/{surah_number}/{ayah_number}.json</div>
        </div>

        <div class="endpoint">
            <h3>Translations</h3>
            <p><strong>Get translation information:</strong></p>
            <div class="endpoint-url">/api/{language_code}/{translation_key}/info.json</div>

            <p><strong>Get a surah in a specific translation:</strong></p>
            <div class="endpoint-url">/api/{language_code}/{translation_key}/surah/{surah_number}/index.json</div>

            <p><strong>Get an ayah in a specific translation:</strong></p>
            <div class="endpoint-url">/api/{language_code}/{translation_key}/surah/{surah_number}/{ayah_number}.json</div>
        </div>

        <h2 class="examples">Examples</h2>

        <div class="example">
            <h4>Get Surah Al-Fatiha (Surah 1)</h4>
            <div class="endpoint-url">/api/surah/1/index.json</div>
            <a href="api/surah/1/index.json" class="try-button" onclick="fetchEndpoint(event, this.href)">Try it</a>
        </div>

        <div class="example">
            <h4>Get Ayah 1 of Surah Al-Baqarah (Surah 2)</h4>
            <div class="endpoint-url">/api/surah/2/1.json</div>
            <a href="api/surah/2/1.json" class="try-button" onclick="fetchEndpoint(event, this.href)">Try it</a>
        </div>

        <div class="example">
            <h4>Get available English translations</h4>
            <div class="endpoint-url">/api/translations/en/index.json</div>
            <a href="api/translations/en/index.json" class="try-button" onclick="fetchEndpoint(event, this.href)">Try it</a>
        </div>

        <div id="response-container">
            <h3>Response</h3>
            <pre id="response"></pre>
        </div>
    </div>

    <script>
        async function fetchEndpoint(event, url) {
            event.preventDefault();

            try {
                const response = await fetch(url);
                const data = await response.json();

                document.getElementById('response-container').style.display = 'block';
                document.getElementById('response').textContent = JSON.stringify(data, null, 2);
            } catch (error) {
                document.getElementById('response-container').style.display = 'block';
                document.getElementById('response').textContent = `Error: ${error.message}`;
            }

            // Scroll to response
            document.getElementById('response-container').scrollIntoView({ behavior: 'smooth' });
        }
    </script>
</body>
</html>
"""

        with open(self.base_path / "index.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        print("Created HTML explorer for the API")

    def run(self):
        """
        Run the full download and API generation process.
        """
        print(f"Starting Quran Static API generation in {self.base_path}...")

        # Download languages and isocodes
        self.download_languages_and_isocodes()

        # Download translations metadata
        translations_by_language = self.download_translations_metadata()

        # Ask user which languages/translations to download
        print("\nAvailable languages:")
        for i, lang_code in enumerate(sorted(translations_by_language.keys()), 1):
            translation_count = len(translations_by_language[lang_code])
            print(f"{i}. {lang_code} ({translation_count} translations)")

        languages_to_download = input("\nEnter language codes to download (comma-separated, or 'all' for all): ")

        if languages_to_download.lower() == "all":
            selected_languages = list(translations_by_language.keys())
        else:
            selected_languages = [lang.strip() for lang in languages_to_download.split(",")]

        for language_code in selected_languages:
            if language_code not in translations_by_language:
                print(f"Language '{language_code}' not found. Skipping.")
                continue

            print(f"\nAvailable translations for {language_code}:")
            for i, translation in enumerate(translations_by_language[language_code], 1):
                print(f"{i}. {translation['key']} - {translation['title']}")

            translations_to_download = input("\nEnter translation indices to download (comma-separated, or 'all' for all): ")

            if translations_to_download.lower() == "all":
                selected_translations = range(1, len(translations_by_language[language_code]) + 1)
            else:
                selected_translations = [int(idx.strip()) for idx in translations_to_download.split(",") if idx.strip().isdigit()]

            for idx in selected_translations:
                if 1 <= idx <= len(translations_by_language[language_code]):
                    translation = translations_by_language[language_code][idx - 1]
                    self.download_translation(language_code, translation["key"], translation)
                else:
                    print(f"Invalid translation index: {idx}")

        # Create default Quran structure
        self.create_default_quran_structure()

        # Create documentation
        self.create_readme()
        self.create_html_explorer()

        print("\nQuran Static API generation completed!")
        print(f"You can now host the '{self.base_path}' directory as a static website or access it locally.")
        print("Open index.html in a web browser to explore the API.")

if __name__ == "__main__":
    generator = QuranStaticApiGenerator()
    generator.run()
