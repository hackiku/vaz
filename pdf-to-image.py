from pdf2image import convert_from_path
import os

# Directory where your PDFs are stored
pdf_dir = 'slides/'
# Directory to save the images
image_dir = 'images/'

# Create the image directory if it doesn't exist
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Function to convert PDF to Images
def convert_pdf_to_images(pdf_path, output_folder):
    # Extract lesson number from the PDF filename
    lesson_num = os.path.basename(pdf_path).split('.')[0]

    # Create a specific folder for the lesson
    lesson_folder = os.path.join(output_folder, lesson_num)
    if not os.path.exists(lesson_folder):
        os.makedirs(lesson_folder)

    # Convert each page of the PDF to an image
    images = convert_from_path(pdf_path)

    # Save each page as an image
    for i, image in enumerate(images):
        image_filename = f"slide_{i+1}.png"
        image.save(os.path.join(lesson_folder, image_filename), 'PNG')

# Convert each PDF in the pdf directory
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith('.pdf'):
        convert_pdf_to_images(os.path.join(pdf_dir, pdf_file), image_dir)

print("Conversion completed!")
