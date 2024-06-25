# Combinator

`combinator.py` is a Python script that concatenates all files with a specified extension from within a directory (recursively) into a single output file. It adds a comment with the file name between each concatenated file and can optionally remove unnecessary whitespace from `.java` files.

## Features

- Recursively searches for files with a specified extension within a given directory.
- Concatenates the contents of these files into a single output file.
- Adds a comment with the file name between each concatenated file.
- Optionally removes unnecessary whitespace from `.java` files.
- Provides verbose output for detailed logging.

## Requirements

- Python 3.x

## Usage

### Basic Usage

To run the script, use the following command:

```sh
python3 combinator.py <folder> <extension>
```

- `<folder>`: The folder to search for files.
- `<extension>`: The file extension to look for (e.g., `.txt`, `.java`).

Example:

```sh
python3 combinator.py ../livechat/ ".java"
```

### Verbose Mode

To enable verbose output, use the `-v` or `--verbose` flag:

```sh
python3 combinator.py <folder> <extension> -v
```

Example:

```sh
python3 combinator.py ../livechat/ ".java" -v
```

## Output

The concatenated file will be created in the `.out` directory with a name based on the input folder and extension. The file will include:

- A header indicating the folder and extension.
- The contents of each file, separated by a comment with the file name.

## Script Details

### `remove_excessive_line_breaks(content)`

This function processes the content to remove unnecessary whitespace and excessive line breaks.

### `concatenate_files(folder, extension, verbose=False)`

This function handles the main logic of concatenating files:
- Ensures the `.out` directory exists.
- Generates an output file name based on the input folder.
- Writes a header to the output file.
- Recursively searches for files with the specified extension and concatenates their contents into the output file.
- Optionally removes excessive line breaks for `.java` files.
- Adds a comment with the file name between each concatenated file.
- Provides detailed logging if verbose mode is enabled.

## Example Output

If the script is run with the following command:

```sh
python3 combinator.py ../livechat/ ".java"
```

The output file will be named something like `.out/_home_user_livechat_concatenated.txt` and include:

```
# Concatenated files with extension .java in folder /home/user/livechat time: Wed Jun 30 14:15:22 2024

# Filename: Example1.java
<contents of Example1.java>

# Filename: Example2.java
<contents of Example2.java>
...
```

## License

This project is licensed under the MIT License.
