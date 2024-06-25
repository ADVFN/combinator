# ADVFN Combinator

`combinator.py` is a Python script that concatenates all files with specified patterns from within a directory (recursively) into a single output file. It adds a comment with the file name between each concatenated file and can optionally remove unnecessary whitespace from specified file types.

## Features

- Recursively searches for files with specified patterns within a given directory.
- Concatenates the contents of these files into a single output file.
- Adds a comment with the file name between each concatenated file.
- Optionally removes unnecessary whitespace from specified file types.
- Provides verbose output for detailed logging.

## Requirements

- Python 3.x

## Usage

### Basic Usage

To run the script, use the following command:

```sh
python3 combinator.py <folder> <patterns>
```

- `<folder>`: The folder to search for files.
- `<patterns>`: A comma-separated list of file patterns to look for (e.g., `*.txt,*.ts`).

Example:

```sh
python3 combinator.py ../folder_name/ "*.ts,*.tsx"
```

This command will include both `.ts` and `.tsx` files while excluding `.tsx.snap` files.

### Verbose Mode

To enable verbose output, use the `-v` or `--verbose` flag:

```sh
python3 combinator.py <folder> <patterns> -v
```

Example:

```sh
python3 combinator.py ../folder_name/ "*.ts,*.tsx" -v
```

## Output

The concatenated file will be created in the `out` directory with a name based on the input folder and patterns. The file will include:

- A header indicating the folder and patterns.
- The contents of each file, separated by a comment with the file name.

## Script Details

### `remove_excessive_whitespace(content)`

This function processes the content to remove unnecessary whitespace and excessive line breaks.

### `concatenate_files(folder, patterns, verbose=False)`

This function handles the main logic of concatenating files:
- Ensures the `out` directory exists.
- Generates an output file name based on the input folder and patterns.
- Writes a header to the output file.
- Recursively searches for files matching the specified patterns and concatenates their contents into the output file.
- Optionally removes excessive whitespace for specified file extensions.
- Adds a comment with the file name between each concatenated file.
- Provides detailed logging if verbose mode is enabled.

## Example Output

If the script is run with the following command:

```sh
python3 combinator.py ../folder_name/ "*.ts,*.tsx"
```

The output file will be named something like `out/_home_user_folder_name_concatenated_ts_tsx.txt` and include:

```
# Concatenated files with patterns *.ts,*.tsx in folder /home/user/folder_name time: Wed Jun 30 14:15:22 2024

# Filename: Example1.ts
<contents of Example1.ts>

# Filename: Example2.tsx
<contents of Example2.tsx>
...
```

## License

This project is licensed under the MIT License.