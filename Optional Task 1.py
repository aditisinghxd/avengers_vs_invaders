#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os

def read_file_with_encoding(file_path):
    encodings = ['utf-8', 'latin-1', 'cp1252']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Cannot decode file: {file_path}")

def combine_markdown_files(directories, output_file):
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through the list of directories
        for directory in directories:
            try:
                # List all files in the current directory
                files = os.listdir(directory)
                # Filter out files that do not end with .md
                markdown_files = [f for f in files if f.endswith('.md')]
                
                # Iterate through the list of markdown files
                for md_file in markdown_files:
                    # Create the full path to the markdown file
                    full_path = os.path.join(directory, md_file)
                    try:
                        # Read the file content with appropriate encoding
                        content = read_file_with_encoding(full_path)
                        # Write the directory name as a header (optional)
                        outfile.write(f'# Directory: {directory}\n')
                        outfile.write(f'# File: {md_file}\n\n')
                        # Write the content to the output file
                        outfile.write(content)
                        # Add a newline to separate contents of different files
                        outfile.write('\n\n')
                    except UnicodeDecodeError as e:
                        print(f"Could not decode file {full_path}: {e}")
            except Exception as e:
                print(f"An error occurred with directory {directory}: {e}")

# Specify the directories containing the markdown files
directories = [
    "C:/Users/DELL/Documents/Jupyter File/Markdown files/data files",
    "C:/Users/DELL/Documents/Jupyter File/Markdown files/Task 1",
    "C:/Users/DELL/Documents/Jupyter File/Markdown files/Task 2"
]

# Specify the output file path
output_file = 'combined_output.md'

# Combine the markdown files from the specified directories
combine_markdown_files(directories, output_file)

print(f"Markdown files combined into {output_file}")


# In[ ]:





# In[ ]:




