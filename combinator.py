import argparse
import os
import glob

def concatenate_files(folder, extension):

    if not os.path.exists(".out"):
        os.makedirs(".out")
        print("Created .out folder")

    # Get the absolute path of the folder
    folder = os.path.abspath(folder)

    # Replace / and . in the folder name to avoid issues with the output filename
    folder_display = folder.replace("/", "_").replace(".", "_")

    output_filename = f".out/{folder_display}_concatenated.txt"

    with open(output_filename, 'w') as outfile:
        # Write a header with the folder and extension
        outfile.write(f"# Concatenated files with extension {extension} in folder {folder} time: {os.ctime()}\n\n")

        for filepath in glob.iglob(f"{folder}/**/*{extension}", recursive=True):
            with open(filepath, 'r') as infile:
                outfile.write(infile.read())

def main():
    parser = argparse.ArgumentParser(description="Concatenate all files with a given extension in a directory recursively.")
    parser.add_argument('folder', type=str, help="Folder to search for files")
    parser.add_argument('extension', type=str, help="File extension to look for (e.g., .txt)")

    args = parser.parse_args()
    concatenate_files(args.folder, args.extension)

if __name__ == "__main__":
    main()
