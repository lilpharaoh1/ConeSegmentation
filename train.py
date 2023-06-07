import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
#from CGNetPy import CGNet
from PIL import Image
import os
from glob import glob
import cv2
import os
import time
from ConeSegmentation.display_masks import display_pred_masks

from ConeSegmentation.models.CGNet.CGNetPyVitis import CGNet
model = CGNet()

image_dir = 'DanishTeam_Segmentation/DanishTeam_Segmentation/Training/imgs/'
mask_dir = 'DanishTeam_Segmentation/DanishTeam_Segmentation/Training/masks/'

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

def build_dataset(image_dir='DanishTeam_Segmentation/DanishTeam_Segmentation/Training/imgs/', \
                      mask_dir='DanishTeam_Segmentation/DanishTeam_Segmentation/Training/masks/'):
    
    dataset = CustomDataset(image_dir, mask_dir)
    
    tsplit = 0.15
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

# import wandb
# wandb.login()
# wandb.init(project="CGNet-Cones")

EPOCHS = 2
optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)
loss_func = nn.BCELoss()
print_every = 150
step = 0
test_losses, train_losses = [], []
checkpoint = True
train_loader, test_loader = build_dataset()

class CGNetEnd(nn.Module):
    def __init__(self):
        super(CGNetEnd, self).__init__()
        self.size = torch.Size([1088, 1456])
        
    def forward(self, x):
        out = F.interpolate(x, self.size, mode='bilinear', align_corners=True)
        out = torch.sigmoid(out)
        
        return out

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model#.to(device)
model_end = CGNetEnd()

for e in range(EPOCHS):
    running_loss = 0        
    for image, label in train_loader:
#         image, label = image.to(device), label.to(device)
        step += 1
        optimizer.zero_grad()
        output = model(torch.tensor(image))
        output = model_end(output)
        loss = loss_func(output, torch.tensor(label))
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        if step % print_every == 0:
            test_loss = 0
            accuracy = 0

            with torch.no_grad():
                model.eval()
                for image, label in test_loader:
                    output = model(torch.tensor(image))#.double())
                    output = model_end(output)
                    test_loss += loss_func(output, torch.tensor(label))
                model.train()

                for g in optimizer.param_groups:
                    g['lr'] *= 0.98

                train_losses.append(running_loss/len(train_loader))
                test_losses.append(test_loss/len(test_loader))

                if not isinstance(checkpoint, bool): # checkpoint exists
                    if test_losses[-1] > test_losses[-2]*1.3:
                        model.load_state_dict(checkpoint)
                    else:
                        checkpoint = model.state_dict()
                else:
                    checkpoint = model.state_dict()

                print("Epoch: {}/{}.. ".format(e+1, EPOCHS),
                      "Training Loss: {:.3f}.. ".format(running_loss / print_every),
                      "Test Loss: {:.3f}.. ".format(test_losses[-1])) 

                # wandb.log({
                #     'train_loss': running_loss / print_every,
                #     'test_loss': test_losses[-1]
                # })

                running_loss = 0

print("Done Training...")

if not os.path.isdir('weights'):
    os.mkdir('weights')
    
torch.save(model.state_dict(), 'weights/CGNetWeights_avmax')
# torch.save(model.state_dict(), 'weights_tuned/CGNetWeights_wrong_conv_4')

dataset = CustomDataset()
img, mask = dataset[0]

display_pred_masks(model, model_end, img, mask[0], output_name='train_output.png')