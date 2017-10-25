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

void detectAndDraw( Mat& img);

int main(int argc, char** argv)
{

    wiringPiSetup();
    pinMode (0, OUTPUT);
    digitalWrite (0, HIGH); delay(500);
    time_t timer_begin,timer_end;
    raspicam::RaspiCam_Cv Camera;
    cv::Mat image;
    int nCount=100;
    //set camera params
    Camera.set( CV_CAP_PROP_FORMAT, CV_8UC1 );
    //Open camera
    cout<<"Opening Camera..."<<endl;
    if (!Camera.open()) {cerr<<"Error opening the camera"<<endl;return -1;}
    //Start capture
    Camera.grab();
    Camera.retrieve (image);

    Mat img = image;

	if (back == 0){
		back= 1;			
		for (int u =0; u<200; u++){
			Camera.grab();
     			Camera.retrieve ( image);		
			delay(100);		
		}
		cv::imwrite("background.jpg",image);
		cout<<"saved background.jpg"<<endl;
	}

    return 0;
}


