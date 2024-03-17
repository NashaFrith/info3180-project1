import os

def get_uploaded_images():
    uploads_folder = os.path.join(os.getcwd(), 'uploads') 
    images = []
    for subdir, dirs, files in os.walk(uploads_folder):
        for file in files:
            images.append(file)
    return images