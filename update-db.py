import json
import os

# Load the existing db.json into a variable
db_path = 'db.json'
with open(db_path, 'r') as db_file:
    db = json.load(db_file)

# Function to update description paths and create .md files
def update_descriptions_and_create_md_files(subject):
    for lesson in db[subject]:
        for slide in lesson['slides']:
            # Construct the .md file path based on the image_path
            md_path = slide['image_path'].replace('.png', '.md')
            # Update the description to the .md file path
            slide['description'] = md_path
            # Create the .md file if it doesn't exist
            if not os.path.exists(md_path):
                os.makedirs(os.path.dirname(md_path), exist_ok=True)
                with open(md_path, 'w') as md_file:
                    md_file.write(f"# Slide {slide['slide_number']}\n\n")
                    md_file.write("Content for slide goes here.\n")

# Update descriptions and create .md files for 'proracunska aerodinamika'
update_descriptions_and_create_md_files('proracunska aerodinamika')

# Write the updated db back to db.json
with open(db_path, 'w') as db_file:
    json.dump(db, db_file, indent=4)
