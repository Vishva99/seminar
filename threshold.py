# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:40:29 2016

@author: admin
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
#import Tkinter
#import tkMessageBox
#import easygui
import ctypes


img1 = cv2.imread('SEM Image 2.jpg',0)
#tkMessageBox.showinfo("Image area selection","Select two points which will crop the image and the calculations will be based on the selected area")
ctypes.windll.user32.MessageBoxA(0, "Select two points which will crop the image and the calculations will be based on the selected area", "Image area selection", 1)
#img=img1[0:150,0:150]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img1,'gray')
v=[]
w=[]
def oneclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print 'x = %d, y = %d'%(
        ix, iy)

    global coords
    coords = [ix, iy]
    v.append(ix)
    w.append(iy)
    return coords
for i in xrange(0,1):

    cid = fig.canvas.mpl_connect('button_press_event', oneclick)
plt.show()
img=img1[w[0]:w[1],v[0]:v[1]]

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,110,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

'''for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
#plt.imshow(thresh5,'gray')
#plt.show()'''

plt.imshow(thresh2,'gray')    
plt.show()
contours,hierarchy = cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
m=len(contours)
cnt = contours[1]
#print m

(x,y),radius= cv2.minEnclosingCircle(cnt)
radius=int(radius)
center=(int(x),int(y))
cv2.circle(thresh2,center,radius,(255,0,255),1)
'''plt.imshow(thresh2,'gray')
plt.show()'''
#cv2.imshow('img',thresh2)
#cv2.waitKey()
x1=[]
y1=[]
radius1=[]
area1=[]
for i in xrange(m):
    cnt = contours[i]
    (x,y),radius= cv2.minEnclosingCircle(cnt)
    area=cv2.contourArea(cnt)
    area1.append(area)
    radius=int(radius)
    center=(int(x),int(y))
    cv2.circle(thresh2,center,radius,(255,0,255),2)
    x1.append(x)
    y1.append(y)
    radius1.append(radius)
    center = (x1,y1)
radius2=sorted(radius1)    
#print sorted(area1) 
plt.imshow(thresh2,'gray') 
plt.show()
#print radius1

r=[]
from collections import defaultdict
d=defaultdict(int)
'''for n in radius2:
    d[n] +=1
    r+=[d[n]]   
t=[]    
for j in xrange(m):
    if r[j]<=3:
        radius2[j]=0
for i, j in enumerate(radius2):
    if j == 0:
        t+=[i]   
        
radius3=np.delete(radius2,t)'''
plt.hist(sorted(area1),bins=30)
plt.show()
for n in area1:
    d[n]+=1
    r+=[d[n]]
t=[]
for j in xrange(m):
    if area1[j]<=20:
        area1[j]=0
for i,j in enumerate(area1):
    if j ==0:
        t+=[i]
        
area2=np.delete(area1,t)
r1=np.delete(r,t)
#print radius3
print area2       
print r1     
#plt.plot(area2,r1,'r')
'''
plt.hist(sorted(area2),bins=30)
plt.show()'''



        
#print radius2    
#print r    
#plt.plot(radius3,r1,'r')
#plt.show()
#easygui.msgbox("please select the scale in the image by selecting the start point and the end point","image scaling")
ctypes.windll.user32.MessageBoxA(0, "please select the scale in the image by selecting the start point and the end point", "image scaling", 1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img1,'gray')
u=[]
def twoclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print 'x = %d, y = %d'%(
        ix, iy)

    global coords
    coords = [ix, iy]
    u.append(ix)
    return coords


for i in xrange(0,1):

    cid = fig.canvas.mpl_connect('button_press_event', twoclick)


plt.show()
x1=50/(u[1]-u[0])
area3=area2*x1**2
print area3




#radius = int(radius)
#img1 = cv2.circle(thresh2,center,radius,(0,255,0),2)
#plt.imshow(img1,'gray')

#plt.imshow(img1,'gray')
#plt.show()

#contours = cv2.findContours(thresh3, 1, 2)
#while contours:
    
    #print contours
    #contours=contours.h_next()
#M = cv2.moments(cnt)
#print M