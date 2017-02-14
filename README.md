# Cisco-Spark-Experiments
Cisco Spark is a Team Collaboration software platform. This repository is a personal code playground for Cisco Spark. 


####Face Detection Using Raspberry-Pi
For the experiment  camera was interfaced with RaspberryPi and used Python's _pyCamera2_ package to capture images into framebuffer. 
Image is getting classified with help of _CascadeClassifier_ of OpenCV library.

If there is a change in number of faces detected from previous frame, then a notification is sent to user over Cisco Spark using Email.
