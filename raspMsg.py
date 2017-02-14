# -*- coding: utf-8 -*-
"""
#author manjaria
#date Feb 5, 2017
"""

import json
import requests
import ntpath
from requests_toolbelt.multipart.encoder import MultipartEncoder


accesstoken="Bearer "+"<Token Here>"

def _url(path):
    return 'https://api.ciscospark.com/v1' + path

def sendImageonSpark(faceNum,imgName,sendTo):    
    #filename ="/Users/manjaria/Pictures/"+imgName
    #openfile = open(filename, 'rb')
    #filename = ntpath.basename(filename)
    
    print('1')
    payload={}
    #payload = {'files': (filename, openfile, 'image/jpg')}
    payload['toPersonEmail']=sendTo
    payload['text']=faceNum +" Face(s) Detected!"
    #print ("payload"+str(payload))
    #m = MultipartEncoder(fields=payload)
    headers = {'Authorization': accesstoken, 'content-type': 'application/json'}
    
    resp = requests.post(url=_url('/messages'), data=payload, headers=headers)
    message_dict = json.loads(resp.text)
    message_dict['statuscode'] = str(resp.status_code)
    #return str(resp.status_code),message_dict['files']
    print(str(resp.status_code))
    return str(resp.status_code)

sendImageonSpark('1','screenshot.jpg','xyz@maildomain.com')
