/*
 * cointroll.cpp
 *
 *  Created on: Nov 2, 2015
 *      Author: tiago
 * 	for malte
 *
 */
#include <ctime>
#include <raspicam/raspicam_cv.h>

#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <wiringPi.h>
#include <iostream>
#include <sstream>

using namespace cv;
using namespace std;

int back =0;
int coin =0;
int temp =0;
Mat bimg;
Mat cimg;
Mat background;
Mat NEWimage;
int frame = 1;
std::stringstream file;
string result;


int main(int argc, char** argv)
{
   wiringPiSetup();
    pinMode (0, OUTPUT);
    digitalWrite (0, HIGH); delay(500);
	cout << "throwing coin"<<endl;
	digitalWrite (0, LOW); 
	delay(500);
        digitalWrite (0, HIGH); 
	delay(600000);
}
  
