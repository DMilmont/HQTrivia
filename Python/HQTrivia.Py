#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:29:42 2018

@author: David
"""

try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract, os
from pytube import YouTube
import cv2
print(cv2.__version__)
#https://github.com/madmaze/pytesseract


videoDirectory = '/Users/David/HQVideos'

youtubeURLs = ['https://www.youtube.com/watch?v=T2fjU_wACn8','https://www.youtube.com/watch?v=e7lj0Tgo0bk']

#downloads youtube videos for later parsing - pass in array of youtube URLs
def ytDownload(youtubeURLs):
    for video in youtubeURLs:
        YouTube(video).streams.first().download(videoDirectory)
        print('Downloading: ',video)


#extract images from videos and place into folder
def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # takes a frame every 1 second
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      count = count + 1


#https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
#insturctions for image classification - this will be added on a new branch



#where the images are located to be parsed with OCR
directory = os.fsencode('/Users/David/HQVideos/.png')      

#loop through each classified image file in the directory and have tesseract do its OCR magic 
def parseImages(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            #This should eventually parse to a list 
            print(pytesseract.image_to_string(Image.open(filename)))
            continue


#Example of OCR to list - this should be changed to OCR specific coordinates
text = []
text.append(pytesseract.image_to_string(Image.open('C:/Users/Dave/Desktop/scene00023.png')))
print(pytesseract.image_to_string(Image.open('C:/Users/Dave/Desktop/scene00022.png')))
