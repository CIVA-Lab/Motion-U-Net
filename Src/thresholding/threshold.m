%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% Program Name: Threshold
%                
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                
%  Author: Gani Rahmon & Kannappan Palaniappan
%  Copyright(C)2020-2021. G. Rahmon, K. Palaniappan and      
%             Curators of the University of Missouri, a          
%             public corporation. All Rights Reserved.
%
%  Created by
%  Gani Rahmon & Kannappan Palaniappan
%  Department of Electrical Engineering and Computer Science,
%  University of Missouri-Columbia
%  For more information, contact:
%
%      Gani Rahmon
%      211 Naka Hall (EBW) 
%      University of Missouri-Columbia
%      Columbia, MO 65211
%      grzc7@mail.missouri.edu
% 
% or
%      Dr. K. Palaniappan
%      205 Naka Hall (EBW)
%      University of Missouri-Columbia
%      Columbia, MO 65211
%      palaniappank@missouri.edu
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%  Script threshold.m
%  Inputs:  
%        Put videoPath and endPoint of the video sequence
%        
%  Outputs: binary masks
%        
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function threshold(videoPath, endPoint)
    
    maskFolder='../outputMaskMUNet1/CD2014/';
    orgImgFolder='../data/testData/CD2014/dataset/';
    thresholdFolder = '../thresholdMUNet1/CD2014/';
    
    maskPath = strcat(maskFolder, videoPath);
    orgImgPath = strcat(orgImgFolder, videoPath,"input/");
    thresholdPath = strcat(thresholdFolder, videoPath);
    
    % create threshold folder
    if (0==isdir(thresholdPath))
        mkdir(thresholdPath);
    end
    
    videoPath
    
    for i = 1 : endPoint
         % filename formatting
         fileName = num2str(i, '%.6d');
         
         % read image
         mask = imread(fullfile(maskPath, ['bin', fileName, '.png']));
         
         % read orginal frame
         orgImg = imread(fullfile(orgImgPath, ['in', fileName, '.jpg']));
         
         % get size of original image
         iSize = size(orgImg);
                  
         % resize mask to original image size
         maskResize = imresize(mask, [iSize(1), iSize(2)], 'bilinear');
         
         % threshold to binary
         maskBinary = im2bw(maskResize, 0.0);
         maskBinary = im2uint8(maskBinary);

         fullfile(thresholdPath, ['bin', fileName, '.png'])
         
         % write resulting threshold one binary image to directory 
         imwrite(maskBinary, fullfile(thresholdPath, ['bin', fileName, '.png']));
    end
end
    
