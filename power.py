import torch
import torch.nn as nn
import torch.nn.functional as F 
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from cone_dataset import build_dataset, CustomDataset
from ConeSegmentation.CGNetPy1 import CGNet, CGNetEnd
import time 
import pynvml

def power_test(model, model_end, dataset, num_tests=100, device=torch.device('cuda')):

    torch.cuda.set_device(0)

    pynvml.Init()
    gpu = pynvml.nvmlDeviceGetHandleByIndex(0)
    name = pynvml.nvmlGetDeviceGetName(0)
    device = name.decode("utf-8")

    powers = np.zeros([num_tests])
    model.eval()
    model_end.eval()
    model.to(device)
    model_end.to(device)

    for idx, (image, mask) in enumerate(dataset):
        out = model(image.unsqueeze(0).to(device))
        out = model_end(out)
        power_usage = pynvml.nvmlDeviceGetPowerUsage(gpu) / 1000

        powers[idx] = power_usage

        if idx == num_tests - 1:
            break
    
    return np.mean(powers)


        # base_array = np.zeros_like(output.detach().numpy())
        # base_array[output > 0.5] = 1

dataset = CustomDataset()
img, mask = dataset[0]

# print(torch.cuda.is_available())

device = torch.device('cuda')

model = CGNet().to(device)
model_end = CGNetEnd().to(device)

state_dict = torch.load('weights/CGNetWeights_conv_2')
model.load_state_dict(state_dict)

power = power_test(model, model_end, dataset, num_tests=3)
print(power)
print(torch.cuda.is_available())
