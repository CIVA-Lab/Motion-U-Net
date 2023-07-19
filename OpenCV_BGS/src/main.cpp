#include "opencv2/imgproc.hpp"
#include "opencv2/videoio.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/video/background_segm.hpp"
#include "opencv2/core/utils/filesystem.hpp"
#include <stdio.h>
#include <string>
#include <iostream>
#include "config.h"
#include "filelisting_RP.h"

using namespace std;
using namespace cv;

string stringify(int x) {
  ostringstream temp;
  string ret;
  int z;
  temp << x;
  string st = temp.str();
  z = 6 - st.size();
  for (int i = 0; i < z; i++)
    ret += "0";
  ret += st;
  return ret;
}

int main(int argc, const char ** argv)
{

    cout << "OpenCV version : " << CV_VERSION << endl;

    //Add in parameter config path
    string config_path = "../../config.txt";
    Config config = Config(config_path);

    //==================Get the name list of all the images================
    string img_dir, img_ext, out_dir;
    if (argc != 4) {
        cout << "Loading the input images..." << endl;
        img_dir = config.input_dir;
        cout << "Input image extension check" << endl;
        img_ext = config.img_ext;
        cout << "Setting the output directory..." << endl;
        out_dir = config.output_dir;
    }
    else {
        img_dir = argv[1];
        img_ext = argv[2];
        out_dir = argv[3];
    }

    cout << "Img: "<< img_dir << endl;

    filenames f1;
    f1= file_listing(img_dir.data(), img_ext.data(), 1) ;

    Mat tmp_frame, bgmask, bgmask2, smothedImage, bgImage;

    // with negative learning rate (automatically chosen learning rate)
    Ptr<BackgroundSubtractorMOG2> bgsubtractor = createBackgroundSubtractorMOG2();
    bgsubtractor->setVarThreshold(16);
    //bgsubtractor->setDetectShadows(false);

    // custom learning rate (0.001)
    //Ptr<BackgroundSubtractorMOG2> bgsubtractor2 = createBackgroundSubtractorMOG2();
    //bgsubtractor2->setVarThreshold(16);

    // number of MOG
    //cout<< "MOG:"<<endl;
    //cout<<bgsubtractor->getNMixtures()<<endl;

    // history
    //cout<< "History:"<<endl;
    //cout<<bgsubtractor->getHistory()<<endl;

    cv::utils::fs::createDirectory(config.output_dir);

    int64 t0 = cv::getTickCount();

    //Start main loop
    for (int i=1; i<f1.used; i++) {

        // remove .DS_STORE before running the code (for MAC only)

        string img_name = f1.names[i];
        cv::Mat img = cv::imread(img_name); //Read images
        tmp_frame = img;

        cout<<"Img name: "<<img_name<<endl;

        // Apply the Gaussian Blur filter.
        // The Size object determines the size of the filter (the "range" of the blur)
        GaussianBlur(tmp_frame, smothedImage, Size(5, 5), 0, 0, BORDER_DEFAULT);

        bgsubtractor->apply(smothedImage, bgmask, -1);
        //bgsubtractor2->apply(tmp_frame, bgmask2, 0.001);
        bgsubtractor->getBackgroundImage(bgImage);

        // number of MOG
        //cout<< "MOG:"<<endl;
        //cout<<bgsubtractor->getNMixtures()<<endl;

        // **** if video frame starts with 1 make i+1
        // **** if video frame starts with 0 make i
        cv::imwrite(config.output_dir +"/bgs_" + stringify(i+1) +".png", bgmask);
        //cv::imwrite(config.output_dir +"/smooth_" + to_string(i) +".png", smothedImage);
        //cv::imwrite(config.output_dir +"/BGModel/bgm_" + stringify(i) +".png", bgImage);
        //cv::imwrite(config.output_dir +"/Alpha001/bgmask_" + to_string(i) +".png", bgmask2);
    }

    bgmask = cv::Scalar(0);

    //cv::imwrite(config.output_dir +"/BGS/bgs_" + stringify(0) +".png", bgmask);
    //cv::imwrite(config.output_dir +"/BGModel/bgm_" + stringify(0) +".png", bgmask);

    //cv::imwrite(config.output_dir +"/BGS/bgs_" + stringify(1) +".png", bgmask);
    //cv::imwrite(config.output_dir +"/BGModel/bgm_" + stringify(1) +".png", bgmask);


    int64 t1 = cv::getTickCount();
    double secs = (t1-t0)/cv::getTickFrequency();

    cout<<"Running time in secs: "<<secs<<endl;

    return 0;
}
