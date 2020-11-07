# Resize and Threshold output masks of Motion U-Net

## Part 3 : Threshold

**To get binary masks of Motion U-Net1 (MU-Net1)**

1. Change ```orgImgFolder``` and ```maskFolder``` paths accordingly in ```threshold.m```. The example is given for CDNet 2014 dataset.

2. Change input image names and extension accordingly in ```threshold.m```

3. Change the folder path of video sequences and maximum number of frames in that sequence accordingly in ```runThreshold.m```. The example is given for CDNet 2014 dataset.

4. Run ```runThreshold.m```

This script will resize and threshold extracted masks to generate binary masks and save the binary masks inside ```thresholdMUNet1``` folder.  

**To get binary masks of Motion U-Net2 (MU-Net2)**

1. Change ```orgImgFolder``` and ```maskFolder``` paths accordingly in ```threshold.m```. The example is given for CDNet 2014 dataset.

2. Change ```thresholdFolder``` to ```../thresholdMUNet2/...``` and rest accordingly in ```threshold.m```

3. Change input image names and extension accordingly in ```threshold.m```

4. Change the folder path of video sequences and maximum number of frames in that sequence accordingly in ```runThreshold.m```. The example is given for CDNet 2014 dataset.

5. Run ```runThreshold.m```

This script will resize and threshold extracted masks to generate binary masks and save the binary masks inside ```thresholdMUNet2``` folder.  