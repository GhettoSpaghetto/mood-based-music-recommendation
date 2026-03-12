import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import numpy as np
from PIL import Image


class EmotionCNN(nn.Module):

    def __init__(self):
        super().__init__()

        # Conv Block 1
        self.conv1 = nn.Conv2d(1, 64, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(64)

        self.conv2 = nn.Conv2d(64, 64, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)

        # Conv Block 2
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)
        self.bn3 = nn.BatchNorm2d(128)

        self.conv4 = nn.Conv2d(128, 128, 3, padding=1)
        self.bn4 = nn.BatchNorm2d(128)

        # Conv Block 3
        self.conv5 = nn.Conv2d(128, 256, 3, padding=1)
        self.bn5 = nn.BatchNorm2d(256)

        self.conv6 = nn.Conv2d(256, 256, 3, padding=1)
        self.bn6 = nn.BatchNorm2d(256)

        # Classifier
        self.fc1 = nn.Linear(6*6*256, 256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 7)

        self.drop = nn.Dropout(0.25)

    def forward(self,x):

        x = F.leaky_relu(self.bn1(self.conv1(x)),0.1)
        x = F.leaky_relu(self.bn2(self.conv2(x)),0.1)
        x = F.max_pool2d(x,2)
        x = self.drop(x)

        x = F.leaky_relu(self.bn3(self.conv3(x)),0.1)
        x = F.leaky_relu(self.bn4(self.conv4(x)),0.1)
        x = F.max_pool2d(x,2)
        x = self.drop(x)

        x = F.leaky_relu(self.bn5(self.conv5(x)),0.1)
        x = F.leaky_relu(self.bn6(self.conv6(x)),0.1)
        x = F.max_pool2d(x,2)
        x = self.drop(x)

        x = torch.flatten(x,1)

        x = F.leaky_relu(self.fc1(x),0.1)
        x = self.drop(x)

        x = F.leaky_relu(self.fc2(x),0.1)
        x = self.drop(x)

        x = self.fc3(x)

        return x

class MoodModel:
    def __init__(self, model_path):

        self.model = EmotionCNN()

        state_dict = torch.load(model_path, map_location="cpu")
        self.model.load_state_dict(state_dict)

        self.model.eval()

        self.labels = ["angry","happy","sad","neutral","surprise"]

        self.transform = transforms.Compose([
            transforms.Grayscale(),
            transforms.Resize((48,48)),
            transforms.ToTensor(),
            transforms.Normalize([0.5], [0.5])
        ])

    def predict(self, image: Image.Image):
        img = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            output = self.model(img)
            pred = torch.argmax(output, 1).item()


        return self.labels[pred]