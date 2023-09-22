import torch
import torch.nn as nn
import torch.nn.functional as F


# Define model
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(32 * 32 * 3, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 10)
        self.act = nn.ReLU()

    def forward(self, x):
        x = x.reshape((x.shape[0], -1))
        x = self.act(self.fc1(x))
        x = self.act(self.fc2(x))
        x = self.fc3(x)
        return x
    
class CNN(nn.Module):
    def __init__(self, num_input_channels, num_output_classes):
        super(CNN, self).__init__()

        self.conv1 = nn.Conv2d(num_input_channels, 64, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(64,128,3,1,1)
        self.conv3 = nn.Conv2d(128,256,3,1,1)
        self.pool = nn.MaxPool2d(kernel_size=2,stride=2)
        self.fc = nn.Linear(4096, num_output_classes)

    def forward(self, inputs):
        x = F.relu(self.conv1(inputs))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = F.relu(self.conv3(x)) 
        x = self.pool(x)
        x = x.view(-1, 4096)
        x = self.fc(x)
        return x
