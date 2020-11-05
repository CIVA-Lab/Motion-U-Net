###########################################################################
#
#  Program Name: Train Data Loader
#                
#################################################################
#                
#  Author: Gani Rahmon & Kannappan Palaniappan
#  
#  Copyright(C)2020-2021. G. Rahmon, K. Palaniappan and      
#             Curators of the University of Missouri, a          
#             public corporation. All Rights Reserved.
#
#  Created by
#  Gani Rahmon & Kannappan Palaniappan
#  Department of Electrical Engineering and Computer Science,
#  University of Missouri-Columbia
#  For more information, contact:
#
#      Gani Rahmon
#      211 Naka Hall (EBW)  
#      University of Missouri-Columbia
#      Columbia, MO 65211
#      grzc7@mail.missouri.edu
# 
# or
#      Dr. K. Palaniappan
#      205 Naka Hall (EBW)
#      University of Missouri-Columbia
#      Columbia, MO 65211
#      palaniappank@missouri.edu
#
###########################################################################
#  
#  Script trainDataLoader.py
#  Inputs:
#        For MUNet1 put input (original frame) and label paths
#        For MUNet2 put inputs (original frame, bgSub, flux) and label paths 
#             
#  Outputs: Dataloader for training the network
#        
###########################################################################


import torch
import numpy as np
import torchvision.transforms as transforms

from torch.utils.data.dataset import Dataset
from skimage.transform import resize
from PIL import Image

# train data loader for MU-Net1
class MU_Net1_DataLoader(Dataset):
    def __init__(self, image_paths, target_paths):

        self.image_paths = image_paths
        self.target_paths = target_paths

        self.transforms = transforms.Compose([
            transforms.Resize((320,480)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) # imagenet
        ])

    def __getitem__(self, index):
        
        image = Image.open(self.image_paths[index])
        mask = Image.open(self.target_paths[index])

        x = self.transforms(image)
        y = np.array(mask)
        y = resize(y, (320, 480))
        y = torch.from_numpy(y).long()
        
        return x, y

    def __len__(self):

        return len(self.image_paths)


# train data loader for MU-Net2
class MU_Net2_DataLoader(Dataset):
    def __init__(self, image_paths, bgSub_paths, flux_paths, target_paths):

        self.image_paths = image_paths
        self.bgSub_paths = bgSub_paths
        self.flux_paths = flux_paths
        self.target_paths = target_paths

        self.transforms = transforms.Compose([
            transforms.Resize((320,480)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) # imagenet
        ])

    def __getitem__(self, index):
        
        # convert input frame to grayscale
        image = Image.open(self.image_paths[index]).convert('L')
        # bgSub mask
        bgSub = Image.open(self.bgSub_paths[index]).convert('L')
        # flux mask
        flux = Image.open(self.flux_paths[index]).convert('L')
        # label
        mask = Image.open(self.target_paths[index])

        newInputImg = Image.merge('RGB', (image, bgSub, flux))

        x = self.transforms(newInputImg)
        y = np.array(mask)
        y = resize(y, (320, 480))
        y = torch.from_numpy(y).long()
        
        return x, y

    def __len__(self):

        return len(self.image_paths)
