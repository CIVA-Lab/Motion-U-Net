###########################################################################
#
#  Program Name: Motion U-Net Network Architecture
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
#  Script MUNet.py
#  Inputs:
#        For creating a MUNet1 or MUNet2 put number of classes the network
#        will give as an output result
#        Ex: For CDNet2014 and SBi2015 the number of classes = 1 (fg / bg)
#         
#  Outputs: Output of the network
#        
###########################################################################


import torch
import torch.nn as nn
import torchvision

from torchvision import models

# convolution + relu layers
def conv_relu(in_channels, out_channels, kernel, padding):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, kernel, padding=padding),
        nn.ReLU(inplace=True),
    )

# MU-Net network model
class MUNet(nn.Module):

    def __init__(self, n_out_class):
        super().__init__()
        
        # get pretrained resnet 18
        rnet_base_model = models.resnet18(pretrained=True)
        self.rnet_base_layers = list(rnet_base_model.children())                
        
        # ******************** Encoder part  **********************
        # Conv-1 (Resnet 18) 
        self.layer_1 = nn.Sequential(*self.rnet_base_layers[:3])
        # input size = (input.H/2, input.W/2)

        # Conv-2 (Resnet 18)
        self.layer_2 = nn.Sequential(*self.rnet_base_layers[3:5]) 
        # input size = (input.H/4, input.W/4)

        # Conv-3 (Resnet 18)
        self.layer_3 = self.rnet_base_layers[5]
        # input size = (input.H/8, input.W/8)

        # Conv-4 (Resnet 18)
        self.layer_4 = self.rnet_base_layers[6] 
        # input size = (input.H/16, input.W/16)

        # Conv-5 (Resnet 18)      
        self.layer_5 = self.rnet_base_layers[7]
        # input size = (input.H/32, input.W/32)

        # Convolve last encoder layer
        self.layer_5_conv = conv_relu(512, 512, 1, 0) 

        # *********************************************************
        
        # skip connection (sc) after each Resnet 18 conv layer
        self.layer_1_sc = conv_relu(64, 64, 1, 0) 
        self.layer_2_sc = conv_relu(64, 64, 1, 0) 
        self.layer_3_sc = conv_relu(128, 128, 1, 0) 
        self.layer_4_sc = conv_relu(256, 256, 1, 0) 
        
        # ******************** Decoder part  **********************
        # define upsampling
        self.up_sample = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        
        # define convolution after each upsample
        # input channels defined by previous upsample channels + skip connection channels
        self.conv_d_4 = conv_relu(256 + 512, 512, 3, 1)
        # input channels defined by previous upsample channels + skip connection channels
        self.conv_d_3 = conv_relu(128 + 512, 256, 3, 1)
        # input channels defined by previous upsample channels + skip connection channels
        self.conv_d_2 = conv_relu(64 + 256, 256, 3, 1)
        # input channels defined by previous upsample channels + skip connection channels
        self.conv_d_1 = conv_relu(64 + 256, 128, 3, 1)

        # **********************************************************
        
        # preserving original input size
        self.conv_input_size_1 = conv_relu(3, 64, 3, 1)
        self.conv_input_size_2 = conv_relu(64, 64, 3, 1)
        self.conv_input_size_3 = conv_relu(64 + 128, 64, 3, 1)
        
        # final convolution later
        self.conv_final = nn.Conv2d(64, n_out_class, 1)
        
    def forward(self, input):
        
        # encoder part
        layer_1 = self.layer_1(input)            
        layer_2 = self.layer_2(layer_1)
        layer_3 = self.layer_3(layer_2)
        layer_4 = self.layer_4(layer_3)        
        layer_5 = self.layer_5(layer_4)
        layer_5 = self.layer_5_conv(layer_5)

        # skip connections
        layer_4 = self.layer_4_sc(layer_4)
        layer_3 = self.layer_3_sc(layer_3)
        layer_2 = self.layer_2_sc(layer_2)
        layer_1 = self.layer_1_sc(layer_1)

        # decoder part
        d_out = self.up_sample(layer_5)
        d_out = torch.cat([d_out, layer_4], dim=1)
        d_out = self.conv_d_4(d_out)
 
        d_out = self.up_sample(d_out)
        d_out = torch.cat([d_out, layer_3], dim=1)
        d_out = self.conv_d_3(d_out)

        d_out = self.up_sample(d_out)
        d_out = torch.cat([d_out, layer_2], dim=1)
        d_out = self.conv_d_2(d_out)

        d_out = self.up_sample(d_out)
        d_out = torch.cat([d_out, layer_1], dim=1)
        d_out = self.conv_d_1(d_out)
        
         # convolve input for decoder part
        inp_org = self.conv_input_size_1(input)
        inp_org = self.conv_input_size_2(inp_org)

        d_out = self.up_sample(d_out)
        d_out = torch.cat([d_out, inp_org], dim=1)
        d_out = self.conv_input_size_3(d_out)        
        
        # final convolution later
        out = self.conv_final(d_out)        
        
        return out