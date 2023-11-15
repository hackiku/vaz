#!/bin/bash

# Loop through all .md files in the current directory
for file in *.md
do
  # Check if the file exists
  if [ -f "$file" ]; then
    # Use sed to replace \( with $$ and \) with $$
    # Escape the parentheses and backslashes properly
    sed -i '' -e 's/\\( /$$ /g' -e 's/ \\)/ $$ /g' "$file"
  fi
done