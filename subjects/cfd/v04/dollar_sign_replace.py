import os
import re

def replace_parentheses_in_md_files():
    # Loop through all files in the current directory
    for filename in os.listdir("."):
        # Check if the file is a markdown file
        if filename.endswith(".md"):
            with open(filename, 'r') as file:
                content = file.read()

            # Replace \( and \) with $$
            modified_content = re.sub(r'\\\((.*?)\\)', r'$$ \1 $$', content)

            # Write the modified content back to the file
            with open(filename, 'w') as file:
                file.write(modified_content)

# Run the function
replace_parentheses_in_md_files()