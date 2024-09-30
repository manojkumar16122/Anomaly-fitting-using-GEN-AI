import os
import cv2
import numpy as np
import torch
from torchvision import transforms
from PIL import Image

def augment_images(source_folder, destination_folder, augmentations_per_image=30):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Define the augmentation pipeline
    transform = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.5),
        transforms.RandomRotation(degrees=45),
        transforms.RandomApply([transforms.GaussianBlur(3)], p=0.2),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.RandomResizedCrop(size=(256, 256), scale=(0.8, 1.2))
    ])

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            try:
                # Read the image
                image = Image.open(source_path)
                if image is None:
                    print(f"Could not read {filename}. Skipping.")
                    continue

                for i in range(augmentations_per_image):
                    augmented_image = transform(image)

                    base, ext = os.path.splitext(filename)
                    new_filename = f"{base}_aug_{i}.jpg"
                    destination_path = os.path.join(destination_folder, new_filename)
                    
                    # Save the augmented image
                    augmented_image.save(destination_path)
                    print(f"Saved augmented image {new_filename}.")
            except Exception as e:
                print(f"Failed to augment {filename}: {e}")

# Example usage:
source_folder = 'images'
destination_folder = 'output_img'
augment_images(source_folder, destination_folder)
