import os
import glob

def rename_images(folder_path):
    # Get a list of all image files in the folder
    image_files = glob.glob(os.path.join(folder_path, '*.*'))
    image_files = [f for f in image_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # Sort files to ensure consistent ordering
    image_files.sort()

    for idx, image_file in enumerate(image_files):
        # Define new filename
        new_filename = f"image_{idx + 1}.jpg"
        new_filepath = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(image_file, new_filepath)
        print(f"Renamed {image_file} to {new_filepath}")

# Example usage:
folder_path = 'output'
rename_images(folder_path)
