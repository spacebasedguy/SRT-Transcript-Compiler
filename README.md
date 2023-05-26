# SRT Transcript Compiler

The SRT Transcript Compiler is a Python script designed to extract and compile the text content from multiple .srt (subtitle) files located in several directories. This can be extremely useful, for instance, if you've downloaded a course or series with multiple .srt subtitle files across various folders, and you want to compile one comprehensive transcript document from start to end.

## Benefits

This script aids in generating a unified transcript document for a collection of .srt files spread across different folders, which can be a course, lecture series, multi-part documentary, or any multi-part video content. Having one consolidated transcript can aid in better comprehension, quick reference, revision, or even for accessibility reasons.

## Features

- Processes multiple .srt files across numerous directories.
- Removes timestamps and sequence numbers for clean text output.
- Appends a divider and the name of the file between each transcript for better differentiation.
- Orders the processed files and directories numerically for a logical, easy-to-follow transcript.

## Usage

1. Place the script (`srt_transcript_compiler.py`) in the parent directory containing the directories of .srt files.
2. Run the script using Python3:
3. The compiled transcript will be outputted in the same directory as `transcript.txt`.

## Requirements

- Python 3
- The directories containing .srt files should be in the same directory as the script.
- SRT files should follow the standard format.

## Limitations

The script assumes that the .srt files follow the standard subtitle format. If they include other formatting tags, those will be included in the output as well. For a more sophisticated parsing, consider using a dedicated subtitle parsing library like `pysrt`.
