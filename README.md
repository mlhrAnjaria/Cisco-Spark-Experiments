# Cisco-Spark-Experiments
[Cisco Spark](https://developer.ciscospark.com/) is a Team Collaboration software platform. 
This repository is a personal code playground for Cisco Spark API and Spark Bots.


####Face Detection Using Raspberry-Pi
For the experiment  camera was interfaced with RaspberryPi and used Python's _pyCamera2_ package to capture images into framebuffer. 
Image is getting classified with help of _CascadeClassifier_ of _OpenCV_ library.

If there is a change in number of faces detected from previous frame, then a notification is sent to user over Cisco Spark using Email.

![Alt text](https://cloud.githubusercontent.com/assets/644483/22945008/b18248f8-f318-11e6-87bc-f70995efa2de.png "Detection Result")

####BookmarkBot
BookmarkBot allows a user to add and find personal bookmarks. 
This bot was developed using [Gupshup Platform](https://www.gupshup.io). 

Gupshup provides a good guide on how to start developing a bot and how to integrate it with Cisco Spark or any other channel.

**Usage**
@bookmarkbot /\<command> \<name> \<URL>
* /command - can be /add or /get
* name - any valid one word name that you can search late. 
* URL - A Valid URL.

Example,
@bookmarkbot /add SparkExperiments https://github.com/mlhrAnjaria/Cisco-Spark-Experiments
@bookmarbot /get SparkExperiments
