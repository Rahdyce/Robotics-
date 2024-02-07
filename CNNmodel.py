import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as nnf
import matplotlib.pyplot() as plt
import numpy as np
from torchvision import transforms as T

from PIL import Image
import cv2

# Create a Model Class that inherits nn.Module
class CNNmodel(nn.Module):
    # Input Layer (Color of the Game Piece, number of edges, and others) -> (Hidden Layers) -> Output Layers (Large game piece, small game piece, timer button, start light, fuel thruster, booster)
    def __init__(self, in_features=2, h1=64, h2=32, out_features=6):
        super(CNNmodel, self).__init__()
        self.fc1 = nn.Linear(in_features, h1)
        self.fc2 = nn.Linear(h1, h2)
        self.out = nn.Linear(h2, out_features)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)

        return x

# Create an instance of the model
model = CNNmodel()

# Print the model architecture
print(model)
