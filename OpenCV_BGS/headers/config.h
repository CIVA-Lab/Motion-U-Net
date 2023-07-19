#ifndef CONFIG_H
#define CONFIG_H

#include <string>
using namespace std;

class Config
{
public:
    Config();
    Config(string path);

    //main.cpp params
    string input_dir;
    string output_dir;
    string img_ext;
};
#endif
