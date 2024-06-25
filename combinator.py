import argparse
import os
import glob
import time

def concatenate_files(folder, extension):
    # Ensure .out directory exists
    if not os.path.exists(".out"):
        os.makedirs(".out")
        print("Created .out folder")

    # Get the absolute path of the folder
    folder = os.path.abspath(folder)

    # Replace / and . in the folder name to avoid issues with the output filename
    folder_display = folder.replace("/", "_").replace(".", "_")

    output_filename = f".out/{folder_display}_concatenated.txt"

    try:
        with open(output_filename, 'w') as outfile:
            # Write a header with the folder and extension
            outfile.write(f"# Concatenated files with extension {extension} in folder {folder} at {time.ctime()}\n\n")

            file_count = 0
            for filepath in glob.iglob(f"{folder}/**/*{extension}", recursive=True):
                if os.path.getsize(filepath) > 0:  # Skip empty files
                    try:
                        with open(filepath, 'r') as infile:
                            outfile.write(infile.read())
                            outfile.write("\n")  # Optional newline between files
                            file_count += 1
                    except Exception as e:
                        print(f"Error reading file {filepath}: {e}")
                else:
                    print(f"Skipping empty file: {filepath}")

            print(f"Concatenation complete. {file_count} files were concatenated into {output_filename}")
    except Exception as e:
        print(f"Error writing to output file {output_filename}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Concatenate all files with a given extension in a directory recursively.")
    parser.add_argument('folder', type=str, help="Folder to search for files")
    parser.add_argument('extension', type=str, help="File extension to look for (e.g., .txt)")

    args = parser.parse_args()
    concatenate_files(args.folder, args.extension)

if __name__ == "__main__":
    main()
