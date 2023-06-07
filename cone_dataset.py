import torch
import numpy as np 
from glob import glob
import cv2
import torchvision
import os

class CustomDataset(torch.utils.data.Dataset):
  def __init__(self, image_dir='DanishTeam_Segmentation/DanishTeam_Segmentation/Training/imgs/', \
                    mask_dir='DanishTeam_Segmentation/DanishTeam_Segmentation/Training/masks/', \
                    mask_suffix='', transform=None):
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

def build_dataset(image_dir='DanishTeam_Segmentation/DanishTeam_Segmentation/Training/imgs/', \
                    mask_dir='DanishTeam_Segmentation/DanishTeam_Segmentation/Training/masks/', \
                    test_split=0.15):
    
    dataset = CustomDataset(image_dir, mask_dir)
    
    tsplit = test_split
    tsize = int(len(dataset)*tsplit)
    indices = torch.randperm(len(dataset)).tolist()

    train = torch.utils.data.Subset(dataset, indices[:-tsize])
    test = torch.utils.data.Subset(dataset, indices[-tsize:])

    train_loader = torch.utils.data.DataLoader(
      train,
      batch_size=1,
      shuffle=True,
      num_workers=0
    )

    test_loader = torch.utils.data.DataLoader(
        test,
        batch_size=1,
        shuffle=True,
        num_workers=0
    )
    
    return train_loader, test_loader
