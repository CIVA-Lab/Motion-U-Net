# Pre-trained weights of Motion U-Net

1. To use pre-trained weights of Motion U-Net, put the weights from the root **weights** folder here. 

2. To obtain masks from pre-trained weights of MU-Net1 on CD2014 dataset, open ```ExtractMaskMUNet1.py```

3. Uncomment  ```# model.load_state_dict(torch.load('./weights/MU_Net1_Weights.pt'))``` the following instuction.

4. Comment ```model = torch.load('./models/MUNet1.pt')``` the following instruction.

5. Run ```ExtractMaskMUNet1.py```
