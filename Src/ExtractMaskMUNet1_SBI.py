###########################################################################
#
#  Program Name: Extract Mask MU-Net1
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
#  Script ExtractMaskMUNet1_SBI.py
#  Desc:
#        Main script used to extract mask using trained model of MU-Net1
#
#  Inputs:
#       Put your inputs inside data/testData/ folder
#       change extensions accordingly while loading the paths 
#             
#  Outputs: masks
#        
###########################################################################


import torch
import torch.optim as optim

import numpy as np
import torchvision
import matplotlib.pyplot as plt
import glob
import os
import pandas as pd
import imageio
import torch.nn.functional as F
import time

from datetime import timedelta
from torchvision import models
from torchsummary import summary
from torch.optim import lr_scheduler

from pythonCodes.testDataLoader import MU_Net1_TestDataLoader
from pythonCodes.MUNet import MUNet

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

numClass = 1
model = MUNet(numClass).to(device)

# load trained model
model = torch.load('./models/MUNet1.pt')

# load pre-trained weights
# model.load_state_dict(torch.load('./weights/MU_Net1_Weights.pt'))

model.eval() 

# get video path from Flist.txt
fileName = 'FlistSBI.txt'
df = pd.read_csv(fileName, names=['filename'])
nameList = df['filename']

for videoPath in nameList:

    # start timer 
    startTime = time.time()

    print(videoPath)

    # path to the test image
    # change folder name and extension according to your test images
    folderTestData = sorted(glob.glob("./data/testData/SBI2015/dataset/" + videoPath + "*.jpg"))

    testDataset = MU_Net1_TestDataLoader(folderTestData)
    print(len(testDataset))

    testLoader = torch.utils.data.DataLoader(testDataset, batch_size=1, shuffle=False)

    # set mask path
    maskDir = os.path.join('./outputMaskMUNet1/SBI2015/', videoPath)
    # create path if not exist
    if not os.path.exists(maskDir):
            os.makedirs(maskDir)

    for i, inputs in enumerate(testLoader):
        
        inputs = inputs.to(device)
        
        # Predict
        pred = model(inputs)
        
        # The loss functions include the sigmoid function.
        pred = F.sigmoid(pred)	 
        pred = pred.data.cpu().numpy()
        
        outPred = pred[0].squeeze()
        outPredNorm = 255 * outPred
        outPredUint8 = outPredNorm.astype(np.uint8)

        # get frame name from original frame and replace in with bin and extension of jpg to png
        # change accordingly replace functions for your test inputs
        fname = os.path.basename(folderTestData[i]).replace('in','bin').replace('jpg','png')

        print(maskDir + fname)
        
        imageio.imwrite(maskDir + fname, outPredUint8)

    finalTime = time.time() - startTime
    msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(finalTime))
    print(msg)




