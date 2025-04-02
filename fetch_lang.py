import os
import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor

# Define available languages and their translation IDs from quran.com API
LANGUAGE_TRANSLATION_IDS = {
    "en": 38,   # English
    "ur": 174,  # Urdu
    "bn": 20,   # Bengali
    "tr": 167,  # Turkish
    "es": 40,   # Spanish
    "fr": 49,   # French
    "bs": 23,   # Bosnian
    "ru": 138,  # Russian
    "ml": 106,  # Malayalam
    "id": 67,   # Indonesian
    "uz": 175,  # Uzbek
    "nl": 118,  # Dutch
    "de": 33,   # German
    "tg": 160,  # Tajik
    "ta": 158,  # Tamil
    "ja": 76,   # Japanese
    "it": 74,   # Italian
    "vi": 177,  # Vietnamese
    "zh": 185,  # Chinese
    "sq": 187,  # Albanian
    "fa": 43,   # Persian
    "bg": 16,   # Bulgarian
    "bm": 19,   # Bambara
    "ha": 58,   # Hausa
    "pt": 133,  # Portuguese
    "ro": 137,  # Romanian
    "hi": 60,   # Hindi
    "sw": 157,  # Swahili
    "kk": 82,   # Kazakh
    "th": 161,  # Thai
    "tl": 164,  # Tagalog
    "km": 84,   # Central Khmer
    "as": 10,   # Assamese
    "ko": 86,   # Korean
    "so": 150,  # Somali
    "az": 13,   # Azeri
    "ku": 89,   # Kurdish
    "dv": 34,   # Divehi (Dhivehi, Maldivian)
    "ms": 110,  # Malay
    "prs": 190, # Dari
    "zgh": 188, # Amazigh
    "am": 6,    # Amharic
    "ce": 25,   # Chechen
    "cs": 29,   # Czech
    "fi": 45,   # Finnish
    "ar": 1     # Arabic (Original)
}

