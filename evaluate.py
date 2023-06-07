from distutils.command.build import build
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from cone_dataset import build_dataset

def evaluate(model, model_head=None, loss_fn=torch.nn.BCELoss(), e=1, test_split=0.98, eval=False):
    if eval:
        model.eval()
        model_head.eval()
    total = 0
    loss = 0

    train_loader, test_loader = build_dataset(test_split=test_split)
    device = torch.device('cpu')
    model.to(device)
    model_head.to(device)


    for epoch in range(e):
        print("evaluate: epoch " + str(epoch) + "...")
        for image, label in train_loader:
            image, label = image.to(device), label.to(device)
            out = model(image)
            out = model_head(out)
            l = loss_fn(out, label)
            loss += l.item()
            total += 1
            

    print("evaluation done...")

    loss /= total

    return loss

def evaluate_simplenet(model):
    device = torch.device('cpu')
    model.eval()
    model.to(device)

    for epoch in range(1):
        print('beginning simplenet evaluation...')
        for _ in range(300):
            out = model(torch.rand([1, 1, 28, 28]))

    print('simplenet evaluation done')

    return 0
