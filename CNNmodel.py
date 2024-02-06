import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as nnf
import matplotlib.pyplot() as plt
import numpy as np
from torchvision import transforms as T

from PIL import Image
import cv2

#Create a Model Class that inherits nn.Module
class CNNmodel(nn.Module):
    #Input Layer (Color of the Game Piece, number of edges, and others) -> (Hidden Layers) -> Output Layers (Large game piece, small game piece, timer button, start light, fuel thruster, booster)
    def __init__(self, in_features= 5,h1 = 8, h2= 8,out_features=6):
        super().__init__()
        self.fc1 = nn.Linear(in_features, h1)
        self.fc2= nn.Linear(h1, h2)
        self.out= nn.Linear(h2, out_features)
        
    def forward(self, x):
        x = nnf.relu(self.fc1(x))
        x = nnf.relu(self.fc2(x))
        x = nnf.relu(self.out(x))
        
        return x
