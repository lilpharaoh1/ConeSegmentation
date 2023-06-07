from matplotlib.colors import get_named_colors_mapping
import torch
import torchvision
import os
from ConeSegmentation.models.CGNet.CGNetPyVitis import CGNet
from glob import glob
import cv2
import matplotlib.pyplot as plt


model = CGNet()

model.load_state_dict(torch.load('weights/CGNetWeights_wrong_conv_4'))

class CustomDataset(torch.utils.data.Dataset):
  def __init__(self, image_dir, mask_dir, mask_suffix='', transform=None):
    self.image_dir = image_dir
    self.mask_dir = mask_dir
    self.mask_suffix = mask_suffix

    if transform == None:
      self.transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
    else: 
      self.transform = transform
    self.ids = [os.path.splitext(file)[0] for file in os.listdir(image_dir)
                    if not file.startswith('.') and not '20210305' in file]

  def __getitem__(self, i):
    basename = self.ids[i]

    mask_file = glob(self.mask_dir + basename + self.mask_suffix + '.*')
    img_file = glob(self.image_dir + basename + '.*')

    mask = cv2.imread(mask_file[0])
    img = cv2.imread(img_file[0]) 

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
    img = self.transform(img)
    mask = self.transform(mask)
    base_array = torch.zeros_like(mask[0])
    base_array[mask[2] > 0.] = 1  
    base_array = base_array.reshape(1, base_array.shape[0], base_array.shape[1])

    return img, base_array

  def __len__(self):
    return len(self.ids)


image_dir = 'DanishTeam_Segmentation/DanishTeam_Segmentation/Training/imgs/'
mask_dir = 'DanishTeam_Segmentation/DanishTeam_Segmentation/Training/masks/'

dataset = CustomDataset(image_dir, mask_dir)

import torch.nn.functional as F
import numpy as np
import torch.nn as nn

class CGNetEnd(nn.Module):
    def __init__(self):
        super(CGNetEnd, self).__init__()
        self.size = torch.Size([1088, 1456])
        
    def forward(self, x):
        out = F.interpolate(x, self.size, mode='bilinear', align_corners=True)
        out = torch.sigmoid(out)

        return out
    
model_end = CGNetEnd()

def display_pred_masks(model, image, label):
    num_rows = 1

    num_columns = 3
    fig, axes = plt.subplots(num_rows, num_columns, figsize=(num_columns * 4, num_rows * 4))
    axes = axes.reshape(-1, num_columns)
    plt.tight_layout()
    
#     tensor_image = torch.tensor(image).double()
#     tensor_image = tensor_image.reshape(1, *tensor_image.shape)
#     output = model(tensor_image.double())
    
    image = torch.tensor(image).unsqueeze(0)
    output = model(image)
    output = model_end(output)
        
    axes[0, 0].imshow(image.squeeze().permute(1,2,0))
    axes[0, 0].set_xlabel("Image")
    axes[0, 0].axes.set_xticks([])
    axes[0, 0].axes.set_yticks([])
    axes[0, 1].imshow(label.squeeze())
    axes[0, 1].set_xlabel("Mask")
    axes[0, 1].axes.set_xticks([])
    axes[0, 1].axes.set_yticks([])
        
    base_array = np.zeros_like(output.detach().numpy())
    base_array[output > 0.5] = 1
    
    axes[0, 2].imshow(base_array.squeeze())
    axes[0, 2].set_xlabel("Pred Mask")
    axes[0, 2].axes.set_xticks([])
    axes[0, 2].axes.set_yticks([])

    plt.show()
    plt.savefig('output.png')

image, label = dataset[300]

display_pred_masks(model, image, label[0])


print("end of file")

