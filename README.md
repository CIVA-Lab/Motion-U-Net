# Motion U-Net
The official implementation of the ICPR 2020 paper [**Motion U-Net: Multi-cue Encoder-Decoder Network for Motion Segmentation**](https://ieeexplore.ieee.org/document/9413211)

## News

**[July 18, 2023]** 

- :fire::fire::fire:  **Code for generating Background Subtraction (BGS) result using OpenCV library used in this work is available now !** 


## Motion U-Net: Multi-cue Encoder-Decoder Network for Motion Segmentation
Detection of moving objects is a critical component of many computer vision tasks. Recently, deep learning architectures have been developed for supervised learning based moving object change detection. Some top performing architectures, like FgSegNet are single frame spatial appearance cue-based detection and tend to overfit to the training videos. We propose a novel compact multi-cue autoencoder deep architecture, Motion U-Net (MU-Net) for robust moving object detection that generalizes much better than FgSegNet and requires nearly 30 times fewer weight parameters. Motion and change cues are estimated using a multi-modal background subtraction module combined with flux tensor motion estimation. MU-Net was trained and evaluated on the CDnet-2014 change detection challenge video sequences and had an overall F-measure of 0.9369. We used the unseen SBI-2015 video dataset to assess generalization capacity where MU-Net had an F-measure of 0.7625 while FgSegNet_v2 was 0.3519, less than half the MU-Net accuracy.

## MU-Net1: Single-stream Spatial-only Detection Using Semantic Segmentation
The proposed single-stream moving object detection network, MU-Net1, is based on a ResNet-18 [15] backbone, which enables deeper layers without degradation in network learning by using identity shortcut connections that skips one or more layers to facilitate deeper information propagation.

![](/figures/MU-Net1_Arch.png)

## MU-Net2: Single-stream Early Fusion for Spatio-temporal Change Detection (Three Channel)
The proposed MU-Net2 uses motion cues as input computed from multi-modal change detection and flux motion, through our fast tensor-based motion estimation and an adaptive multi-modal background subtraction model respectively. MU-Net2 incorporates three input channel processing streams, with the first channel being appearance (the three channel RGB color input is converted to gray-scale). Motion and change cues corresponding to the current frame computed using a temporal sliding window of frames for the case of flux motion and using a background model based on using past frames for the case of slower temporal change, are assigned to the second and third channels. Encoder part of the network extracts spatial appearance features from the first channel of the input, and spatio-temporal, change and motion based features are extracted from the second and third channels of the input.

![](/figures/MU-Net2_Arch.png)


# How to use Motion U-Net

**Src** folder contains all scripts used to train models, extract masks from trained models, and threshold the output results to get binary masks.

**weights** folder contains pre-trained weights of the Motion U-Net, if you want to use pre-trained weights, put them inside **Src/weights/** folder.

There are three parts for this software in ```Src``` folder, you can skip Part 1 (Train Models) if you are planning to use pre-trained models.

**Part 1 -->** Train Models: train both MU-Net models from scratch.

**Part 2 -->** Extract Masks: use trained/pre-trained models to extract masks.

**Part 3 -->** Threshold: use thresholding to convert output masks to binary masks.

In every parts, there are readme file that describes the needed steps. The description is also placed here.

**You need to use PyTorch to do Part 1 and Part2.**

**You need to use MATLAB to do Part 3.**

## Part 1 : Train Models

**To train Motion U-Net1 (MU-Net1)**

1. Put your input images used to train the network in a folder called ```inputs```, inside ```data/trainData/``` folder. Initial 50 images are given as an example. 

2. Put your label images used to train the network in a folder called ```labels```, inside ```data/trainData/``` folder. Initial 50 images are given as an example. **Label images need to be binary mask, where background is equal to 0 and foreground is equal to 1**.

3. Change input and label paths and extensions accordingly in ```TrainMUNet1.py```

4. Run ```TrainMUNet1.py```

This script will train MU-Net1 model according to the inputs and labels you provided and save trained model inside ```models``` folder.

**To train Motion U-Net2 (MU-Net2)**

1. Put your input images used to train the network in a folder called ```inputs```, inside ```data/trainData/``` folder. Initial 50 images are given as an example. 

2. Put your Background Subtraction masks used to train the network in a folder called ```bgSub```, inside ```data/trainData/``` folder. Initial 50 images are given as an example. 

3. Put your Flux masks used to train the network in a folder called ```flux```, inside ```data/trainData/``` folder. Initial 50 images are given as an example. 

4. Put your label images used to train the network in a folder called ```labels```, inside ```data/trainData/``` folder. Initial 50 images are given as an example. **Label images needs to be binary mask, where background is equal to 0 and foreground is equal to 1**.

3. Change inputs and label paths and extensions accordingly in ```TrainMUNet2.py```

4. Run ```TrainMUNet2.py```

This script will train MU-Net2 model according to the inputs and labels you provided and save trained model inside ```models``` folder.

## Part 2 : Extract Masks

**To extract masks of Motion U-Net1 (MU-Net1)**

1. To extract masks using trained / pre-trained model of MU-Net1 create a new folder with dataset name inside ```data/testData/``` folder and and put your images inside created folder. Initial 250 images are given as an example, which is taken from CDNet 2014 dataset.

2. Change dataset paths and extensions accordingly in ```ExtractMaskMUNet1.py```

3. Change video sequence paths accordingly in ```Flist.txt```. Some examples of video sequence taken from CDNet 2014 are given inside  ```Flist.txt```

4. Run ```ExtractMaskMUNet1.py```

This script will extract masks using trained / pre-trained model of MU-Net1 for the given dataset and save the result of output masks inside ```outputMaskMUNet1``` folder.

**To extract masks of Motion U-Net2 (MU-Net2)**

1. To extract masks using trained / pre-trained model of MU-Net2:

* * create a new folder with dataset name inside ```data/testData/``` folder and and put your images inside created folder. Initial 250 images are given as an example, which is taken from CDNet 2014 dataset

* * create another folder inside ```data/testData/``` folder and put Background Subtraction masks related to the input images. Initial 250 background subtraction masks are given as an example, which is obtained using OpenCV library **BackgroundSubtractorMOG2** on an input images. 

* * create another folder inside ```data/testData/``` folder and put Flux masks related to the input images. Initial 250 flux masks are given as an example, which is obtained using **trace of the flux tensor** on an input images.

* * For more detail how to obtain Background Subtaction and Flux masks read the paper.  

2. Change dataset paths and extensions accordingly in ```ExtractMaskMUNet2.py```

3. Change video sequence paths accordingly in ```Flist.txt```. Some examples of video sequence taken from CDNet 2014 are given inside  ```Flist.txt```

4. Run ```ExtractMaskMUNet2.py```

This script will extract masks using trained / pre-trained model of MU-Net2 for the given dataset with related background subtraction and flux masks and save the result of output masks inside ```outputMaskMUNet2``` folder.

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

## Running OpenCV Background Subtraction (BGS):

**To get BGS results for use in Motion U-Net1 (MU-Net1) and Motion U-Net2 (MU-Net2)**

1. Go to ```OpenCV_BGS``` folder.
```
cd OpenCV_BGS
```

2. Change the input/output paths and image file format in ```config.txt``` file accordingly.  

3. Create a ```build``` folder:  
```
mkdir build
```

4. Enter the ```build``` folder:
```
cd build
```

5. Run ```cmake```:
```
cmake ..
```

6. Run ```make```:
```
make
```

7. Go to ```bin/linux``` folder:
```
cd ../bin/linux
```

8. Run ```BGSubOpenCV```:
```
./BGSubOpenCV
```

## Project Collaborators and Contact

**Author:** Gani Rahmon, Filiz Bunyak and Kannappan Palaniappan

Copyright &copy; 2020-2021. Gani Rahmon and Prof. K. Palaniappan and Curators of the University of Missouri, a public corporation. All Rights Reserved.

**Created by:** Ph.D. student: Gani Rahmon  
Department of Electrical Engineering and Computer Science,  
University of Missouri-Columbia  

For more information, contact:

* **Gani Rahmon**  
226 Naka Hall (EBW)  
University of Missouri-Columbia  
Columbia, MO 65211  
grzc7@mail.missouri.edu  

* **Dr. F. Bunyak**  
219 Naka Hall (EBW)  
University of Missouri-Columbia  
Columbia, MO 65211  
bunyak@missouri.edu

* **Dr. K. Palaniappan**  
205 Naka Hall (EBW)  
University of Missouri-Columbia  
Columbia, MO 65211  
palaniappank@missouri.edu

## ✏️ Citation

If you think this project is helpful, please feel free to leave a star⭐️ and cite our paper:

```
@inproceedings{gani2021MUNet,
  title={Motion U-Net: Multi-cue Encoder-Decoder Network for Motion Segmentation}, 
  author={Rahmon, Gani and Bunyak, Filiz and Seetharaman, Guna and Palaniappan, Kannappan},
  booktitle={2020 25th International Conference on Pattern Recognition (ICPR)}, 
  pages={8125-8132},
  year={2021}
}
```