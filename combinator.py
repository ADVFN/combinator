import argparse
import os
import glob
import time

def remove_excessive_line_breaks(content):
    # Split the content into lines
    lines = content.splitlines()
    # Remove empty lines and strip leading/trailing whitespace
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    # Join the cleaned lines with a single newline
    return "\n".join(cleaned_lines)

def concatenate_files(folder, extension, verbose=False):
    # Ensure .out directory exists
    if not os.path.exists(".out"):
        os.makedirs(".out")
        if verbose:
            print("Created .out folder")

    # Get the absolute path of the folder
    folder = os.path.abspath(folder)

    # Replace / and . in the folder name to avoid issues with the output filename
    folder_display = folder.replace("/", "_").replace(".", "_")

    output_filename = f".out/{folder_display}_concatenated.txt"

    try:
        with open(output_filename, 'w') as outfile:
            # Write a header with the folder and extension
            outfile.write(f"# Concatenated files with extension {extension} in folder {folder} time: {time.ctime()}\n\n")

            file_count = 0
            for filepath in glob.iglob(f"{folder}/**/*{extension}", recursive=True):
                if os.path.getsize(filepath) > 0:  # Skip empty files
                    try:
                        with open(filepath, 'r') as infile:
                            content = infile.read()
                            if extension == ".java":
                                content = remove_excessive_line_breaks(content)
                            # Add comment with file name
                            outfile.write(f"# Filename: {os.path.basename(filepath)}\n")
                            outfile.write(content)
                            outfile.write("\n")  # Add a newline between files
                            file_count += 1
                            if verbose:
                                print(f"Concatenated: {filepath}")
                    except Exception as e:
                        print(f"Error reading file {filepath}: {e}")
                else:
                    if verbose:
                        print(f"Skipping empty file: {filepath}")

            print(f"Concatenation complete. {file_count} files were concatenated into {output_filename}")
    except Exception as e:
        print(f"Error writing to output file {output_filename}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Concatenate all files with a given extension in a directory recursively.")
    parser.add_argument('folder', type=str, help="Folder to search for files")
    parser.add_argument('extension', type=str, help="File extension to look for (e.g., .txt)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")

    args = parser.parse_args()
    concatenate_files(args.folder, args.extension, args.verbose)

if __name__ == "__main__":
    main()
