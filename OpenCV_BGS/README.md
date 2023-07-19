# Running OpenCV Background Subtraction (BGS):

**To get BGS results for use in Motion U-Net1 (MU-Net1) and Motion U-Net2 (MU-Net2)**

1. Change the input/output paths and image file format in ```config.txt``` file accordingly. 
```
# Config file to run OpenCV Background Subtraction

##### IO Parameters #####
# Input sequence path (give full path)
input_dir = /mnt/c/Users/ganir/OneDrive/Desktop/Projects/Motion-U-Net/Src/data/trainData/inputs

# Input image file format (e.g., jpg, png)
image_ext = jpg

# Ouput path (give full path)
output_dir =  /mnt/c/Users/ganir/OneDrive/Desktop/Projects/Motion-U-Net/Src/data/trainData/BGS/
``` 

2. Create a ```build``` folder:  
```
mkdir build
```

3. Enter the ```build``` folder:
```
cd build
```

4. Run ```cmake```:
```
cmake ..
```

5. Run ```make```:
```
make
```

6. Go to ```bin/linux``` folder:
```
cd ../bin/linux
```

7. Run ```BGSubOpenCV```:
```
./BGSubOpenCV
```

8. The output of BGS will be saved in the provided output path.