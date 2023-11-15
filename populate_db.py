import os
import json

# Function to create lesson entries with .md file paths for descriptions
def create_lesson_entry(lesson_path, lesson_number, subject_title):
    slides = []
    # Get all files in the directory, sorted numerically
    slide_files = sorted(
        [f for f in os.listdir(lesson_path) if f.endswith('.png')],
        key=lambda x: int(x.split('_')[1].split('.')[0])
    )
    
    for slide_file in slide_files:
        slide_number = int(slide_file.split('_')[1].split('.')[0])
        slide_entry = {
            "slide_number": slide_number,
            "image_path": os.path.join(lesson_path, slide_file),
            "description": os.path.join(lesson_path, f"slide_{slide_number}.md")
        }
        slides.append(slide_entry)
        
        # Create corresponding .md files for each slide
        md_path = slide_entry["description"]
        if not os.path.exists(md_path):  # Check if the .md file doesn't exist
            with open(md_path, 'w') as md_file:
                md_file.write(f"# Slide {slide_number}\n\n")  # Write basic content
                md_file.write(f"Content for slide {slide_number}.\n")  # Placeholder text

    return {
        "lesson_number": lesson_number,
        "title": subject_title,
        "slides": slides
    }

# Main function to populate db.json
def populate_db():
    db = {"proracunska aerodinamika": []}  # Adjusted for the subject name

    # Path to the subjects directory
    subjects_dir = './subjects/'

    # For Proracunska Aerodinamika lessons
    subject_path = os.path.join(subjects_dir, 'cfd')
    for lesson_folder in sorted(os.listdir(subject_path)):
        lesson_path = os.path.join(subject_path, lesson_folder)
        if os.path.isdir(lesson_path):
            lesson_number = lesson_folder  # Assuming the folder name is the lesson number
            db["proracunska aerodinamika"].append(create_lesson_entry(lesson_path, lesson_number, "Fundamentals of Aerodynamics"))

    # Write to db.json
    with open('db.json', 'w') as db_file:
        json.dump(db, db_file, indent=4)

# Run the script to populate db.json
populate_db()
