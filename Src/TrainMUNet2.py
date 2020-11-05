###########################################################################
#
#  Program Name: Train Motion U-Net 2 (MU-Net2)
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
#  Script TrainMUNet2.py
#  Desc:
#        Main script used to train and save MU-Net2 model
#
#  Inputs:
#       Put your inputs, bgSub, flux and labels inside data/trainData/
#       change extensions accordingly while loading the paths 
#             
#  Outputs: Trained model of MU-Net2
#        
###########################################################################


import torch
import torch.optim as optim

import numpy as np
import torchvision
import matplotlib.pyplot as plt
import glob

from torchvision import models
from torchsummary import summary
from torch.optim import lr_scheduler

from pythonCodes.trainDataLoader import MU_Net2_DataLoader
from pythonCodes.MUNet import MUNet
from pythonCodes.trainModel import trainModel

# inputs and labels path
# put your input and label inside data folder
# change extensions accordingly 
folderData = sorted(glob.glob("./data/trainData/inputs/*.jpg"))
folderBgSub = sorted(glob.glob("./data/trainData/bgSub/*.png"))
folderFlux = sorted(glob.glob("./data/trainData/flux/*.png"))
folderMask = sorted(glob.glob("./data/trainData/labels/*.png"))

print(len(folderData))
print(len(folderBgSub))
print(len(folderFlux))
print(len(folderMask))

dataset = MU_Net2_DataLoader(folderData, folderBgSub, folderFlux, folderMask)
print(len(dataset))

# split into 90% for training and 10% for validation
lengths = [int(len(dataset)*0.9), int(len(dataset)*0.1)]
trainDataset, valDataset = torch.utils.data.random_split(dataset, lengths)
print(lengths)

# set batch size
batchSize = 8

trainLoader = torch.utils.data.DataLoader(trainDataset, batch_size=batchSize, shuffle=True)
valLoader = torch.utils.data.DataLoader(valDataset, batch_size=batchSize, shuffle=True)

dataLoaders = {
    'train': trainLoader,
    'val': valLoader
}

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

numClass = 1
model = MUNet(numClass).to(device)

# summarize the network
summary(model, input_size=(3, 320, 480))

# using Adam optimizer with learning rate 1e-4
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=1e-4)
# decrease learning rate by 0.1 after each 20th epoch
lrScheduler = lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.1)
# train model with 40 epoch
model = trainModel(dataLoaders, model, optimizer, lrScheduler, numEpochs=40)
# save trained model for later use
torch.save(model, './models/MUNet2.pt') 
