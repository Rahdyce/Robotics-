import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import pandas as pd
import os

import torch.multiprocessing as mp
mp.set_start_method('spawn', force=True)

# Define transformations
class ToTensorRGB(object):
    def __init__(self, target_size=(480, 640)):
        self.target_size = target_size

    def __call__(self, sample):
        image, edges, color_range_min, color_range_max, label = \
            sample['image'], sample['edges'], sample['color_range_min'], sample['color_range_max'], sample['label']
        
        # Resize the image to the target size
        image = transforms.Resize(self.target_size)(image)
        
        # Apply your custom logic to convert RGB to tensor (assuming it's a 3-channel RGB image)
        image = transforms.ToTensor()(image)

        return {'image': image, 'edges': edges, 'color_range_min': color_range_min,
                'color_range_max': color_range_max, 'label': label}


class CustomDataset(Dataset):
    def __init__(self, csv_file= r'C:\Users\david\OneDrive\Pictures\IEEE\GameLabels.csv', root_dir= r'C:\Users\david\OneDrive\Pictures\IEEE', transform=None):
        self.data = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.data.iloc[idx, 1], self.data.iloc[idx, 0])
        image = Image.open(img_name).convert('RGB')
        edges = self.data.iloc[idx, 4]

        # Directly convert the values to a list
        color_range_min = [int(val) for val in self.data.iloc[idx, 5:9]]
        color_range_max = [int(val) for val in self.data.iloc[idx, 9:]]

        label = self.data.iloc[idx, -1]  # Use the last column 'true_false' as the label

        sample = {'image': image, 'edges': edges, 'color_range_min': color_range_min,
                  'color_range_max': color_range_max, 'label': label}

        if self.transform:
            sample = self.transform(sample)

        return sample


# Instantiate the dataset and dataloader
transform = transforms.Compose([ToTensorRGB(target_size=(480, 640))])
dataset = CustomDataset(csv_file=r'C:\Users\david\OneDrive\Pictures\IEEE\GameLabels.csv',
                        root_dir=r'C:\Users\david\OneDrive\Pictures\IEEE', transform=transform)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

# Define the CNN model
import torch.nn.functional as F

class CNNModel(nn.Module):
    def __init__(self, num_classes=2):  # Assuming 2 classes: true and false
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64 * 480 * 640 + 6, 256)  # Adjusted based on the corrected conv2
        self.fc2 = nn.Linear(256, num_classes)  # Adjusted for the correct number of output classes

    def forward(self, x, edges, color_range_min, color_range_max):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1, 64 * 480 * 640)  # Adjust the view size based on your architecture

        # Concatenate the RGB and edges features to the flattened output
        x = torch.cat([x, torch.Tensor(color_range_min), torch.Tensor(color_range_max), edges.unsqueeze(1)], dim=1)

        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Instantiate the CNN model
model = CNNModel(num_classes=2)  # Assuming 2 classes: true and false

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Example training loop
num_epochs = 10
for epoch in range(num_epochs):
    for batch in dataloader:
        inputs, edges, color_range_min, color_range_max, labels = \
            batch['image'], batch['edges'], batch['color_range_min'], batch['color_range_max'], batch['label']

        optimizer.zero_grad()
        outputs = model(inputs, edges, color_range_min, color_range_max)

        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')

# Save the trained model
torch.save(model.state_dict(), r'C:\Users\david\OneDrive\Pictures\IEEE\CNNmodel.pth')

# Add a statement to indicate when training is complete
print("Training is complete.")

