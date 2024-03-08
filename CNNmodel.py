import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import pandas as pd
import os
from torch.nn import AdaptiveAvgPool2d
import torch.multiprocessing as mp

# Define transformation class
class ToTensorRGB(object):
    def __init__(self, target_size=(224, 224)):
        self.target_size = target_size

    def __call__(self, img):
        transform = transforms.Compose([
            transforms.Resize(self.target_size),
            transforms.ToTensor()
        ])
        return transform(img)

# Define CustomDataset class
class CustomDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.data_frame = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

        print("Before filtering:", len(self.data_frame))
        self.data_frame = self.data_frame[self.data_frame.apply(lambda row: os.path.exists(os.path.join(root_dir, row['img_name'])), axis=1)]
        print("After filtering:", len(self.data_frame))

    def __len__(self):
        return len(self.data_frame)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.data_frame.iloc[idx]['img_name'])
        image = Image.open(img_name).convert('RGB')

        # Dummy placeholders for other data, replace with your actual data logic
        edges = 0  # Placeholder
        color_range_min = 0  # Placeholder
        color_range_max = 0  # Placeholder
        label = self.data_frame.iloc[idx]['true_false']  # Assuming 'true_false' is a column in your CSV

        if self.transform:
            image = self.transform(image)

        return image, edges, color_range_min, color_range_max, label

# Define CNN model class
class RCNNModel(nn.Module):
    def __init__(self, num_classes=2):
        super(RCNNModel, self).__init__()
        # Use a pre-trained model for feature extraction
        self.base_model = models.resnet18(pretrained=True)
        # Remove the final fully connected layer
        self.base_features = nn.Sequential(*list(self.base_model.children())[:-1])
        # Add new classification head
        self.fc1 = nn.Linear(self.base_model.fc.in_features, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        # Extract features
        x = self.base_features(x)
        x = x.view(-1, self.base_model.fc.in_features)
        # Classify features
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def main():
    # Necessary for Windows. If you're using Linux, this is not needed but doesn't hurt to be here.
    mp.set_start_method('spawn', force=True)

    # Instantiate your dataset and dataloader
    transform = ToTensorRGB(target_size=(480, 640))
    dataset = CustomDataset(csv_file=r'C:\Users\david\OneDrive\Pictures\IEEE\GameLabels.csv',
                            root_dir=r'C:\Users\david\OneDrive\Pictures\IEEE', transform=transform)
    dataloader = DataLoader(dataset, batch_size=8, shuffle=True, num_workers=4)

    # Instantiate model, define loss function and optimizer
    model = CNNModel(num_classes=2)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    # Training loop
    num_epochs = 10
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for batch_idx, (images, _, _, _, labels) in enumerate(dataloader):
            # Your training code here. This is a placeholder loop.
            # You'll need to adjust it to your needs (e.g., send images/labels to device, reset gradients, etc.)
            pass

        print(f'Epoch {epoch+1}/{num_epochs} completed.')

    # Placeholder for saving model, adjust path as needed
    torch.save(model.state_dict(), r'C:\Users\david\OneDrive\Pictures\IEEE\CNNmodel.pth')
    print("Training complete.")

if __name__ == '__main__':
    main()

