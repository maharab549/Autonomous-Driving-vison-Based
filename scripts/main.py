#! /usr/bin/env python3

import sys 
import os
path = os.path.abspath(".")
sys.path.insert(0,path+"/src/opencv_detection/scripts")

import rospy
import cv2
import ctypes
import numpy as np
import  time
from  geometry_msgs.msg import Twist
from  ai_yolov5 import YoLov5TRT ,get_max_area
from opencv_line import line_preprocess,find_lines,how_to_turn,element_preprocess,tuple_transform
from servo_pd import Servo_PD

PLUGIN_LIBRARY =  "/home/blossoms/ai_control/src/opencv_detection/scripts/320_yolo/libmyplugins.so"
engine_file_path = "/home/blossoms/ai_control/src/opencv_detection/scripts/320_yolo/320.engine"

# PLUGIN_LIBRARY = "/home/blossoms/ai_control/src/opencv_detection/scripts/small_yolo/libmyplugins.so"
# engine_file_path = "/home/blossoms/ai_control/src/opencv_detection/scripts/small_yolo/small.engine"
categories = ["slope","side_walk","speed","speed_limit","turn_left"]
yolo_flag = 1
line_flag = 1

Servo_Kp = 0.022
Servo_Kd = 0.062

speed_x = 0.6

