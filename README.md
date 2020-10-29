# Motion-U-Net
Detection of moving objects is a critical component of many computer vision tasks. Recently, deep learning architectures have been developed for supervised learning based moving object change detection. Some top performing architectures, like FgSegNet are single frame spatial appearance cue-based detection and tend to overfit to the training videos. We propose a novel compact multi-cue autoencoder deep architecture, Motion U-Net (MU-Net) for robust moving object detection that generalizes much better than FgSegNet and requires nearly 30 times fewer weight parameters. Motion and change cues are estimated using a multi-modal background subtraction module combined with flux tensor motion estimation. MU-Net was trained and evaluated on the CDnet-2014 change detection challenge video sequences and had an overall F-measure of 0.9369. We used the unseen SBI-2015 video dataset to assess generalization capacity where MU-Net had an F-measure of 0.7625 while FgSegNet v2 was 0.3519, less than half the MU-Net accuracy.

## MU-Net1: Single-stream Spatial-only Detection Using Semantic Segmentation
The proposed single-stream moving object detection network, MU-Net1, is based on a ResNet-18 [15] backbone, which enables deeper layers without degradation in network learning by using identity shortcut connections that skips one or more layers to facilitate deeper information propagation.

![](/figures/MU-Net1_Arch.png)

## MU-Net2: Single-stream Early Fusion for Spatio-temporal Change Detection (Three Channel)
The proposed MU-Net2 uses motion cues as input computed from multi-modal change detection and flux motion, through our fast tensor-based motion estimation and an adaptive multi-modal background subtraction model respectively. MU-Net2 incorporates three input channel processing streams, with the first channel being appearance (the three channel RGB color input is converted to gray-scale). Motion and change cues corresponding to the current frame computed using a temporal sliding window of frames for the case of flux motion and using a background model based on using past frames for the case of slower temporal change, are assigned to the second and third channels. Encoder part of the network extracts spatial appearance features from the first channel of the input, and spatio-temporal, change and motion based features are extracted from the second and third channels of the input.

![](/figures/MU-Net2_Arch.png)


