import os
import glob
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

# Empty string to store the transcript
transcript = ""

# Get a sorted list of all folders in the current directory
folders = sorted_alphanumeric([d for d in os.listdir('.') if os.path.isdir(d)])

for folder in folders:
    # Get a sorted list of all .srt files in the folder
    files = sorted_alphanumeric(glob.glob(f'{folder}/*.srt'))
    
    for file in files:
        # Open the .srt file
        with open(file, 'r') as f:
            content = f.read()

            # Remove sequence numbers, timestamps, and blank lines
            content = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', content)
            content = re.sub(r'\n+', '\n', content)

            # Add the filename as a title and a divider after the content
            transcript += f"--- {file} ---\n{content}\n----------------------\n"

# Write the transcript to a file
with open('transcript.txt', 'w') as f:
    f.write(transcript)