if __name__=="__main__":
    rospy.init_node("opencv_main")
    pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
    twist = Twist()

    start_time = 0
    end_time = 0

    redline_flag = 0
    crossing_flag = 0
    yellow_flag = 0

    redline_area = 0
    crossing_area = 0
    yellow_area = 0


    slope_flag =0
    side_walk_flag =0
    speed_limit_flag =0
    speed_flag =0
    turn_left_flag =0
    
    slope_area =0
    crossing_area =0
    speed_limit_area =0
    speed_area =0
    turn_left_area =0

    cls_id = 10
    area = 0
    score = 0

    stop_time = [-1,-1]
    yolo_time = [0,0]

    ctypes.CDLL(PLUGIN_LIBRARY) 
    yolov5_wrapper = YoLov5TRT(engine_file_path)
    cap = cv2.VideoCapture(0)
    Servo = Servo_PD(Servo_Kp,Servo_Kd)
    new_mask_points = np.array([[(0,105), (0,0) ,(260,0),(260,105)]])
    rospy.loginfo("enter opencv_main")
    try:
        while not rospy.is_shutdown():
            # 640x480
            ret, img = cap.read()
            if not ret:
                continue
            img = cv2.resize(img, (320, 240), interpolation=cv2.INTER_AREA)
            # fps = cap.get(cv2.CAP_PROP_FPS)
            end_time = start_time
            start_time = rospy.get_time()
            fps = 1/(start_time - end_time)
            
            # img = cv2.resize(img,[320,240])
            
            if yolo_flag:
                # yolo_time[0] = rospy.get_time()
                # image = cv2.resize(img, (640, 360), interpolation=cv2.INTER_AREA)
                frame = img[0:224, 100:320, :]
                result_boxes, result_scores, result_classid, use_time = yolov5_wrapper.infer(frame)

                # print("use_time : ",use_time)
                if (len(result_classid) != 0):
                    cls_id, area, score = get_max_area(frame,result_boxes, result_classid,result_scores)
                    cv2.putText(frame, str("cls_id:%s" % categories[cls_id]), (20, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.putText(frame, str("area:%d" % area), (20, 160),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.putText(frame, str("score:%f" % score), (20, 130),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                # yolo_time[1] = rospy.get_time()
                # print("yolo_time",yolo_time[1]-yolo_time[0])
                # cv2.imshow("frame", frame)

            if line_flag:

                # yolo_time[0] = rospy.get_time()
                # element_img = img[135:240 , 25:285, : ]
                line_img = cv2.resize(img, (240, 180), interpolation=cv2.INTER_AREA)
                line_img = line_img[ 100:180 , : , : ]  #h*w

                line_roi=line_preprocess(line_img)

                line_img, left_results, right_results, left_fit, right_fit = find_lines( line_roi, line_img,yellow_flag)
                if len(left_results) > 0 and len(right_results) > 0 and redline_flag == 4  and yellow_flag != 8:
                    # 创建梯形掩模，只处理赛道中间的区域
                    A ,B ,C, D  = tuple_transform(left_results,right_results)
                    # if left_results[0][0] > right_results[0][0]:
                    #     left_results[0] =  (yellow_img.shape(1)/2-20,0)
                    #     right_results[0] = (yellow_img.shape(1)/2+20,0)
                    # print("left : ",left_results , "right: " ,right_results)
                    mask_points = np.array([[A ,B ,C, D]])
                    
                    yellow_area = element_preprocess(element_img,"yellow",mask_points)

                    if yellow_flag == 0 and yellow_area > 500:
                        yellow_flag += 1
                    elif yellow_flag  == 1 and yellow_area < 5:
                        yellow_flag += 1
                    elif yellow_flag == 2 and yellow_area > 500:
                        yellow_flag += 1
                    elif yellow_flag  == 3 and yellow_area < 5:
                        yellow_flag += 1
                    elif yellow_flag == 4 and yellow_area > 500:
                        yellow_flag += 1
                    elif yellow_flag  == 5 and yellow_area < 5:
                        yellow_flag += 1
                    elif yellow_flag == 6 and yellow_area > 500:
                        yellow_flag += 1
                    elif yellow_flag  == 7 and yellow_area < 50:
                        yellow_flag += 1
                        twist.linear.x=0.0
                        stop_time[0] = rospy.get_time()


                    

                if redline_flag != 4 and 0:
                    redline_area = element_preprocess(element_img,"red_line",new_mask_points)
                if crossing_flag !=1 and 0:
                    crossing_area = element_preprocess(element_img,"crossing",new_mask_points)
                error = how_to_turn(line_roi, left_results , right_results, left_fit, right_fit)
                # output = Servo.calc_servo_pd(error)
                # twist.linear.x=0.4
                if redline_flag == 0 and redline_area>1500:
                    redline_flag += 1
                elif redline_flag == 1  and redline_area == 0:
                    redline_flag += 1
                elif redline_flag == 2  and redline_area >1500:
                    redline_flag += 1
                elif redline_flag == 3  and redline_area <1500:
                    redline_flag += 1
                    twist.linear.x=0.0
                    stop_time[0] = rospy.get_time()
                  

                if  crossing_flag==0 and crossing_area>3500:
                    crossing_flag += 1
                    twist.linear.x=0.0
                    stop_time[0] = rospy.get_time()


                if side_walk_flag == 0 and cls_id == 1 and area > 700 and score > 0.8:
                    side_walk_flag =1 
                    crossing_flag = 1
                    twist.linear.x=0.0
                    stop_time[0] = rospy.get_time()
                
                if slope_flag == 0 and cls_id == 0 and area > 1500 and score > 0.8:
                    slope_flag =1 
                    redline_flag = 4
                    twist.linear.x=0.0
                    stop_time[0] = rospy.get_time()

                if (crossing_flag==1 or redline_flag==4 or yellow_flag == 8) and stop_time[1]-stop_time[0] > 1.5 or stop_time[0] ==-1:
                    twist.linear.x=speed_x
                    stop_time = [-1, -1]


                stop_time[1] = rospy.get_time()
                

                # twist.angular.z= output
                # print("yellow_flag : ", yellow_flag)
                cv2.imshow("line_img",line_img)
                # rospy.loginfo("error:%.0f  output:%.2f,fps: %d ,redline_area: %d ",error,output,fps,redline_area)
                rospy.loginfo("fps: %d",fps)
                # pub.publish(twist)
                # yolo_time[1] = rospy.get_time()
                # print("line_time :" ,yolo_time[1]-yolo_time[0])
                # end_time = time.time_ns()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # destroy the instance
        twist.linear.x=0.0
        twist.angular.z=0
        pub.publish(twist)
        
        rospy.loginfo("exit  opencv_main")
        cap.release()
        cv2.destroyAllWindows()
        yolov5_wrapper.destroy()
