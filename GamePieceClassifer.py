import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from torchvision.io import read_image
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.autograd import Variable
from PIL import Image
from sklearn.model_selection import train_test_split
import os

# Define the CNN model
class GamePieceClassifier(nn.Module):
    def __init__(self, num_classes):
        super(GamePieceClassifier, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(32 * 64 * 64, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 32 * 64 * 64)
        x = self.fc1(x)
        return x

# Define the dataset class
class GamePieceDataset(Dataset):
    def __init__(self, image_dir, label_csv, label_column='label', console_label='0', transform=None):
        self.image_dir = image_dir
        self.label_csv = label_csv
        self.label_column = label_column
        self.console_label = console_label
        self.transform = transform

        # Assuming labels are in a CSV file with columns: filename, label
        labels_df = pd.read_csv(label_csv)

        # Check if 'label' column is present, otherwise use the specified column as labels
        if label_column in labels_df.columns:
            self.labels = labels_df[label_column].astype(str).tolist()
        else:
            raise ValueError(f"Column '{label_column}' not found in the CSV file.")

        # Use the first column as filenames
        self.image_paths = [os.path.join(image_dir, img) for img, label in zip(labels_df.iloc[:, 0], self.labels) if str(label) == console_label]

        # Ensure the lengths match
        assert len(self.image_paths) > 0, f"No images found with label '{console_label}'. Make sure the label is present in the CSV file."

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]

        image = Image.open(img_path).convert('RGB')  # Open image as PIL Image and ensure it's in RGB format

        if self.transform:
            image = self.transform(image)

        # Assuming all labels are 0 (console)
        label = torch.tensor(0, dtype=torch.long)

        return image, label

# Set up the data loaders and transformations
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

# Ask user for the directories containing the images and labels
image_dir = input("Enter the directory path containing the images: ")
label_csv = input("Enter the path to the CSV file containing labels: ")


# Create a dataset and split it into training and testing sets
dataset = GamePieceDataset(image_dir=image_dir, label_csv=label_csv, label_column='console', console_label='0', transform=transform)

train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])

# Create data loaders for training and testing sets
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# Train the model
num_epochs = 10
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = Variable(images)
        labels = Variable(labels)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        if (i+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

# Test the model
model.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        images = Variable(images)
        labels = Variable(labels)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    print(f'Test Accuracy: {100 * correct / total}%')

