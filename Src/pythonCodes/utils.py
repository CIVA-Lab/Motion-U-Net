###########################################################################
#
#  Program Name: Utils
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
#  Script utils.py
#  Desc:
#       Functions used to calculate loss and print statistics
#                     
###########################################################################


import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F

# tversky loss
def tverskyLoss(pred, target, alpha = 0.3, beta = 0.7, smooth = 1.):
    pred = pred.contiguous()
    target = target.contiguous()
    
    TP = (pred * target).sum(dim=2).sum(dim=2)    
    FP = ((1-target) * pred).sum(dim=2).sum(dim=2)
    FN = (target * (1-pred)).sum(dim=2).sum(dim=2)
    
    loss = (TP + smooth) / (TP + alpha * FP + beta * FN + smooth)
    loss = 1 - loss
    
    return loss.mean() 

# calculate overall loss
def calcLoss(pred, target, stats, bceWeight=0.5):

    bce = F.binary_cross_entropy_with_logits(pred, target)

    pred = F.sigmoid(pred)
    tversky = tverskyLoss(pred, target)

    loss = bce * bceWeight + tversky * (1 - bceWeight)

    stats['bce'] += bce.data.cpu().numpy() * target.size(0)
    stats['tversky'] += tversky.data.cpu().numpy() * target.size(0)
    stats['loss'] += loss.data.cpu().numpy() * target.size(0)

    return loss

# print loss values
def printStats(stats, epochSamples, phase):
   
    outStats = []

    for i in stats.keys():
        outStats.append("{}: {:3f}".format(i, stats[i] / epochSamples))

    print("{}: {}".format(phase, ", ".join(outStats)))
