#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include "config.h"

Config::Config(string path)
{
    string str_line, str_param, str_temp;
    cout << "Path: "<< path.c_str() << endl;
    ifstream ifs(path.c_str());
    if ( !ifs.is_open() ) {
        cout << "ERROR: cannot open the configuration file!" << endl << "Using default setting instead." << endl;
        Config();
    }

    else{
        while(getline(ifs, str_line)) {
            istringstream iss(str_line);
            iss >> str_param >> str_temp;
            if ( iss.fail() || str_temp != "=" || str_param[0] == '#' ) { // skip the invalid parameters and comments in the config file
                continue;
            }
            if (str_param == "input_dir") iss >> input_dir;
            else if (str_param == "output_dir") iss >> output_dir;
            else if (str_param == "img_ext") iss >> img_ext;
        }
        ifs.close();
    }
}

Config::Config(){
    //main.cpp params
    //input_dir = "/Users/ganirahmon/AIP/HW7/input";
    //output_dir = "/Users/ganirahmon/Desktop/OutputBG";
    //img_ext = "png";
}
