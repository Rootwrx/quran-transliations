import os
import json
import glob

def sort_verses_in_index_file(index_file_path):
    """
    Sort verses in an index.json file by verse number.
    """
    try:
        with open(index_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check if the file has the expected structure
        if "verses" in data and isinstance(data["verses"], list):
            # Sort verses by number
            data["verses"].sort(key=lambda v: v.get("number", 0) if v.get("number") is not None else 0)

            # Write the sorted data back to the file
            with open(index_file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"Sorted verses in {index_file_path}")
            return True
        else:
            print(f"Skipping {index_file_path}: No 'verses' list found")
            return False

    except json.JSONDecodeError:
        print(f"Error: Could not parse {index_file_path}")
        return False
    except Exception as e:
        print(f"Error processing {index_file_path}: {str(e)}")
        return False

def find_index_files_recursively(directory):
    """
    Recursively find all index.json files in the given directory.
    """
    index_files = []

    # Walk through all directories and files
    for root, dirs, files in os.walk(directory):
        # Check if this directory is named "surah" or is a numeric directory inside a "surah" directory
        is_surah_dir = os.path.basename(root) == "surah"
        parent_dir = os.path.dirname(root)
        is_numeric_in_surah = (os.path.basename(parent_dir) == "surah" and
                              os.path.basename(root).isdigit() and
                              1 <= int(os.path.basename(root)) <= 114)

        # If this is a surah directory or a numeric directory inside a surah directory
        if is_surah_dir or is_numeric_in_surah:
            # Look for index.json in this directory
            index_path = os.path.join(root, "index.json")
            if os.path.exists(index_path) and os.path.isfile(index_path):
                index_files.append(index_path)

    return index_files

def process_all_index_files(root_dir="."):
    """
    Find all index.json files recursively and sort their verses.
    """
    # Find all index.json files recursively
    index_files = find_index_files_recursively(root_dir)

    print(f"Found {len(index_files)} index.json files")

    # Process each index file
    total_files = len(index_files)
    sorted_files = 0

    for index_file in index_files:
        if sort_verses_in_index_file(index_file):
            sorted_files += 1

    print(f"\nSummary:")
    print(f"Total index.json files found: {total_files}")
    print(f"Successfully sorted: {sorted_files}")
    print(f"Failed: {total_files - sorted_files}")

if __name__ == "__main__":
    print("Quran Index.json Verse Sorter (Recursive)")
    print("----------------------------------------")
    print("This script will recursively find all index.json files")
    print("in surah directories and sort the verses by verse number.\n")

    # Get root directory from user or use current directory
    root_dir = input("Enter the root directory (press Enter for current directory): ").strip()
    if not root_dir:
        root_dir = "."

    if not os.path.exists(root_dir):
        print(f"Error: Directory '{root_dir}' does not exist.")
    else:
        process_all_index_files(root_dir)
