#!/usr/bin/env python3
# coding=utf-8
import cv2
import os
import numpy as np

RGB_Threshold = { 
                'green': {'L': np.array([0, 56, 0]), 'H': np.array([48, 255, 255])}, # 绿灯
                'red': {'L': np.array([115, 0, 37]), 'H': np.array([255, 76, 134])}, # 红灯  255 73 134
                } 

cap = cv2.VideoCapture(0)

def callback():
    pass


# 创建画布、窗口、进度条
canvas = np.zeros((40, 450, 3), dtype=np.uint8) + 255  # 创建画布放置阈值动态调节窗口
cv2.imshow("THRESHOLD", canvas)
cv2.createTrackbar("R_min", "THRESHOLD", 0, 255, callback)
cv2.createTrackbar("R_max", "THRESHOLD", 10, 255, callback)
cv2.createTrackbar("G_min", "THRESHOLD", 170, 255, callback)
cv2.createTrackbar("G_max", "THRESHOLD", 255, 255, callback)
cv2.createTrackbar("B_min", "THRESHOLD", 171, 255, callback)
cv2.createTrackbar("B_max", "THRESHOLD", 255, 255, callback)

while True:
    ret, frame = cap.read()
    
    R_min = cv2.getTrackbarPos("R_min", "THRESHOLD", )  
    R_max = cv2.getTrackbarPos("R_max", "THRESHOLD", )
    G_min = cv2.getTrackbarPos("G_min", "THRESHOLD", )
    G_max = cv2.getTrackbarPos("G_max", "THRESHOLD", )
    B_min = cv2.getTrackbarPos("B_min", "THRESHOLD", )
    B_max = cv2.getTrackbarPos("B_max", "THRESHOLD", )
    # R_min = 0
    # R_max = 48
    # G_min = 56
    # G_max = 255
    # B_min = 0
    # B_max = 255
    
    frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)
    
    if not ret:
        continue
    

    # frame = frame[120:240, :, :] # 180x200
    frame = frame[50:130, 80:280, :]
    frame = cv2.resize(frame, (400, 160), cv2.INTER_AREA)
    
    blur_frame = cv2.medianBlur(frame, 7)  
    rgb_image = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('rgb_image', rgb_image)

    frame_binary = cv2.inRange(rgb_image, np.array([R_min, G_min, B_min]), np.array([R_max, G_max, B_max])) 
    # _ , frame_binary = cv2.threshold(gray_image,R_min,R_max,cv2.THRESH_BINARY)

    erode_kernel = (3, 3)
    dilate_kernel = (7, 7)
    frame_binary_DE = cv2.erode(frame_binary, erode_kernel, iterations=1)
    frame_binary_DE = cv2.dilate(frame_binary_DE, dilate_kernel, iterations=1)


    cv2.imshow('frame_binary_DE', frame_binary_DE)


    contours ,h= cv2.findContours(frame_binary_DE, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    len_cont = len(contours)
    
    element_area = 0
    if len_cont > 0:
        # cv2.imshow("img", img)
        for contour in contours:
            contours_img = cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
            element_area += cv2.contourArea(contour)
            cv2.imshow("contours_img : ",contours_img)
    
    print("element_area: ",element_area)
    # contours = cv2.findContours(frame_binary_DE, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # len_cont = len(contours)
    # max_cont_area = 0
    # all_cont_area = 0
    # if len_cont > 0:
    #     for c in contours:
    #         all_cont_area += cv2.contourArea(c)
    #     c = max(contours, key=cv2.contourArea)
    #     max_cont_area = cv2.contourArea(c)
    

    # cv2.putText(frame, str("all_cont_area:%d"%all_cont_area), (0, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0),2)
    # cv2.imshow("light_image ", light_image)
    cv2.imshow("frame ", frame)

    if cv2.waitKey(1) == ord('q'):
       break
        
        
        
cap.release()
cv2.destroyAllWindows()



