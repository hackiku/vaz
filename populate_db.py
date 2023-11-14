import os
import json

def create_lesson_entry(lesson_path, lesson_number, subject_title):
    slides = []
    slide_files = sorted(os.listdir(lesson_path), key=lambda x: int(x.split('_')[1].split('.')[0]))
    for slide in slide_files:
        if slide.endswith('.png'):
            slide_number = int(slide.split('_')[1].split('.')[0])
            slides.append({
                "slide_number": slide_number,
                "image_path": os.path.join(lesson_path, slide),
                "description": f"Description for Slide {slide_number}"
            })
    return {
        "lesson_number": lesson_number,
        "title": subject_title,
        "slides": slides
    }

def populate_db():
    db = {"cfd": [], "rocket_science": []}  # Initial structure

    # Path to the subjects directory
    subjects_dir = './subjects/'

    # For CFD lessons
    cfd_dir = os.path.join(subjects_dir, 'cfd/')
    for lesson in sorted(os.listdir(cfd_dir)):
        if os.path.isdir(os.path.join(cfd_dir, lesson)):
            db["cfd"].append(create_lesson_entry(os.path.join(cfd_dir, lesson), lesson, "Fundamentals of Aerodynamics"))

    # Add similar loops for other subjects like Rocket Science

    # Write to db.json
    with open('db.json', 'w') as db_file:
        json.dump(db, db_file, indent=4)

if __name__ == "__main__":
    populate_db()
