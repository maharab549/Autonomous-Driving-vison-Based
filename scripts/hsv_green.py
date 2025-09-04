#!/usr/bin/env python3.6
# coding=utf-8
import cv2
import os
import numpy as np



cap = cv2.VideoCapture(0,cv2.CAP_V4L2)

def callback():
    pass


# 创建画布、窗口、进度条
canvas = np.zeros((40, 450, 3), dtype=np.uint8) + 255  # 创建画布放置阈值动态调节窗口
cv2.imshow("THRESHOLD", canvas)
cv2.createTrackbar("H_min", "THRESHOLD", 34, 180, callback)
cv2.createTrackbar("H_max", "THRESHOLD", 77, 180, callback)
cv2.createTrackbar("S_min", "THRESHOLD", 116, 255, callback)
cv2.createTrackbar("S_max", "THRESHOLD", 255, 255, callback)
cv2.createTrackbar("V_min", "THRESHOLD", 113, 255, callback)
cv2.createTrackbar("V_max", "THRESHOLD", 255, 255, callback)


while True:
    ret, frame = cap.read()
    
    H_min = cv2.getTrackbarPos("H_min", "THRESHOLD", )  # 获得进度条值
    H_max = cv2.getTrackbarPos("H_max", "THRESHOLD", )
    S_min = cv2.getTrackbarPos("S_min", "THRESHOLD", )
    S_max = cv2.getTrackbarPos("S_max", "THRESHOLD", )
    V_min = cv2.getTrackbarPos("V_min", "THRESHOLD", )
    V_max = cv2.getTrackbarPos("V_max", "THRESHOLD", )
    
    frame = cv2.resize(frame, (320, 240), cv2.INTER_AREA)
    frame = frame[50:130, 100:260, :] # 180x200
    light_image = cv2.resize(frame, (400, 200), cv2.INTER_AREA)
    
    blur_frame = cv2.medianBlur(light_image, 7)  
    hsv_image = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)
    

    frame_binary = cv2.inRange(hsv_image, np.array([H_min, S_min, V_min]), np.array([H_max, S_max, V_max]))  

    kernel = (3, 3)
    frame_binary_DE = cv2.erode(frame_binary, kernel, iterations=1)
    frame_binary_DE = cv2.dilate(frame_binary_DE, kernel, iterations=2)
    cv2.imshow('frame_binary_DE', frame_binary_DE)
    
    contours = cv2.findContours(frame_binary_DE, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    len_cont = len(contours)
    max_cont_area = 0
    all_cont_area = 0
    if len_cont > 0:
        for c in contours:
            all_cont_area += cv2.contourArea(c)
        c = max(contours, key=cv2.contourArea)
        max_cont_area = cv2.contourArea(c)
    

    cv2.putText(frame, str("all_cont_area:%d"%all_cont_area), (0, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0),2)
    cv2.imshow("light_image ", light_image)
    # cv2.imshow("frame ", frame)

    if cv2.waitKey(1) == ord('q'):
       break
        
        
        
cap.release()
cv2.destroyAllWindows()



