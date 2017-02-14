import io
import picamera
import cv2
import numpy

import json
import requests
import ntpath
from requests_toolbelt.multipart.encoder import MultipartEncoder

accesstoken="Bearer "+"<Token Here>"
image_filename = 'detected.jpg'
email_addr = 'xyz@maildomain.com'

def _url(path):
    return 'https://api.ciscospark.com/v1' + path

def sendImageonSpark(faceNum,imgName,sendTo):    
    filename ="/home/pi/"+imgName
    openfile = open(filename, 'rb')
    filename = ntpath.basename(filename)
    
    payload={}
    payload = {'files': (filename, openfile, 'image/jpg')}
    payload['toPersonEmail']=sendTo
    payload['text']=str(faceNum) +" Face(s) Detected!"
    #print ("payload"+str(payload))
    m = MultipartEncoder(fields=payload)
    headers = {'Authorization': accesstoken, 'Content-Type': m.content_type}
    
    resp = requests.post(url=_url('/messages'), data=m, headers=headers)
    message_dict = json.loads(resp.text)
    message_dict['statuscode'] = str(resp.status_code)
    return str(resp.status_code),message_dict['files']


while True:
    #Create a memory stream so photos doesn't need to be saved in a file
    stream = io.BytesIO()

    #Get the picture (low resolution, so it should be quite fast)
    #Here you can also specify other parameters (e.g.:rotate the image)
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture(stream, format='jpeg')

    #Convert the picture into a numpy array
    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

    #Now creates an OpenCV image
    image = cv2.imdecode(buff, 1)

    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

    #Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if (len(faces) > 0):
        print "Face detected!!!"
        #Draw a rectangle around every found face
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imwrite(image_filename, image)
        sendImageonSpark(len(faces), image_filename, email_addr)
    else:
        print "No face detected..."

#print "Found "+str(len(faces))+" face(s)"

#Draw a rectangle around every found face
#for (x,y,w,h) in faces:
#    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

#Save the result image
#cv2.imwrite('cam_result.jpg',image)
