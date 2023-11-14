import streamlit as st
import os
import json
from PIL import Image

# Function to load images for a given lesson
def load_images_for_lesson(lesson_num):
    images = []
    folder_path = f'images/v{lesson_num:02}/'  # Updated to match your folder structure
    if os.path.exists(folder_path):
        for img_file in sorted(os.listdir(folder_path)):
            if img_file.endswith('.png'):
                image_path = os.path.join(folder_path, img_file)
                images.append(Image.open(image_path))
    return images

# Main Streamlit UI
def main():
    st.title('CFD Class Slides')

    # Tab-like menu for lesson selection
    lessons = ["01", "02", "03", "04", "05", "06", "07"]
    selected_lesson = st.selectbox("Select Lesson", lessons)

    # Load images for selected lesson
    images = load_images_for_lesson(selected_lesson)

    # Scroll buttons and display area
    if images:
        current_slide = st.sidebar.slider("Select Slide", 1, len(images), 1)
        
        # Display image and dummy description
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image(images[current_slide - 1], use_column_width=True)
        with col2:
            st.write("AI-generated description for the slide goes here...")

# Run the app
if __name__ == "__main__":
    main()
