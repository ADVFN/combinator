import argparse
import os
import time
import fnmatch
import re

# List of common library folders to ignore
IGNORE_FOLDERS = {
    "node_modules",  # JavaScript/TypeScript
    "venv",          # Python virtual environment
    "__pycache__",   # Python bytecode cache
    "dist", "build", # Build folders
    ".git",          # Git repository data
    "target",        # Maven/Gradle Java build output
    ".idea",         # IntelliJ IDEA project data
    ".vscode",       # Visual Studio Code project data
    "env",           # Another common Python virtual environment name
    "Pods",          # CocoaPods folder for iOS projects
    "DerivedData",   # Xcode derived data,
    ".next",         # Next.js build output
    "bin", "obj"     # C#/C++ build output
}

# List of file extensions for which unnecessary whitespace should be removed
REMOVE_WHITESPACE_EXTENSIONS = {".java", ".ts", ".tsx", ".js", ".jsx", ".json", ".c", ".cpp", ".cs", ".go", ".php"}

def remove_excessive_whitespace(content):
    # Split the content into lines
    lines = content.splitlines()
    # Remove empty lines and strip leading/trailing whitespace, replace multiple spaces with single space
    cleaned_lines = [re.sub(r'\s+', ' ', line.strip()) for line in lines if line.strip()]
    # Join the cleaned lines with a single newline
    return " ".join(cleaned_lines)

def should_ignore_folder(folder_path):
    return any(ignore_folder in folder_path for ignore_folder in IGNORE_FOLDERS)

def concatenate_files(folder, patterns, verbose=False):
    # Ensure out directory exists
    if not os.path.exists("out"):
        os.makedirs("out")
        if verbose:
            print("Created out folder")

    # Get the absolute path of the folder
    folder = os.path.abspath(folder)

    # Replace / and . in the folder name to avoid issues with the output filename
    folder_display = folder.replace("/", "_").replace(".", "_")

    # Create an appropriate output filename based on the pattern
    output_filename = f"out/{folder_display}_concatenated_{patterns.replace('*', '-').replace('.', '_').replace(',', '_')}.txt"

    pattern_list = patterns.split(',')

    try:
        with open(output_filename, 'w') as outfile:
            # Write a header with the folder and patterns
            outfile.write(f"# Concatenated files with patterns {patterns} in folder {folder} time: {time.ctime()}\n\n")

            file_count = 0
            for root, dirs, files in os.walk(folder):
                # Remove ignored directories from the search
                dirs[:] = [d for d in dirs if not should_ignore_folder(os.path.join(root, d))]
                for filename in files:
                    if any(fnmatch.fnmatch(filename, pattern) for pattern in pattern_list):
                        if not filename.endswith(".tsx.snap"):  # Exclude .tsx.snap files
                            filepath = os.path.join(root, filename)
                            if os.path.getsize(filepath) > 0:  # Skip empty files
                                try:
                                    with open(filepath, 'r') as infile:
                                        content = infile.read()
                                        if any(filename.endswith(ext) for ext in REMOVE_WHITESPACE_EXTENSIONS):
                                            content = remove_excessive_whitespace(content)
                                        # Add comment with file name
                                        outfile.write(f"# Filename: {filename}\n")
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
    parser = argparse.ArgumentParser(description="Concatenate all files with given extension patterns in a directory recursively.")
    parser.add_argument('folder', type=str, help="Folder to search for files")
    parser.add_argument('patterns', type=str, help="Comma-separated list of file patterns to look for (e.g., *.txt,*.ts)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")

    args = parser.parse_args()
    concatenate_files(args.folder, args.patterns, args.verbose)

if __name__ == "__main__":
    main()
