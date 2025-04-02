import os
import json

def merge_info_and_index():
    # Base directory
    surah_base_dir = '.'

    # Process all 114 surahs
    for surah_num in range(1, 115):
        surah_str = str(surah_num)
        surah_dir = os.path.join(surah_base_dir, surah_str)

        # Make sure the directory exists
        if not os.path.exists(surah_dir):
            print(f"Warning: Directory missing for surah {surah_num}")
            continue

        info_file = os.path.join(surah_dir, 'info.json')
        index_file = os.path.join(surah_dir, 'index.json')
        output_file = os.path.join(surah_dir, 'index.info.json')

        # Check if both files exist
        if not os.path.exists(info_file) or not os.path.exists(index_file):
            print(f"Warning: Missing files for surah {surah_num}")
            continue

        try:
            # Read info.json
            with open(info_file, 'r', encoding='utf-8') as f:
                info_data = json.load(f)

            # Read index.json
            with open(index_file, 'r', encoding='utf-8') as f:
                index_data = json.load(f)

            # Create the new merged structure
            merged_data = {
                # Info properties to keep
                "number": info_data.get("number"),
                "revelation_order": info_data.get("revelation_order"),
                "bismillah_pre": info_data.get("bismillah_pre"),
                "verses_count": info_data.get("verses_count"),
                "words_count": info_data.get("words_count"),
                "letters_count": info_data.get("letters_count"),
                "name_simple": info_data.get("name_simple"),
                "name_complex": info_data.get("name_complex"),
                "name_arabic": info_data.get("name_arabic"),
                "translated_name": info_data.get("translated_name"),
                "start_page": info_data.get("start_page"),
                "end_page": info_data.get("end_page"),

                # Nested objects from info
                "revelation_place": info_data.get("revelation_place"),
                "name": info_data.get("name"),

                # Process juz data - change verse_1 format to just 1
                "juz": []
            }

            # Process juz data
            for juz in index_data.get("juz", []):
                new_juz = {
                    "index": juz.get("index"),
                    "verse": {
                        "start": juz.get("verse", {}).get("start", "").replace("verse_", ""),
                        "end": juz.get("verse", {}).get("end", "").replace("verse_", "")
                    }
                }
                merged_data["juz"].append(new_juz)

            # Process verses - change from verse_1 format to just 1 as key
            verses = {}
            for key, value in index_data.get("verse", {}).items():
                new_key = key.replace("verse_", "")
                verses[new_key] = value

            merged_data["verses"] = verses

            # Write the merged data to the output file
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(merged_data, f, ensure_ascii=False, indent=2)

            print(f"Successfully merged files for surah {surah_num}")

        except Exception as e:
            print(f"Error processing surah {surah_num}: {e}")

if __name__ == "__main__":
    merge_info_and_index()
    print("Merging complete!")
