/*
 * cointroll.cpp
 *
 *  Created on: Nov 2, 2015
 *  Finished on: Nov 20, 2015
 *    Author: tiago romagnani silveira
 * 	for malte bartsch
 *    premiere at Berlin Masters - Gallery Arndt
 *
 *   Further ideas: saving pic/videos of people picking up the coin.
 *   
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
   // cv::imwrite("imag.jpg",image);

    Mat img = image;
    if(img.empty())
    {
        cout << "can not open " << endl;
        return -1;
    } else
    {
         cout << "In capture ..." << endl;

         for(;;)
         {
		if (back == 0){
		//  background saving done from ./bgroud
		//	back= 1;			
		//	for (int u =0; u<200; u++){
		//		Camera.grab();
             	//		Camera.retrieve ( image);		
		//		delay(100);		
		//	}
		//	cv::imwrite("background.jpg",image);	
		//	cout<<"loaded background"<<endl;
		// LOAD BACKGROUND
			background = imread("/home/pi/COIN/background.jpg", 0);		
		}
             Camera.grab();
             Camera.retrieve ( image);
		delay(200);
     	    imwrite("/home/pi/COIN/temp.jpg", image);
		delay(1000);
		image = imread("/home/pi/COIN/temp.jpg", 0);
		delay(200);
		cv::subtract(image, background, NEWimage);
	    imwrite("/home/pi/COIN/subtracted.jpg", NEWimage);
	    
            NEWimage = NEWimage(Rect(0,0,1193,960));
	    detectAndDraw( NEWimage);
             delay( 600 );
         }
    }

}



void throwcoin ()
{
        coin++;	
	cout << "throwing coin number"<< coin <<" and waiting 10s"<<endl;
	digitalWrite (0, LOW); 
	delay(500);
        digitalWrite (0, HIGH); 
	delay(10000);
}
  

void detectAndDraw( Mat& img)
{

    medianBlur(img, img, 3);
    //cvtColor(img, cimg, COLOR_GRAY2BGR);

    vector<Vec3f> circles;
    HoughCircles(img, circles, HOUGH_GRADIENT, 1, img.rows,
                 200, 10, 1, 10 // change the last two parameters
                                // (min_radius & max_radius) to detect larger circles
                 );
    size_t howmany = circles.size();

    cout << "found " << howmany << endl;
    cvtColor(img, cimg, COLOR_GRAY2BGR);
    for( size_t i = 0; i < circles.size(); i++ )
    {
        Vec3i c = circles[i];
        circle( cimg, Point(c[0], c[1]), c[2], Scalar(0,0,255), -1, LINE_AA);
        circle( cimg, Point(c[0], c[1]), c[2], Scalar(0,255,0), 1, LINE_AA);

    }

    	cv::imwrite("/home/pi/COIN/last.jpg", cimg);
	frame++;

    if (circles.size() > 0){
    	cout << "not throwing anything"<<endl;	
	temp = 0;
    } else {
        temp++;
	if (temp > 7) {
	      throwcoin();
	      temp= 0;
  	} else if (temp < 7){
         	cout << "trying many times (7) befor throw:"<<temp<<endl; 
		delay (10);
	}
     
    }

  // imshow("COINTROLL", cimg);

//    waitKey();

//    return 0;
}