def fetch_verse_words(surah_num, verse_num):
    """Fetch word-by-word breakdown for a specific verse"""
    url = f"https://api.quran.com/api/v4/verses/by_key/{surah_num}:{verse_num}"
    params = {
        "words": "true",
        "word_fields": "text_indopak,text_uthmani,translation,transliteration"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching word data for {surah_num}:{verse_num}: {e}")
        return None

def fetch_verse_translation(surah_num, verse_num, language_code):
    """Fetch verse translation in a specific language"""
    if language_code not in LANGUAGE_TRANSLATION_IDS:
        print(f"Warning: Translation ID not found for language code {language_code}")
        return None

    translation_id = LANGUAGE_TRANSLATION_IDS[language_code]
    url = f"https://api.quran.com/api/v4/quran/translations/{translation_id}"
    params = {"verse_key": f"{surah_num}:{verse_num}"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {language_code} translation for {surah_num}:{verse_num}: {e}")
        return None

def fetch_chapter_info(surah_num, language_code):
    """Fetch chapter information in a specific language"""
    url = f"https://api.quran.com/api/v4/chapters/{surah_num}/info"
    params = {"language": language_code}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching chapter info for {surah_num} in {language_code}: {e}")
        return None

def get_verse_count(surah_num):
    """Get the number of verses in a surah"""
    surah_verse_counts = {
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
    return surah_verse_counts.get(surah_num, 0)

def process_verse(surah_num, verse_num, languages, base_dir):
    """Process a single verse for multiple languages"""
    surah_str = str(surah_num)
    verse_str = str(verse_num)

    # Fetch word-by-word data (language agnostic)
    words_data = fetch_verse_words(surah_num, verse_num)
    if words_data:
        # Store in main verse directory
        verse_dir = os.path.join(base_dir, surah_str, 'verses', verse_str)
        os.makedirs(verse_dir, exist_ok=True)
        with open(os.path.join(verse_dir, 'words.json'), 'w', encoding='utf-8') as f:
            json.dump(words_data, f, ensure_ascii=False, indent=2)

    # Fetch translations for each language
    for lang in languages:
        lang_dir = os.path.join(base_dir, lang, surah_str, 'verses', verse_str)
        os.makedirs(lang_dir, exist_ok=True)

        translation = fetch_verse_translation(surah_num, verse_num, lang)
        if translation:
            with open(os.path.join(lang_dir, 'translation.json'), 'w', encoding='utf-8') as f:
                json.dump(translation, f, ensure_ascii=False, indent=2)

    return f"Processed verse {surah_num}:{verse_num}"

def store_multilingual_quran_data(languages=None, base_dir='quran_data'):
    """
    Fetch and store Quran data in multiple languages

    Directory structure:
    quran_data/
    ├── surah/              # Original Arabic structure
    │   ├── 1/
    │   │   ├── info.json
    │   │   ├── verses/
    │   │   │   ├── 1/
    │   │   │   │   └── words.json
    │   │   │   └── ...
    │   │   └── ...
    │   └── ...
    ├── en/                # English translations
    │   ├── 1/
    │   │   ├── info.json
    │   │   ├── verses/
    │   │   │   ├── 1/
    │   │   │   │   └── translation.json
    │   │   │   └── ...
    │   │   └── ...
    │   └── ...
    └── [other languages]
    """
    # If no languages specified, use a default set
    if languages is None:
        languages = ["en", "es", "fr", "ar"]

    # Create base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create language directories
    for lang in languages:
        os.makedirs(os.path.join(base_dir, lang), exist_ok=True)

    # Create original surah directory
    surah_dir = os.path.join(base_dir, "surah")
    os.makedirs(surah_dir, exist_ok=True)

    # Process each surah
    for surah_num in range(1, 115):
        print(f"Processing Surah {surah_num}...")

        # Create surah directories for each language
        for lang in languages:
            lang_surah_dir = os.path.join(base_dir, lang, str(surah_num))
            os.makedirs(lang_surah_dir, exist_ok=True)

            # Fetch and store chapter info for this language
            chapter_info = fetch_chapter_info(surah_num, lang)
            if chapter_info:
                with open(os.path.join(lang_surah_dir, f"about.{lang}.json"), 'w', encoding='utf-8') as f:
                    json.dump(chapter_info, f, ensure_ascii=False, indent=2)

        # Get verse count for this surah
        verse_count = get_verse_count(surah_num)

        # Use ThreadPoolExecutor to process verses in parallel
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for verse_num in range(1, verse_count + 1):
                futures.append(
                    executor.submit(process_verse, surah_num, verse_num, languages, base_dir)
                )

            # Wait for all futures to complete and print results
            for future in futures:
                try:
                    print(future.result())
                except Exception as e:
                    print(f"Error in worker thread: {e}")

        # Add delay between surahs to avoid overwhelming the API
        time.sleep(2)

def fetch_specific_surah_multilingual(surah_num, languages=None, base_dir='quran_data'):
    """Fetch data for a specific surah in multiple languages"""
    if languages is None:
        languages = ["en", "es", "fr", "ar"]

    # Create base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create language directories
    for lang in languages:
        lang_dir = os.path.join(base_dir, lang, str(surah_num))
        os.makedirs(lang_dir, exist_ok=True)

        # Fetch and store chapter info
        chapter_info = fetch_chapter_info(surah_num, lang)
        if chapter_info:
            with open(os.path.join(lang_dir, f"about.{lang}.json"), 'w', encoding='utf-8') as f:
                json.dump(chapter_info, f, ensure_ascii=False, indent=2)

    # Create surah directory for original content
    surah_dir = os.path.join(base_dir, "surah", str(surah_num))
    os.makedirs(surah_dir, exist_ok=True)

    # Get verse count
    verse_count = get_verse_count(surah_num)

    # Process each verse
    for verse_num in range(1, verse_count + 1):
        process_verse(surah_num, verse_num, languages, base_dir)
        time.sleep(0.5)  # Small delay between verses

if __name__ == "__main__":
    # Choose which languages to fetch
    languages_to_fetch = ["en", "es"]

    # Option 1: Fetch data for all surahs (this will take a long time)
    # store_multilingual_quran_data(languages=languages_to_fetch)

    # Option 2: Fetch data for a specific surah (faster for testing)
    fetch_specific_surah_multilingual(1, languages=languages_to_fetch)

    print("Multilingual Quran data fetching complete!")
