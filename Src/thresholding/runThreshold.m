%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% Program Name: Run Threshold
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
%  Script runThreshold.m
%  Desc:  
%        Main script used to run threshold for the network output results
%        
%  Outputs: binary masks
%        
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% baseline
threshold('baseline/highway/', 1700);
threshold('baseline/office/', 2050);
threshold('baseline/pedestrians/', 1099);
threshold('baseline/PETS2006/', 1200);

% lowFramerate
threshold('lowFramerate/port_0_17fps/', 3000);
threshold('lowFramerate/tramCrossroad_1fps/', 900);
threshold('lowFramerate/tunnelExit_0_35fps/', 4000);
threshold('lowFramerate/turnpike_0_5fps/', 1500);

% cameraJitter
threshold('cameraJitter/badminton/', 1150);
threshold('cameraJitter/boulevard/', 2500);
threshold('cameraJitter/sidewalk/', 1200);
threshold('cameraJitter/traffic/', 1570);
 
% nightVideos
threshold('nightVideos/bridgeEntry/', 2500);
threshold('nightVideos/busyBoulvard/', 2760);
threshold('nightVideos/fluidHighway/', 1364);
threshold('nightVideos/tramStation/', 3000);
threshold('nightVideos/winterStreet/', 1785);
threshold('nightVideos/streetCornerAtNight/', 5200);
 
% badWeather
threshold('badWeather/skating/', 3900);
threshold('badWeather/wetSnow/', 3500);
threshold('badWeather/snowFall/', 6500);
threshold('badWeather/blizzard/', 7000);
 
% dynamicBackground
threshold('dynamicBackground/canoe/', 1189);
threshold('dynamicBackground/fall/', 4000);
threshold('dynamicBackground/fountain01/', 1184);
threshold('dynamicBackground/fountain02/', 1499);
threshold('dynamicBackground/overpass/', 3000);
threshold('dynamicBackground/boats/', 7999);
 
% intermittentObjectMotion
threshold('intermittentObjectMotion/abandonedBox/', 4500);
threshold('intermittentObjectMotion/parking/', 2500);
threshold('intermittentObjectMotion/sofa/', 2750);
threshold('intermittentObjectMotion/streetLight/', 3200);
threshold('intermittentObjectMotion/tramstop/', 3200);
threshold('intermittentObjectMotion/winterDriveway/', 2500);
 
% PTZ
threshold('PTZ/continuousPan/', 1700);
threshold('PTZ/intermittentPan/', 3500);
threshold('PTZ/twoPositionPTZCam/', 2300);
threshold('PTZ/zoomInZoomOut/', 1130);

% shadow
threshold('shadow/backdoor/', 2000);
threshold('shadow/bungalows/', 1700);
threshold('shadow/busStation/', 1250);
threshold('shadow/copyMachine/', 3400);
threshold('shadow/peopleInShade/', 1199);
threshold('shadow/cubicle/', 7400);
 
% thermal
threshold('thermal/diningRoom/', 3700);
threshold('thermal/library/', 4900);
threshold('thermal/park/', 600);
threshold('thermal/corridor/', 5400);
threshold('thermal/lakeSide/', 6500);
 
% turbulence
threshold('turbulence/turbulence0/', 5000);
threshold('turbulence/turbulence1/', 4000);
threshold('turbulence/turbulence2/', 4500);
threshold('turbulence/turbulence3/', 2200);
