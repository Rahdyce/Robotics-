import os
import shutil
import random

# Define paths to your dataset
source_images_dir = 'path/to/source/images'  # Folder containing your images
source_labels_dir = 'path/to/source/labels'  # Folder containing YOLO format labels (e.g., .txt files)
target_dir = 'path/to/target'  # Directory to store the training data

# Define the ratio of images to use for training (e.g., 80%)
train_ratio = 0.8

# Create directories for the YOLOv5 data structure
os.makedirs(os.path.join(target_dir, 'images/train'), exist_ok=True)
os.makedirs(os.path.join(target_dir, 'images/val'), exist_ok=True)
os.makedirs(os.path.join(target_dir, 'labels/train'), exist_ok=True)
os.makedirs(os.path.join(target_dir, 'labels/val'), exist_ok=True)

# Get a list of all image files
image_files = os.listdir(source_images_dir)

# Randomly shuffle the images
random.shuffle(image_files)

# Split images into training and validation sets
split_index = int(len(image_files) * train_ratio)
train_images = image_files[:split_index]
val_images = image_files[split_index:]

# Copy images to the YOLOv5 directories
for image in train_images:
    shutil.copy(os.path.join(source_images_dir, image), os.path.join(target_dir, 'images/train', image))
for image in val_images:
    shutil.copy(os.path.join(source_images_dir, image), os.path.join(target_dir, 'images/val', image))

# Copy label files to the YOLOv5 directories
for image in train_images:
    label_filename = os.path.splitext(image)[0] + '.txt'
    shutil.copy(os.path.join(source_labels_dir, label_filename), os.path.join(target_dir, 'labels/train', label_filename))
for image in val_images:
    label_filename = os.path.splitext(image)[0] + '.txt'
    shutil.copy(os.path.join(source_labels_dir, label_filename), os.path.join(target_dir, 'labels/val', label_filename))
