from email.mime import base
from re import A
import torch
import torch.nn as nn
import torch.nn.functional as F 
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from ConeSegmentation.cone_dataset import build_dataset, CustomDataset
from ConeSegmentation.models.CGNet.CGNetPyVitis import CGNet, CGNetEnd
import time 

def infernece_test(model, model_end, dataset, num_tests=100, device=torch.device('cpu')):

    times1 = np.zeros([num_tests])
    times2 = np.zeros([num_tests])
    model.eval()
    model_end.eval()
    model.to(device)
    model_end.to(device)

    for idx, (image, mask) in enumerate(dataset):
        then = time.time()
        out = model(image.unsqueeze(0).to(device))
        dt1 = time.time() - then
        out = model_end(out)
        dt2 = time.time() - then

        times1[idx] = dt1
        times2[idx] = dt2

        if idx == num_tests - 1:
            break
    
    return np.mean(times1), np.mean(times2)


        # base_array = np.zeros_like(output.detach().numpy())
        # base_array[output > 0.5] = 1

dataset = CustomDataset()
img, mask = dataset[0]

model = CGNet().cpu()
model_end = CGNetEnd().cpu()

state_dict = torch.load('../weights/CGNet/CGNetWeights_conv_2')
model.load_state_dict(state_dict)

time1, time2 = infernece_test(model, model_end, dataset, num_tests=400)
print(time1, time2)
