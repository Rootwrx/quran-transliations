import os
import json
import time
import requests

def fetch_and_save_chapter_info():
    # Base directory for storing the data
    surah_base_dir = '.'

    # Create the base directory if it doesn't exist
    if not os.path.exists(surah_base_dir):
        os.makedirs(surah_base_dir)

    # Process all 114 surahs
    for surah_num in range(1, 115):
        # Construct the API URL for the current surah
        api_url = f"https://api.quran.com/api/v4/chapters/{surah_num}/info"

        # Make sure the surah directory exists
        surah_dir = os.path.join(surah_base_dir, str(surah_num))
        if not os.path.exists(surah_dir):
            os.makedirs(surah_dir)

        output_file = os.path.join(surah_dir, 'about.en.json')

        try:
            # Fetch data from the API
            print(f"Fetching information for surah {surah_num}...")
            response = requests.get(api_url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                chapter_info = response.json()

                # Save the data to the output file
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(chapter_info, f, ensure_ascii=False, indent=2)

                print(f"Successfully saved information for surah {surah_num}")
            else:
                print(f"Error fetching surah {surah_num}: Status code {response.status_code}")

            # Add a small delay to avoid overwhelming the API
            time.sleep(1)

        except Exception as e:
            print(f"Error processing surah {surah_num}: {e}")

if __name__ == "__main__":
    fetch_and_save_chapter_info()
    print("Fetching complete!")
