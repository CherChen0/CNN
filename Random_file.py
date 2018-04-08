# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:14:40 2017

@author: cher
"""

import random
from PIL import Image as image

 
index = [0]*100
for i in range(100):
    index[i] = i


cwd='E:/Anaconda_3/examples/Working/Tensorflow_practice/Images/'
train_cwd='E:/Anaconda_3/examples/Working/Tensorflow_practice/Train_Images/'
test_cwd='E:/Anaconda_3/examples/Working/Tensorflow_practice/Test_Images/'
validation_cwd='E:/Anaconda_3/examples/Working/Tensorflow_practice/Validation_Images/'

classes={'agricultural','airplane','baseballdiamond','beach','buildings','chaparral',
'denseresidential','forest','freeway','golfcourse','harbor','intersection','mediumresidential',
'mobilehomepark','overpass','parkinglot','river','runway','sparseresidential','storagetanks',
'tenniscourt'} 

#目标图片大小
dst_w = 227
dst_h = 227
#保存的图片质量
save_q = 75

for name in classes:
    random.shuffle(index)
    for i in range(0,70):
        string = str(index[i])
        if index[i]>9:
            ori_img = cwd + name + '/' + name + string + '.tif'
            dst_img = train_cwd + name + '/' + name + string + '.tif'
        else:
            ori_img = cwd + name + '/' + name + '0' + string + '.tif'
            dst_img = train_cwd + name + '/' + name + '0' + string + '.tif'
        im = image.open(ori_img)
        im.resize((dst_w,dst_h),image.ANTIALIAS).save(dst_img,quality=save_q)
            
    for i in range(70,80):
        string = str(index[i])
        if index[i]>9:
            ori_img = cwd + name + '/' + name + string + '.tif'
            dst_img = validation_cwd + name + '/' + name + string + '.tif'
        else:
            ori_img = cwd + name + '/' + name + '0' + string + '.tif'
            dst_img = validation_cwd + name + '/' + name + '0' + string + '.tif'
        im = image.open(ori_img)
        im.resize((dst_w,dst_h),image.ANTIALIAS).save(dst_img,quality=save_q)
            
    for i in range(80,100):
        string = str(index[i])
        if index[i]>9:
            ori_img = cwd + name + '/' + name + string + '.tif'
            dst_img = test_cwd + name + '/' + name + string + '.tif'
        else:
            ori_img = cwd + name + '/' + name + '0' + string + '.tif'
            dst_img = test_cwd + name + '/' + name + '0' + string + '.tif'
        im = image.open(ori_img)
        im.resize((dst_w,dst_h),image.ANTIALIAS).save(dst_img,quality=save_q)