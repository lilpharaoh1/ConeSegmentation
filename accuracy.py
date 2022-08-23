from email.mime import base
from re import A
import torch
import torch.nn as nn
import torch.nn.functional as F 
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from cone_dataset import build_dataset, CustomDataset
from ConeSegmentation.CGNetPy1 import CGNet, CGNetEnd

def make_binary(array):
    base_array = np.zeros_like(array)
    base_array[array > 0.5] = 1

    return base_array


def accuracy_test(model, model_end, dataset, num_tests=100, device=torch.device('cpu')):

    accuacy = np.zeros([num_tests])
    model.eval()
    model_end.eval()
    model.to(device)
    model_end.to(device)

    for idx, (image, mask) in enumerate(dataset):
        out = model(image.unsqueeze(0).to(device))
        out = model_end(out)

        out = make_binary(out[0].detach().numpy())
        mask = make_binary(mask.detach().numpy())

        intersection = np.logical_and(out[0], mask)
        union = np.logical_or(out[0], mask)

        # plt.imshow(np.transpose(mask, (1, 2, 0)))
        # plt.savefig('mask.png')
        # plt.imshow(np.transpose(out, (1, 2, 0)))
        # plt.savefig('image.png')
        # plt.imshow(np.transpose(intersection, (1, 2, 0)))
        # plt.savefig('intersection.png')
        # plt.imshow(np.transpose(union, (1, 2, 0)))
        # plt.savefig('union.png')

        iou = np.sum(intersection).item() / np.sum(union).item() if np.sum(union).item() > 0 else 1
        accuacy[idx] = iou

        if idx == num_tests - 1:
            break
    
    return np.mean(accuacy)


        # base_array = np.zeros_like(output.detach().numpy())
        # base_array[output > 0.5] = 1

dataset = CustomDataset()
img, mask = dataset[0]

model = CGNet().cpu()
model_end = CGNetEnd().cpu()

state_dict = torch.load('weights/CGNetWeights_conv_2')
model.load_state_dict(state_dict)

accuracy = accuracy_test(model, model_end, dataset, num_tests=400)
print(accuracy)
