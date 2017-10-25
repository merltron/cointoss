 #####################################
cmake_minimum_required (VERSION 2.8) 
project (coin)
find_package(raspicam REQUIRED)
find_package(OpenCV)
IF  ( OpenCV_FOUND AND raspicam_CV_FOUND)
MESSAGE(STATUS "COMPILING MALTES COIN")
add_executable (coin coin.cpp)  
target_link_libraries (coin ${raspicam_CV_LIBS})
ELSE()
MESSAGE(FATAL_ERROR "OPENCV NOT FOUND IN YOUR SYSTEM")
ENDIF()
#####################################