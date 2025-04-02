import os
import json
import shutil

def copy_arabic_content_to_surah():
    # Base directories
    ar_base_dir = 'ar'
    surah_base_dir = 'surah'

    # Process all 114 surahs
    for surah_num in range(1, 115):
        surah_str = str(surah_num)

        ar_surah_dir = os.path.join(ar_base_dir, surah_str)
        surah_dir = os.path.join(surah_base_dir, surah_str)

        # Make sure both directories exist
        if not os.path.exists(ar_surah_dir) or not os.path.exists(surah_dir):
            print(f"Warning: Directory missing for surah {surah_num}")
            continue

        # Get all JSON files in the ar directory
        ar_files = [f for f in os.listdir(ar_surah_dir) if f.endswith('.json')]

        for ar_file in ar_files:
            ar_file_path = os.path.join(ar_surah_dir, ar_file)
            surah_file_path = os.path.join(surah_dir, ar_file)

            # Skip index.json to avoid overwriting the surah/*/index.json files
            if ar_file == 'index.json':
                continue

            # Copy individual verse files
            if ar_file != 'index.json':
                # If the file doesn't exist in the surah directory, copy it directly
                if not os.path.exists(surah_file_path):
                    shutil.copy2(ar_file_path, surah_file_path)
                    print(f"Copied {ar_file_path} to {surah_file_path}")
                else:
                    # If the file exists, merge the Arabic content with existing content
                    try:
                        # Read the Arabic content
                        with open(ar_file_path, 'r', encoding='utf-8') as f:
                            ar_data = json.load(f)

                        # Read the existing surah content
                        with open(surah_file_path, 'r', encoding='utf-8') as f:
                            surah_data = json.load(f)

                        # Update the surah data with Arabic content
                        # This assumes Arabic content should be added under a key like 'arabic'
                        # Adjust the following line according to your JSON structure
                        surah_data['arabic'] = ar_data  # or use specific fields from ar_data

                        # Write the updated content back to the surah file
                        with open(surah_file_path, 'w', encoding='utf-8') as f:
                            json.dump(surah_data, f, ensure_ascii=False, indent=2)

                        print(f"Merged Arabic content into {surah_file_path}")

                    except Exception as e:
                        print(f"Error processing {ar_file_path}: {e}")

if __name__ == "__main__":
    copy_arabic_content_to_surah()
    print("Content merging complete!")
