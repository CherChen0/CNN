# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:11:13 2017

@author: cher
"""

import os 

 
cwd='E:\Anaconda_3\examples\Working\Tensorflow_practice\Train_Images\\'
classes=['agricultural','airplane','baseballdiamond','beach','buildings','chaparral',
'denseresidential','forest','freeway','golfcourse','harbor','intersection','mediumresidential',
'mobilehomepark','overpass','parkinglot','river','runway','sparseresidential','storagetanks',
'tenniscourt'] #人为 设定 21 类

f1 = open('train.txt','w')
index = 0
for i in range(21):
    name = classes[i]
    class_path=cwd+name+'\\'
    for img_name in os.listdir(class_path):
        img_path=class_path+img_name
        f1.write(img_path + ' ' + str(index))  #序列化为字符串
        f1.write('\n')
    index = index + 1
 
f1.close()