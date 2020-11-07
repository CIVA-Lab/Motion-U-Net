# Train Motion U-Net models and Extract Masks for trained / pretrained model of Motion U-Net

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