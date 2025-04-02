import json
import os

# Load the Quran data from the JSON file
def extract_surahs(input_file='index.json', output_dir='surah'):
    # Read the JSON data
    with open(input_file, 'r', encoding='utf-8') as file:
        surahs = json.load(file)

    # Create the main output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Process each surah
    for surah in surahs:
        surah_number = surah['number']

        # Create directory for the surah
        surah_dir = os.path.join(output_dir, str(surah_number))
        os.makedirs(surah_dir, exist_ok=True)

        # Create info.json file
        info_path = os.path.join(surah_dir, 'info.json')
        with open(info_path, 'w', encoding='utf-8') as file:
            json.dump(surah, file, ensure_ascii=False, indent=2)

        print(f"Saved {info_path}")

if __name__ == "__main__":
    # You can change the input file path if needed
    extract_surahs(input_file='index.json')
    print("Extraction complete!")
