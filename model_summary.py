import torch
from torchsummary import summary
from models.CGNet.CGNetPyVitis import CGNet

model = CGNet().cpu()
summary(model, (3, 1088, 1456))

