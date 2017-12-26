#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob, os
import random
import cv2
import numpy as np

imageFolder = "testimg/"  #待處理的相片資料夾路徑
areaSize = (24,24)   #要取得的圖片寸(w, h)
takePartNum = 3  #每張相片要隨機取幾張?
outputFolder = "output/"  #輸出的相片路徑

locW = 0
locH = 0
takeparts = 0

for filename in os.listdir(imageFolder):
    image = cv2.imread(imageFolder + filename)
    width = image.shape[1]
    height = image.shape[0]
    print("Process image: {}(size:{}x{}).....".format(filename,width,height))

    while takeparts<takePartNum:
        locH = random.randrange(height / areaSize[1])
        locW = random.randrange(width / areaSize[0])

        fromH = locH*areaSize[1]
        fromW = (locH+1)*areaSize[1]
        toH = locW*areaSize[0]
        toW = (locW+1)*areaSize[0]
        print("    take the area: ({}:{},{}:{})".format(fromH, fromW, toH, toW))

        area = image[ fromH:fromW, toH:toW ] 
        
        if not os.path.exists(outputFolder):
            os.mkdir(outputFolder)

        outputFile = outputFolder+"area_"+str(locW)+"_"+str(locH)+".jpg"
        cv2.imwrite(outputFile, area)
        #print("write to {}", outputFile)
        #cv2.imshow("AREA ({},{})".format(locW, locH), area)
        #cv2.waitKey(0)

        takeparts += 1

    takeparts = 0
