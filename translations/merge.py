import os
import json
import glob
from pathlib import Path

def load_reference_data():
    """Load reference data for all surahs and verses from the surah directory."""
    reference_data = {}

    # Path to the reference surah directory
    surah_dir = "./surah"  # Adjust this path if needed

    if os.path.exists(surah_dir):
        # Process each surah folder (1-114)
        for surah_num in range(1, 115):
            surah_folder = os.path.join(surah_dir, str(surah_num))
            if os.path.exists(surah_folder):
                surah_data = {}

                # Load index.json if it exists
                index_file = os.path.join(surah_folder, "index.json")
                if os.path.exists(index_file):
                    try:
                        with open(index_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            if "verses" in data and isinstance(data["verses"], list):
                                for verse in data["verses"]:
                                    verse_num = verse.get("number")
                                    if verse_num:
                                        surah_data[verse_num] = verse
                    except json.JSONDecodeError:
                        print(f"Error loading reference data from {index_file}")

                # Load individual verse files
                verse_files = glob.glob(os.path.join(surah_folder, "[0-9]*.json"))
                for verse_file in verse_files:
                    try:
                        verse_num = int(os.path.splitext(os.path.basename(verse_file))[0])
                        with open(verse_file, 'r', encoding='utf-8') as f:
                            verse_data = json.load(f)
                            surah_data[verse_num] = verse_data
                    except (ValueError, json.JSONDecodeError):
                        continue

                reference_data[surah_num] = surah_data

    return reference_data

def get_verse_metadata(reference_data, surah_num, verse_num):
    """Get metadata for a specific verse from reference data."""
    try:
        surah_num = int(surah_num)
        verse_num = int(verse_num)

        if surah_num in reference_data and verse_num in reference_data[surah_num]:
            verse_data = reference_data[surah_num][verse_num]

            # Determine sajdah_type based on sajdah_number
            sajdah_type = None
            if verse_data.get("sajdah_number") is not None:
                sajdah_type = "obligatory"  # Default to obligatory, adjust as needed

            return {
                "hizb_number": verse_data.get("hizb_number", 1),
                "rub_el_hizb_number": verse_data.get("rub_el_hizb_number", 1),
                "ruku_number": verse_data.get("ruku_number", 1),
                "manzil_number": verse_data.get("manzil_number", 1),
                "sajdah_number": verse_data.get("sajdah_number"),
                "sajdah_type": verse_data.get("sajdah_type", sajdah_type),
                "page_number": verse_data.get("page_number", 1),
                "juz_number": verse_data.get("juz_number", 1)
            }
    except (ValueError, TypeError):
        pass

    # Default values if reference data is not available
    return {
        "hizb_number": 1,
        "rub_el_hizb_number": 1,
        "ruku_number": 1,
        "manzil_number": 1,
        "sajdah_number": None,
        "sajdah_type": None,
        "page_number": 1,
        "juz_number": 1
    }

def transform_verse(verse_data, reference_data=None, surah_num=None):
    """Transform a verse from the old format to the new format."""
    # Extract data from the old format
    sura = verse_data.get("sura", surah_num)
    aya = verse_data.get("aya", "")

    # Get metadata from reference data if available
    metadata = {}
    if reference_data and sura and aya:
        metadata = get_verse_metadata(reference_data, sura, aya)

    # Check if this is a sajdah verse
    sajdah_number = metadata.get("sajdah_number")
    sajdah_type = metadata.get("sajdah_type")

    # If sajdah_number exists but sajdah_type doesn't, set a default type
    if sajdah_number is not None and sajdah_type is None:
        sajdah_type = "obligatory"  # Default type, adjust as needed

    # Create the new format
    new_verse = {
        "id": int(aya) if aya and str(aya).isdigit() else None,
        "verse_number": int(aya) if aya and str(aya).isdigit() else None,
        "page_number": metadata.get("page_number", 1),
        "verse_key": f"{sura}:{aya}" if sura and aya else None,
        "juz_number": metadata.get("juz_number", 1),
        "hizb_number": metadata.get("hizb_number", 1),
        "rub_el_hizb_number": metadata.get("rub_el_hizb_number", 1),
        "sajdah_type": sajdah_type,
        "sajdah_number": sajdah_number,
        "text": verse_data.get("arabic_text", ""),
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
                        new_verse = transform_verse(verse_data, reference_data, surah_num)
                        verses.append(new_verse)

                    # Create the new index.json content
                    new_index_data = {"verses": verses}

                    # Write the new index.json
                    with open(index_file, 'w', encoding='utf-8') as f_out:
                        json.dump(new_index_data, f_out, ensure_ascii=False, indent=2)

                    # Also process individual verse files
                    for verse in verses:
                        verse_num = verse["verse_number"]
                        if verse_num:
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
                with open(verse_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                    # Check if the data has the old format
                    if "result" in data and isinstance(data["result"], dict):
                        verse_data = data["result"]
                        verse_num = os.path.splitext(os.path.basename(verse_file))[0]
                        new_verse = transform_verse(verse_data, reference_data, surah_num)

                        # Write the transformed verse
                        with open(verse_file, 'w', encoding='utf-8') as f_out:
                            json.dump(new_verse, f_out, ensure_ascii=False, indent=2)
            except json.JSONDecodeError:
                print(f"    Error: Could not parse {verse_file}")

def main():
    # Root directory containing all language folders
    root_dir = "."  # Change this to the actual root directory

    # Load reference data for metadata
    print("Loading reference data...")
    reference_data = load_reference_data()
    print(f"Reference data loaded for {len(reference_data)} surahs")

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
