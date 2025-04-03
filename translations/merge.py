import os
import json
import glob
from pathlib import Path

def load_reference_data():
    """Load reference data for all surahs and verses, including sajdah information."""
    reference_data = {}

    # Try to find the reference surah directory that contains the correct metadata
    reference_dirs = ["surah", "en/surah", "ar/surah"]  # Add more potential paths if needed

    reference_dir = None
    for dir_path in reference_dirs:
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            reference_dir = dir_path
            break

    if not reference_dir:
        print("Warning: Could not find reference surah directory. Using default values.")
        return reference_data

    # Load data from all surahs
    for surah_num in range(1, 115):
        surah_dir = os.path.join(reference_dir, str(surah_num))
        if not os.path.exists(surah_dir):
            continue

        reference_data[str(surah_num)] = {"verses": {}}

        # Load index file if it exists
        index_file = os.path.join(surah_dir, "index.json")
        if os.path.exists(index_file):
            try:
                with open(index_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if "verses" in data and isinstance(data["verses"], list):
                        for verse in data["verses"]:
                            verse_num = str(verse.get("number", ""))
                            if verse_num:
                                reference_data[str(surah_num)]["verses"][verse_num] = verse
            except json.JSONDecodeError:
                print(f"Error loading reference data from {index_file}")

        # Load individual verse files
        verse_files = glob.glob(os.path.join(surah_dir, "[0-9]*.json"))
        for verse_file in verse_files:
            try:
                verse_num = os.path.basename(verse_file).split('.')[0]
                with open(verse_file, 'r', encoding='utf-8') as f:
                    verse_data = json.load(f)
                    reference_data[str(surah_num)]["verses"][verse_num] = verse_data
            except (json.JSONDecodeError, IndexError):
                print(f"Error loading reference data from {verse_file}")

    return reference_data

def get_verse_metadata(reference_data, surah_num, verse_num):
    """Get metadata for a specific verse from reference data."""
    default_metadata = {
        "hizb_number": 1,
        "rub_el_hizb_number": 1,
        "ruku_number": 1,
        "manzil_number": 1,
        "sajdah_number": None,
        "page_number": 1,
        "juz_number": 1
    }

    if not reference_data:
        return default_metadata

    surah_data = reference_data.get(str(surah_num), {})
    verse_data = surah_data.get("verses", {}).get(str(verse_num), {})

    metadata = default_metadata.copy()

    # Update with reference data if available
    for key in metadata:
        if key in verse_data:
            metadata[key] = verse_data[key]

    return metadata

def transform_verse(verse_data, reference_data=None, surah_num=None, verse_num=None):
    """Transform a verse from the old format to the new format."""
    # Extract data from the old format
    sura = verse_data.get("sura", surah_num or "")
    aya = verse_data.get("aya", verse_num or "")

    # Get metadata from reference data
    metadata = get_verse_metadata(reference_data, sura, aya)

    # Create the new format
    new_verse = {
        "id": int(aya) if aya and aya.isdigit() else None,
        "number": int(aya) if aya and aya.isdigit() else None,
        "verse_key": f"{sura}:{aya}" if sura and aya else None,
        "hizb_number": metadata["hizb_number"],
        "rub_el_hizb_number": metadata["rub_el_hizb_number"],
        "ruku_number": metadata["ruku_number"],
        "manzil_number": metadata["manzil_number"],
        "sajdah_number": metadata["sajdah_number"],  # This will now be correct from reference data
        "page_number": metadata["page_number"],
        "juz_number": metadata["juz_number"],
        "arabic_text": verse_data.get("arabic_text", ""),
        "translation": verse_data.get("translation", ""),
        "footnotes": verse_data.get("footnotes", "")
    }

    return new_verse

def process_translation_folder(translation_path, reference_data):
    """Process a single translation folder."""
    print(f"Processing translation: {translation_path}")

    # Find all surah folders
    surah_folders = []

    # Check if there's a 'surah' subfolder
    surah_dir = os.path.join(translation_path, "surah")
    if os.path.exists(surah_dir) and os.path.isdir(surah_dir):
        # Get all numeric folders (1-114)
        for i in range(1, 115):
            surah_folder = os.path.join(surah_dir, str(i))
            if os.path.exists(surah_folder) and os.path.isdir(surah_folder):
                surah_folders.append((str(i), surah_folder))
    else:
        # Check if the translation folder directly contains numeric folders (1-114)
        for i in range(1, 115):
            surah_folder = os.path.join(translation_path, str(i))
            if os.path.exists(surah_folder) and os.path.isdir(surah_folder):
                surah_folders.append((str(i), surah_folder))

    # Process each surah folder
    for surah_num, surah_folder in surah_folders:
        process_surah_folder(surah_num, surah_folder, reference_data)

def process_surah_folder(surah_num, surah_folder, reference_data):
    """Process a single surah folder."""
    print(f"  Processing surah {surah_num}: {surah_folder}")

    # Check if there's an index.json file
    index_file = os.path.join(surah_folder, "index.json")
    if os.path.exists(index_file):
        # Process the index file (contains all verses)
        with open(index_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)

                # Check if the data has the old format
                if "result" in data and isinstance(data["result"], list):
                    verses = []
                    for verse_data in data["result"]:
                        verse_num = verse_data.get("aya", "")
                        new_verse = transform_verse(verse_data, reference_data, surah_num, verse_num)
                        verses.append(new_verse)

                    # Create the new index.json content
                    new_index_data = {"verses": verses}

                    # Write the new index.json
                    with open(index_file, 'w', encoding='utf-8') as f_out:
                        json.dump(new_index_data, f_out, ensure_ascii=False, indent=2)

                    # Also process individual verse files
                    for verse in verses:
                        verse_num = verse["number"]
                        verse_file = os.path.join(surah_folder, f"{verse_num}.json")

                        # Write the individual verse file
                        with open(verse_file, 'w', encoding='utf-8') as f_verse:
                            json.dump(verse, f_verse, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                print(f"    Error: Could not parse {index_file}")

    # Process individual verse files if they exist
    verse_files = glob.glob(os.path.join(surah_folder, "[0-9]*.json"))
    for verse_file in verse_files:
        if os.path.basename(verse_file) != "index.json":
            try:
                verse_num = os.path.basename(verse_file).split('.')[0]
                with open(verse_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                    # Check if the data has the old format
                    if "result" in data and isinstance(data["result"], dict):
                        verse_data = data["result"]
                        new_verse = transform_verse(verse_data, reference_data, surah_num, verse_num)

                        # Write the transformed verse
                        with open(verse_file, 'w', encoding='utf-8') as f_out:
                            json.dump(new_verse, f_out, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                print(f"    Error: Could not parse {verse_file}")

def main():
    # Root directory containing all language folders
    root_dir = "."  # Change this to the actual root directory

    # Load reference data first
    print("Loading reference data...")
    reference_data = load_reference_data()
    print(f"Loaded reference data for {len(reference_data)} surahs")

    # Get all language folders
    lang_folders = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f)) and len(f) <= 3]

    for lang in lang_folders:
        lang_path = os.path.join(root_dir, lang)
        print(f"Processing language: {lang}")

        # Process the default translation (directly under the language folder)
        for i in range(1, 115):
            surah_folder = os.path.join(lang_path, str(i))
            if os.path.exists(surah_folder) and os.path.isdir(surah_folder):
                process_surah_folder(str(i), surah_folder, reference_data)

        # Process all translation variants
        translation_variants = [d for d in os.listdir(lang_path)
                               if os.path.isdir(os.path.join(lang_path, d))
                               and d not in [str(i) for i in range(1, 115)]]

        for translation in translation_variants:
            translation_path = os.path.join(lang_path, translation)
            process_translation_folder(translation_path, reference_data)

if __name__ == "__main__":
    main()
