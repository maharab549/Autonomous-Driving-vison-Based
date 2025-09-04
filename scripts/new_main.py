#! /usr/bin/env python3


import sys
import os
path = os.path.abspath(".")
sys.path.insert(0,path+"/src/opencv_detection/scripts")
import threading
import rospy
import numpy as np
import cv2
import time
import ctypes
from  std_msgs.msg import UInt8
from  geometry_msgs.msg import Twist
from  ai_yolov5 import YoLov5TRT ,draw_rerectangle,get_max_area
# Add PyCUDA import to resolve context cleanup issues
import pycuda.driver as cuda


# Threshold for colors to keep
# Obtained using hsv.py
H_min = 20#20
H_max = 80
S_min = 80 #80,78   46 anti-reflection adjustment, but will recognize others as lines
S_max = 255
V_min = 40 #40
V_max = 255
# Red line threshold when changing lanes
H_max_2 = 15 # MODIFIED: Adjusted H_max for red line detection to be more precise
S_min_2 = 45#78   46 anti-reflection adjustment, but will recognize others as lines
S_max_2 = 255
V_min_2 = 40
V_max_2 = 255


HSV_Threshold = {"red_line": {"L1": np.array([0, 100, 70]), "H1": np.array([10, 200, 255]), "L2": np.array([170, 120, 80]), "H2": np.array([180, 255, 255])}, # Red line
                 "crossing": {"L": np.array([80, 0, 200]), "H": np.array([120, 40, 255])}, # Pedestrian crossing
                 "yellow": {"L": np.array([15, 50, 50]), "H": np.array([35, 255, 255])}, # Yellow dashed line
                 "green": {"L": np.array([50, 70, 40]), "H": np.array([70, 255, 255])}, # Green light
                 "red": {"L": np.array([170, 70, 40]), "H": np.array([190, 255, 255])}, } # Red light
# RGB_Threshold = { 
#                 'green': {'L': np.array([50, 54, 40]), 'H': np.array([90, 255, 255])}, # Green light
#                 'red': {'L': np.array([150, 90, 40]), 'H': np.array([180, 190, 255])}, # Red light  255 73 134
#                 } 

# R_min = 0
# G_min = 56
# B_min = 0
# R_max =48
# G_max =255
# B_max =255
# Hough transform parameters
rho = 1
theta = np.pi / 180
# Minimum curve intersections required to detect a line.
threshold = 50
# Minimum line length. Line segments shorter than this are rejected
min_line_lenght = 40
# Maximum allowed gap between line segments to treat them as a single line.
max_line_gap = 20
# Slope limits
slope_max = 3.0 ##2.7
slope_min = 0.3

start_cnt = 0
road_width = 0# Road width


side_walk_flag = True# Pedestrian crossing status
speed_limit_flag = True# Speed limit status
speed_flag = True# Speed limit release status
turn_flag = True# Turn completion status
turn_flag_2 = True
turn_left_flag = True# Left turn status
turn_right_flag = True# Right turn
speed_4_flag = False# Control speed limit
clean_flag = True

change_flag = True# Lane change
change_flag_2 = False# Lane change left/right line filtering
change_flag_3 = True
change_flag_4 = True

clean_right_flag = True# Speed limit right line cleanup
red_light_flag = True# Red light sign
red_light_area = 0# Red light area
green_light_flag = True# Green light sign
green_light_area = 0# Green light area
traffic_flag = True# Traffic light status
traffic_flag_2 = True

# ========== PROGRESSIVE DANGER DETECTION SYSTEM ==========
# TUNING PARAMETERS - MODIFY THESE VALUES TO TUNE BEHAVIOR:
DANGER_DETECTION_THRESHOLD = 370         # Initial danger detection threshold - start monitoring danger
DANGER_ACTION_THRESHOLD = 1200           # Danger action threshold - start gentle left turn avoidance
DANGER_GENTLE_LEFT_FORCE = 195            # Gentle left turn force (30% of normal turn) - adjust this value to change avoidance amplitude
DANGER_AVOIDANCE_SPEED = 0.30            # Speed during danger avoidance - slow down slightly but continue forward
DANGER_RECOVERY_TIME = 195.0               # Danger recovery time (seconds) - time to return to normal after avoidance

# Danger detection state variables
danger_detected = False                  # Is danger detected
danger_avoidance_active = False          # Is danger avoidance active
danger_start_time = 0                    # Danger avoidance start time
current_danger_area = 0                  # Current danger area

print("=== PROGRESSIVE DANGER DETECTION PARAMETERS ===")
print(f"Detection Threshold: {DANGER_DETECTION_THRESHOLD} (start monitoring)")
print(f"Action Threshold: {DANGER_ACTION_THRESHOLD} (start gentle left turn)")
print(f"Gentle Left Force: {DANGER_GENTLE_LEFT_FORCE} (30% turn strength)")
print(f"Avoidance Speed: {DANGER_AVOIDANCE_SPEED}")
print(f"Recovery Time: {DANGER_RECOVERY_TIME}s")
print("===============================================")
# ========================================================

danger_flag = True
danger_flag_2 = True
danger_flag_3 = True
doll_flag = True
stop_time = [-1,-1]
change_time = [0,0]
turn_time = [-1,-1]
clean_time = [0,0]
traffic_time = [0,0]
danger_time = [0,0]
side_time = [0,0]
last_stop_time = 0.0

delayed_stop_flag = False
delayed_stop_time = 0


yolo_flag = True
line_flag = True

speed = 0
EN = 0
def line_preprocess(origin_img):
    # opencv reads BGR, convert to HSV
    hsv = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
    # h = hsv[:,:,0]
    # s = hsv[:,:,1]
    # v = hsv[:,:,2]
    # ev = cv2.equalizeHist(v)
    # new_hsv = np.stack((h,s,ev),axis=2)
    # Filter out background, the numbers inside are the HSV color range of the colors to be kept, need to find them out yourself
    lower_color = np.array([H_min, S_min, V_min])
    higher_color = np.array([H_max, S_max, V_max])
    # Filter out background to keep lanes, binarize, filter out values greater than max and less than min
    binary_img = cv2.inRange(hsv, lower_color, higher_color)
    # # Gaussian blur filter
    # gs_img = cv2.GaussianBlur(binary_img, (5, 5), 0)
    # Create erosion and dilation kernel, 3*3 rectangle for dilation then erosion on binary image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Erosion
        
    erode_img = cv2.erode(binary_img, kernel,iterations=1)
    # Dilation
    dilate_img = cv2.dilate(erode_img, kernel,iterations=2)

    # Get boundary
    # line_img=cv2.Canny(erode_img)

    # cv2.imshow("frame",dilate_img)
    # Return the obtained lane image
    return dilate_img

def line_preprocess_2(origin_img):
    hsv = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
    binary_img1 = cv2.inRange(hsv, HSV_Threshold["red_line"]["L1"], HSV_Threshold["red_line"]["H1"])
    binary_img2 = cv2.inRange(hsv, HSV_Threshold["red_line"]["L2"], HSV_Threshold["red_line"]["H2"])
    binary_img = cv2.bitwise_or(binary_img1, binary_img2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    erode_img = cv2.erode(binary_img, kernel,iterations=1)
    dilate_img = cv2.dilate(erode_img, kernel,iterations=2)
    return dilate_img

# This function is different from line_preprocess, it is specifically for processing other color elements that need to be identified in the track
# Such as ramp red line, pedestrian crossing white line, traffic lights, etc.
# The second parameter is the element to be identified, e.g., 'red_line'
# Returns the area of the element for judgment
def element_preprocess(img,element):

    


    blur_frame = cv2.medianBlur(img, 7)  
    hsv_image = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow("rgb_image",rgb_image)

    # Filter out background to keep lanes, binarize, filter out values greater than max and less than min
    if element == 'red_line':
        binary_img1 = cv2.inRange(hsv_image, HSV_Threshold[element]['L1'], HSV_Threshold[element]['H1'])
        binary_img2 = cv2.inRange(hsv_image, HSV_Threshold[element]['L2'], HSV_Threshold[element]['H2'])
        binary_img = cv2.bitwise_or(binary_img1, binary_img2)
    else:
        binary_img = cv2.inRange(hsv_image, HSV_Threshold[element]['L'], HSV_Threshold[element]['H'])
    # binary_img = cv2.inRange(rgb_image, np.array([R_min, G_min,B_min ]), np.array([  R_max,G_max,B_max])) 
    # cv2.imshow("binary_img", binary_img)

    # Create dilation and erosion kernel and perform dilation and erosion
    # erode_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    erode_kernel = (3, 3)
    dilate_kernel = (7, 7)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    erode_img = cv2.erode(binary_img, erode_kernel)
    # cv2.imshow("erode_img", erode_img)
    dilate_img = cv2.dilate(erode_img, dilate_kernel)
    # if element != 'green' and element != 'red':
    #     mask = np.zeros_like(dilate_img)
    #     cv2.fillPoly(mask, mask_roi, 255)

    #     dilate_img  = cv2.bitwise_and(dilate_img ,mask)
    # cv2.imshow(element+'_img', dilate_img)

    # Find contours
    # Fix: In the new version of OpenCV, findContours only returns two values instead of three
    _, contours, hierarchy = cv2.findContours(dilate_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    len_cont = len(contours)


    element_area = 0
    if len_cont > 0:
        c = max(contours,key = cv2.contourArea)
        contours_img = cv2.drawContours(img, c, -1, (0, 255, 0), 3)
        element_area = cv2.contourArea(c)
        # cv2.imshow("img", img)
        # for contour in contours:
        #     contours_img = cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
        #     element_area += cv2.contourArea(contour)
        cv2.imshow("yolo",contours_img)
    # if element == "yellow":
    #     if element_area < 500:
    #         element_area = 0
    # print(element,"_area : ", element_area)
    return element_area

def HoughLines(line_roi):
    lines = cv2.HoughLinesP(line_roi, rho, theta, threshold,minLineLength=min_line_lenght, maxLineGap=max_line_gap)
    left_results, right_results, left_fit, right_fit = [], [], [], []
    if lines is not None:
        left_lines, right_lines = [], []
        # drawing = np.zeros(
        #     (line_img.shape[0], line_img.shape[1], 3), dtype=np.uint8)
        for line in lines:
            for x1, y1, x2, y2 in line:
                if y1 != y2:
                    k = float(x1 - x2) / (y1 - y2)
                    if slope_max > abs(k) > slope_min:
                        if k > 0:
                            if (k > 0.2 and clean_right_flag == False) or (k > 0.2 and change_flag == False and change_flag_2 == False):# Remove right line when speed limited, remove right line when changing lanes, restore after lane change
                                continue
                            if (x1>x2 and x1<120) or (x2>x1 and x2<120):
                                continue
                            right_lines.append(line)
                                # right_lines.pop(line)
                        elif k < 0:
                            if k > -1.4 and change_flag == False and change_flag_2 == False: # Filter left line when changing lanes, restore after lane change
                                continue
                            if (x1>x2 and x2>120) or (x2>x1 and x1>120):
                                continue
                            # midpoint_x = (x1 + x2) / 2
                            # distance_to_center = abs(midpoint_x - 120)  # Assume center_x is the x-coordinate of the center line
                            # if distance_to_center > 80 and -1.6 < k < -0.9 :
                            #     continue
                            left_lines.append(line)
                    else:
                        continue

        if len(left_lines) > 0:
            clean_lines(left_lines, 0.1)
            left_points = [(x1, y1)for line in left_lines for x1, y1, x2, y2 in line]
            left_points = left_points + [(x2, y2) for line in left_lines for x1, y1, x2, y2 in line]
            ymax, ymin = find_points(left_lines)
            left_results, left_fit = least_squares_fit(left_points, ymin, ymax)

        if len(right_lines) > 0:
            clean_lines(right_lines, 0.1)
            right_points = [(x1, y1)for line in right_lines for x1, y1, x2, y2 in line]
            right_points = right_points + [(x2, y2) for line in right_lines for x1, y1, x2, y2 in line]
            ymax, ymin = find_points(right_lines)
            right_results, right_fit = least_squares_fit(right_points, ymin, ymax)

        # if danger_flag == False :
        #     if len(left_lines) > 0 and len(right_lines) > 0:
        #         right_results[0] = left_results[1]
        #         right_results[1] = (240,70)
    return left_results, right_results, left_fit, right_fit

def least_squares_fit(point_list, ymin, ymax):
    # Least squares fitting
    x = [p[0] for p in point_list]
    y = [p[1] for p in point_list]
    # The third parameter of polyfit is the order of the fitted polynomial, so 1 represents linear
    # This is input in reverse, so K=0 when vertical
    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)  # Get the fitting result
    xmin = int(fit_fn(ymin))
    xmax = int(fit_fn(ymax))
    return [(xmin, ymin), (xmax, ymax)], fit


def find_points(lines):
    line_y_max = 0
    line_y_min = 999
    for line in lines:
        for x1, y1, x2, y2 in line:
            if y1 > line_y_max:
                line_y_max = y1
            if y2 > line_y_max:
                line_y_max = y2
            if y1 < line_y_min:
                line_y_min = y1
            if y2 < line_y_min:
                line_y_min = y2
    return line_y_max, line_y_min

# ========== PROGRESSIVE DANGER AVOIDANCE FUNCTION ==========
def progressive_danger_control():
    """
    Progressive danger avoidance control function
    Returns: (steering_adjustment, speed_adjustment, status_message)
    """
    global danger_avoidance_active, danger_start_time, current_danger_area
    
    # If no danger is detected, return normal control
    if not danger_detected:
        return 0, 0, "NORMAL"
    
    # If danger area is less than action threshold, continue forward but monitor
    if current_danger_area < DANGER_ACTION_THRESHOLD:
        return 0, 0, f"MONITORING - Area: {current_danger_area}"
    
    # Danger area reaches action threshold, start gentle left turn avoidance
    if not danger_avoidance_active:
        danger_avoidance_active = True
        danger_start_time = time.time()
        print(f" DANGER AVOIDANCE ACTIVATED - Area: {current_danger_area} > {DANGER_ACTION_THRESHOLD}")
    
    current_time = time.time()
    elapsed_time = current_time - danger_start_time
    
    # Gentle left turn during recovery time
    if elapsed_time <= DANGER_RECOVERY_TIME:
        # Calculate progressive recovery - maximum left turn force at the beginning, gradually decreasing
        recovery_factor = max(0, 1.0 - (elapsed_time / DANGER_RECOVERY_TIME))
        steering_adjustment = DANGER_GENTLE_LEFT_FORCE * recovery_factor
        
        status = f"GENTLE LEFT TURN - Force: {steering_adjustment:.1f}, Time: {elapsed_time:.1f}s"
        return steering_adjustment, 0, status
    
    # Recovery time ends, reset status
    else:
        danger_avoidance_active = False
        print("✅ DANGER AVOIDANCE COMPLETED - Returning to normal lane following")
        return 0, 0, "RECOVERY_COMPLETE"

def how_to_turn(shape, left_results, right_results, left_fit, right_fit):
    height = shape[0]
    width = shape[1]
    middle_line = width / 2
    # [(xmin, ymin), (xmax, ymax)]

    global road_width
    global start_cnt
    global side_walk_flag
    global speed_limit_flag
    global speed_flag
    global turn_left_flag
    global green_light_flag
    global red_light_flag # Added for red light turn
    global gentle_move_active # Added for gentle move after speed sign
    
    # error>0  Right turn
    # Both lines exist
    if len(left_results) > 0 and len(right_results) > 0:
        if start_cnt < 5 and EN ==1:
            start_cnt += 1
            road_width += (right_results[1][0] + right_results[0][0]) / 2 - (
                        left_results[1][0] + left_results[0][0]) / 2
            if start_cnt == 5:
                road_width /= 5
        # X = (left_results[1][0] + right_results[1][0]) / 2s
        X = (left_fit[0] * height / 2 + left_fit[1] + right_fit[0] * height / 2 + right_fit[1]) / 2
        if abs(left_results[1][1] - right_results[1][1]) < 20:
            X1 = (left_results[1][0] + right_results[1][0]) / 2
            X = (X + X1) / 2
        middle_line = X
        rho = -(middle_line - width / 2)
        # if clean_flag == False and green_light_flag:
        #     rho +=30
        # if green_light_flag == False:
        #     rho -=10
    # Only right line ----- Left turn
    elif len(left_results) == 0 and len(right_results) > 0:
        if start_cnt != 5:
            if turn_flag == False and side_walk_flag:
                road_width = 200
            else :
                road_width = 180
        X_top = right_results[0][0]
        X_bottom = (height - right_results[0][1]) * (right_results[0][0] - right_results[1][0]) / (
                right_results[0][1] - right_results[1][1]) + right_results[0][0]
        # X = (X_top - 10) / 2 + (X_bottom - width) / 2
        X = (X_top + X_bottom) / 2
        middle_line = X - road_width * 0.69
        # Curve
        # if right_fit[0] >= 1.3:
        # rho  = width/2-middle_line
        # Straight line lost
        # else:
        rho = width / 2 - middle_line
        rho = abs(rho)
        if change_flag_3 == False and change_flag_4:
            rho = 0
        # if danger_flag == False:
        #     rho = 40

    # Only left line ----- Right turn
    elif len(right_results) == 0 and len(left_results) > 0:
        if start_cnt != 5:
            if turn_flag == False and side_walk_flag:
                road_width = 200  #170
            else:
                road_width = 180 #140
        X_top = left_results[0][0] 
        X_bottom = (height - left_results[0][1]) * (left_results[0][0] - left_results[1][0]) / (
                left_results[0][1] - left_results[1][1]) + left_results[0][0]
        # X = (X_top + 10) / 2 + (X_bottom + width) / 2
        X = (X_top + X_bottom) / 2
        middle_line = X + road_width / 2
        # Curve
        # if left_fit[0] <= -1.3:
        # rho = -middle_line
        # Straight line lost
        # else:
        rho = width / 2 - middle_line
        # if clean_flag == False and green_light_flag:
        #     rho +=15
        rho = abs(rho)
        rho = -rho


    else:
        rho = 0
        # print("11111")
        if turn_left_flag == False and turn_flag :
            # time.sleep(0.04)
            rho = 130
        elif turn_right_flag == False and turn_flag :
            rho = -130
    
    # ========== PROGRESSIVE DANGER AVOIDANCE INTEGRATION ==========
    # Get steering adjustment for danger avoidance
    steering_adjustment, speed_adjustment, status = progressive_danger_control()
    
    if steering_adjustment != 0:
        # Apply gentle left turn adjustment, but not completely override normal steering
        rho += steering_adjustment
        print(f"DANGER STEERING ADJUSTMENT: +{steering_adjustment} -> Total rho: {rho}")
    
    if status != "NORMAL":
        print(f"DANGER STATUS: {status}")
    # ============================================================

    # ========== GENTLE MOVE LOGIC ==========
    # If gentle move is active, apply a slight right turn
    if gentle_move_active:
        # Apply a small negative rho value for a right turn (rho < 0 for right turn)
        # This value might need tuning based on simulation/real-world testing
        rho -= 20  # Adjust this value for the desired turn amount
        print(f"GENTLE MOVE: Applying right turn, rho: {rho}")
    # ================================================
    if danger_flag == False and danger_flag_2 :
            rho = 100
    if danger_flag == False and danger_flag_3 and danger_flag_2 == False :
            rho = 0





    
    print("middle_line: ", middle_line)
    # cv2.line(line_roi, (middle_line,105),(middle_line,0), (0, 255, 255), 5)
    if start_cnt == 5:
        print("road_width: ", road_width)
    return rho

def clean_lines(lines, threshold):
    # Iterate to calculate mean slope, exclude data with large differences
    slope = [(y2 - y1) / (x2 - x1)
             for line in lines for x1, y1, x2, y2 in line]
    while len(lines) > 0:
        # Average slope
        mean = np.mean(slope)
        diff = [abs(s - mean) for s in slope]
        idx = np.argmax(diff)
        if diff[idx] > threshold:
            slope.pop(idx)
            lines.pop(idx)
        else:
            break
def draw_lines(line_img,left_results,right_results,left_k,right_k):
    if len(left_results)!=0:
        cv2.line(line_img, left_results[0],left_results[1], (0, 0, 255), 10)
        cv2.putText(line_img, str("left_k:%.2f" % left_k[0]), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    if len(right_results)!=0:
        cv2.line(line_img, right_results[0],right_results[1], (0, 255, 0), 10)
        cv2.putText(line_img, str("right_k:%.2f" % right_k[0]), (120, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("line_img",line_img)

def tuple_transform(left_results, right_results):
    A_x = left_results[1][0]
    A_y = left_results[1][1]
    B_x = left_results[0][0]
    B_y = left_results[0][1]
    C_x = right_results[0][0]
    C_y = right_results[0][1]
    D_x = right_results[1][0]
    D_y = right_results[1][1]

    offset = 20

    return (A_x + offset, A_y), (B_x + int(offset / 2), B_y), (C_x, C_y), (D_x, D_y)

def wait(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

class Servo_PD():
    def __init__(self, servo_p, servo_d):
        self.Kp = servo_p
        self.Kd = servo_d
        self.error = 0
        self.last_error = 0
        self.target = 0
        self.output = 0
        self.output_limit = 3.8

    def calc_servo_pd(self, error,kp,kd):
        self.error = error
        self.Kp = kp
        self.Kd = kd
        self.output = self.Kp * self.error + self.Kd * (self.error - self.last_error)
        self.last_error = self.error
        if self.output > self.output_limit:
            self.output = self.output_limit
        elif self.output < - self.output_limit:
              self.output = - self.output_limit
        return self.output



# Speed control function, adjusts vehicle speed based on detected traffic signs (cls_id) and their area (area)
def speed_control(cls_id ,area):
    # Declare all global variables used (to maintain state between different function calls)
    global side_walk_flag        # Pedestrian crossing sign status
    global side_time             # Pedestrian crossing timer [start time, current time]
    global speed_limit_flag      # Speed limit sign status
    global speed_flag            # Speed limit release sign status
    global turn_left_flag        # Left turn sign status
    global turn_right_flag       # Right turn sign status
    global turn_flag             # Main turn flag
    global turn_flag_2           # Auxiliary turn flag
    global red_light_flag        # Red light sign status
    global red_light_area        # Red light detection area
    global green_light_flag      # Green light sign status
    global green_light_area      # Green light detection area
    global danger_flag           # Danger flag status
    global danger_flag_2         # Danger second stage flag
    global danger_flag_3         # Danger third stage flag
    global danger_time           # Danger area timer [start time, current time]
    global speed_4_flag          # Speed limit 4 flag (specific speed limit)
    global yolo_flag             # YOLO detection switch
    global traffic_flag          # Traffic light main flag
    global traffic_flag_2        # Traffic light auxiliary flag
    global speed                 # Current speed value
    global clean_right_flag      # Clear right flag
    global clean_time            # Clear timer [start time, current time]
    global clean_flag            # Clear flag status
    global delayed_stop_flag     # Delayed stop flag
    global delayed_stop_time     # Delayed stop time point
    global doll_flag             # Doll flag (unused)
    global last_stop_time        # Last stop time (unused)
    global stop_time             # Stop timer [start time, current time]
    global turn_time             # Turn timer [start time, current time]
    global change_flag           # Lane change flag
    global change_flag_2         # Lane change second stage flag
    global change_flag_3         # Lane change third stage flag
    global change_flag_4         # Lane change fourth stage flag
    global change_time           # Lane change timer [start time, current time]
    global traffic_time          # Traffic light timer [start time, current time]
    global speed_x               # Base speed value
    global red_light_turn_active # Added for red light turn
    global gentle_move_active # Added for gentle move after speed sign
    global gentle_move_start_time # Added for gentle move after speed sign
    global GENTLE_MOVE_DURATION # Added for gentle move after speed sign
    
    # ========== PROGRESSIVE DANGER DETECTION ==========
    global danger_detected, current_danger_area
    
    # Reset danger detection status
    danger_detected = False
    current_danger_area = 0
    
    # Detect danger sign - progressive logic
    if int(cls_id) == 0 and area > DANGER_DETECTION_THRESHOLD:
        danger_detected = True
        current_danger_area = area
        
        if area < DANGER_ACTION_THRESHOLD:
            print(f"⚠️  DANGER DETECTED - MONITORING: Area {area} < {DANGER_ACTION_THRESHOLD} (continue forward)")
        else:
            print(f" DANGER CLOSE - AVOIDANCE: Area {area} >= {DANGER_ACTION_THRESHOLD} (gentle left turn)")
    
    # Check if speed adjustment is needed for danger avoidance
    _, speed_adjustment, status = progressive_danger_control()
    if "GENTLE LEFT TURN" in status:
        # Slightly slow down during danger avoidance, but continue forward
        pass  # Speed adjustment handled in normal logic below
    # ================================================
    
    # Logic 1: Left turn sign (4) detected and area is large enough
    if turn_left_flag and turn_right_flag and int(cls_id) == 4 and area > 1200:
        turn_left_flag = False  # Turn off left turn flag
        turn_time[0] = time.time()  # Record turn start time
    
    # Logic 2: Right turn sign (5) detected and area is large enough
    elif turn_right_flag and turn_left_flag and int(cls_id) == 5 and area > 1150:
        turn_right_flag = False  # Turn off right turn flag
        turn_time[0] = time.time()  # Record turn start time
    
    # Logic 3: Pedestrian crossing sign (1) detected and area is large enough (after turning)
    elif side_walk_flag and int(cls_id) == 1 and turn_flag == False and area >= 1200:
        side_walk_flag = False  # Turn off pedestrian crossing flag
        stop_time[0] = time.time()  # Start stop timer
        side_time[0] = time.time()  # Start pedestrian crossing timer
    
    # Logic 4: Speed limit sign (3) detected and area is large enough
    elif speed_limit_flag and int(cls_id) == 3 and side_walk_flag == False and area > 780:
        speed_limit_flag = False  # Turn off speed limit flag
        clean_right_flag = False  # Disable right side clear
        speed_4_flag = True      # Enable speed limit 4 mode
        clean_flag = False       # Reset clear flag
        clean_time[0] = time.time()  # Start clear timer
        # gentle_move_active = True # Deactivated here
    
    # Logic 5: Speed limit release sign (2) detected and area is large enough
    elif speed_flag and int(cls_id) == 2 and speed_limit_flag == False and area > 850:
        speed_flag = False  # Turn off speed limit release flag
        gentle_move_active = True # Activate gentle move here
        gentle_move_start_time = time.time() # Record start time for gentle move
    
    # Check if gentle move should be deactivated
    if gentle_move_active and (time.time() - gentle_move_start_time > GENTLE_MOVE_DURATION):
        gentle_move_active = False
        print("GENTLE MOVE DEACTIVATED: Duration ended.")
    
    # Logic 6: Traffic light processing (after speed limit ends)
    elif traffic_flag and speed_flag == False:
        traffic_flag_2 = False  # Turn off auxiliary traffic flag
        # Red light detection (red light area greater than green light + threshold)
        if speed_flag == False and red_light_flag and (red_light_area > green_light_area+100  and red_light_area > 600):
            red_light_flag = False  # Turn off red light flag
            delayed_stop_time = time.time() + 0.80  # MODIFIED: Increased delay to stop further back from red light
            traffic_time[0] = time.time()  # Start traffic light timer
            gentle_move_active = True # Activate gentle move here
        # Green light detection (green light area greater than red light + threshold)
        elif red_light_flag == False and green_light_flag and (green_light_area > red_light_area+100  and green_light_area > 600):
            green_light_flag = False  # Turn off green light flag
            traffic_flag = False      # Turn off main traffic light flag
            yolo_flag = True          # Enable YOLO detection
            gentle_move_active = False # Deactivate gentle move here
        # Traffic light timeout handling (pass directly after 5 seconds)
        elif traffic_time[1]-traffic_time[0] > 5:
            traffic_flag = False  # Turn off main traffic light flag
            yolo_flag = True      # Enable YOLO detection
            gentle_move_active = False # Deactivate gentle move here
    
    # Logic 7: Lane change sign (6) detected and area is large enough
    elif traffic_flag == False and change_flag and int(cls_id) == 6 and area > 200:
        change_flag = False  # Turn off lane change flag
        change_time[0]=time.time()  # Start lane change timer
    
    # Logic 8: Danger sign (0) detected and area is large enough
   # elif change_flag == False and danger_flag and int(cls_id)== 0 and area > 370:
    #   danger_flag = False  # Turn off danger flag
       # danger_time[0] = time.time()  # Start danger area timer



    # Stop control logic
    if stop_time[0]!=-1:
        speed = 0.0  # Stop immediately
        stop_time[1] = time.time()  # Update stop end time
    
    # Speed control logic after stopping
    if stop_time[0] == -1  or stop_time[1]-stop_time[0] > 2:  # Stop ends or more than 2 seconds
        # ========== DANGER AVOIDANCE SPEED CONTROL ==========
        # If danger avoidance is active, use danger avoidance speed
        if danger_avoidance_active:
            speed = DANGER_AVOIDANCE_SPEED
            print(f"DANGER AVOIDANCE SPEED: {speed}")
        # ===================================================
        # Speed limit 4 mode (0.28 speed)
        elif speed_4_flag:
            speed = 0.25
            if speed_flag == False:  # Exit this mode after speed limit release
                speed_4_flag = False
        # Initial turn speed (0.3)
        elif (turn_left_flag == True and turn_right_flag == True) and turn_flag:
            speed = 0.2
        # Turning speed (0.3)
        elif turn_flag:
            speed = 0.2 
        # Speed from turn end to pedestrian crossing stage (0.3)
        elif turn_flag_2 == False and side_walk_flag:
            speed = 0.3
        # Speed from turn end to pedestrian crossing transition stage (0.4)
        elif turn_flag == False and turn_flag_2 and side_walk_flag:
            speed = 0.3
        # Speed from pedestrian crossing to speed limit stage (0.38)
        elif side_walk_flag == False and speed_limit_flag:
            speed = 0.35
        # Speed from speed limit release to traffic light stage (0.33)
        elif speed_flag == False and red_light_flag:
            speed = 0.35
        # Red light stop control
        elif traffic_flag and red_light_flag == False and green_light_flag and time.time() >= delayed_stop_time:
            speed = 0.0  # Full stop
            traffic_time[1] = time.time()  # Update traffic light end time
        # Lane change preparation stage (0.18 low speed)
        elif traffic_flag == False and change_flag:
            speed = 0.18
        # After lane change stage (0.3)
        elif change_flag == False and change_flag_4:
            speed = 0.3
        # Before danger area stage (0.3)
        elif change_flag_4 == False and danger_flag:
            speed = 0.3
        # During danger area stage (0.2 low speed)
        elif danger_flag == False and danger_flag_2:
            speed = 0.2
        # Default driving speed (0.4)
        elif danger_flag == False and danger_flag_2 == False:
            speed = 0.4
        # Minimum speed (using externally defined speed_x)
        else:
            speed = speed_x
        
        # Reset stop timer
        stop_time = [-1,-1]
        
        # Turn time control
        if turn_time[0] != 0 and (turn_left_flag == False or turn_right_flag == False):
            turn_time[1] = time.time()
            if turn_time[1]-turn_time[0] > 1.2:  # Turn off main turn flag after 1.2 seconds
                turn_flag = False
            if turn_time[1]-turn_time[0] > 4.2:  # Turn off auxiliary turn flag after 4.2 seconds
                turn_flag_2 = False
        
        # Lane change time control
        if change_time[0] != 0 and change_flag == False:
            change_time[1] = time.time()
            if change_time[1] - change_time[0] > 2.5:  # Enter second stage after 2.5 seconds
                change_flag_2 = True
            if change_time[1] - change_time[0] > 4.5:  # Turn off third stage after 4.5 seconds
                change_flag_3 = False
            if change_time[1] - change_time[0] > 5.0:  # Turn off fourth stage after 5.0 seconds
                change_flag_4 = False
        
        # Danger area time control
        if danger_time[0] != 0 and danger_flag == False:
            danger_time[1] = time.time()
            if danger_time[1] - danger_time[0] > 0.476:  # Turn off second stage after 0.476 seconds
                danger_flag_2 = False
            if danger_time[1] - danger_time[0] > 1.5:   # Turn off third stage after 1.5 seconds
                danger_flag_3 = False
                danger_time = [0,0]  # Reset timer
        
        # Clear operation time control
        if clean_time[0] !=0 and clean_flag == False:
            clean_time[1] = time.time()
            if clean_time[1] - clean_time[0] > 4:  # Enable right side clear after 4 seconds
                clean_right_flag = True
            if clean_time[1] - clean_time[0] > 6:  # Reset timer after 6 seconds
                clean_time = [0,0]
        
        # Pedestrian crossing time control
        if side_time[0] !=0 and side_walk_flag == False:
            side_time[1] = time.time()
            if side_time[1]-side_time[0] > 6:  # Reset timer after 6 seconds
                side_time = [0,0]
    
    # Print current speed and return
    print("speed: ",speed)
    return speed


def switch_callback(msg):
    global EN
    EN = msg.data

GENTLE_MOVE_DURATION = 2.0 # Duration for the gentle right turn in seconds

# Global variables for control states
red_light_turn_active = False
gentle_move_active = False
gentle_move_start_time = 0.0

if __name__=="__main__":
    rospy.init_node("opencv_new_main")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
    twist = Twist()
    PLUGIN_LIBRARY =  "/home/jetson/catkin_ws/ws/src/opencv_detection/scripts/2025/libmyplugins.so"
    engine_file_path = "/home/jetson/catkin_ws/ws/src/opencv_detection/scripts/2025/best.engine"
    categories = ["danger", "side_walk", "speed", "speed_limit", "turn_left","turn_right","lane_change","red_light","green_light","doll_all"]

    # yolo_flag = True
    # line_flag = True

    # Servo_Kp = 0.022
    # Servo_Kd = 0.062
    # Servo_Kp = 0.016
    # Servo_Kd = 0.056
    # Servo_Kp = 0.014
    # Servo_Turn_Kp = 0.02
    # Servo_Kd = 0.055

    speed_x = 0.30 #0.7 #10 #35

  
    Servo_Kp = 0.22 #0.06 #0.07 #0.010
    Servo_Turn_Kp = 0.035 #0.09 #0.013
    Servo_Kd = 0.065 #0.070 #0.067 #0.057
    # if change_flag == False and change_flag_3 == False :
    #     Servo_Kp = 0.021
    #     Servo_Turn_Kp = 0.041
    #     Servo_Kd = 0.088 #0.057


    start_time = 0
    end_time = 0

    redline_flag = 0
    crossing_flag = 0
    yellow_flag = 0

    redline_area = 0
    crossing_area = 0
    yellow_area = 0


    cap = cv2.VideoCapture(0)#,cv2.CAP_V4L2
    Servo = Servo_PD(Servo_Kp, Servo_Kd)
    # new_mask_points = np.array([[(0, 105), (0, 0), (260, 0), (260, 105)]])
    
    # if clean_right_flag == False :
    #     mask_points = np.array([[(0, 70),(100,0),(240, 0),(240, 70)]])
    # else :
    #     mask_points = np.array([[(0, 70),(0, 60),(60,0) ,(240, 0),(240, 70)]])
    # mask = np.zeros((70,240), dtype=np.uint8)
    # cv2.fillPoly(mask,mask_points,255)

    # traffic_tmp = cv2.imread("/home/blossoms/ai_control/src/opencv_detection/scripts/picture/traffic.jpg")
    # traffic_tmp = cv2.cvtColor(traffic_tmp,cv2.COLOR_BGR2HSV)
    # traffic_tmp = cv2.pyrDown(traffic_tmp)

    # Initialize CUDA
    cuda.init()
    
    ctypes.CDLL(PLUGIN_LIBRARY)
    yolov5_wrapper = YoLov5TRT(engine_file_path)

    # while EN==0:
    # en_sub = rospy.Subscriber("switch",UInt8,switch_callback)
    #     print("EN " ,EN)
    
    rospy.loginfo("enter opencv_main")

    try:
        while not rospy.is_shutdown():
            ret, img = cap.read()
            if not ret:
                continue
            # print(img.shape)
            img = cv2.resize(img, (320, 240), interpolation=cv2.INTER_AREA)
            end_time = start_time
            start_time = time.time()
            fps = 1 / (start_time - end_time)
            # print("EN " ,EN)
            if clean_right_flag == False :
                mask_points = np.array([[(0, 70),(118,0),(240, 0),(240, 70)]])
            elif turn_flag == False and side_walk_flag:
                if turn_left_flag == False and turn_flag_2 == False:
                    mask_points = np.array([[(0, 70),(0,0),(130, 0),(130, 70)]])
                elif turn_right_flag == False and turn_flag_2 == False :
                    mask_points = np.array([[(110, 70),(110,0),(240, 0),(240, 70)]])
                elif turn_left_flag == False and turn_flag_2:
                    mask_points = np.array([[(0, 70),(0, 60),(120,0),(240, 0),(240, 70)]])
                elif turn_right_flag == False and turn_flag_2 :
                    mask_points = np.array([[(0, 70),(0,0),(120, 0),(240, 60),(240, 70)]])
            else :
                mask_points = np.array([[(0, 70),(0, 50),(50, 0),(190, 0),(240,50),(240, 70)]])
            mask = np.zeros((70,240), dtype=np.uint8)
            cv2.fillPoly(mask,mask_points,255)
            if line_flag:
            # element_img = img[135:240 , 25:285, : ]
                line_img = cv2.resize(img, (240, 180), interpolation=cv2.INTER_AREA)
                if change_flag == False and change_flag_4:
                #     line_img = line_img[110:180, :, :]
                    min_line_lenght = 18
                    max_line_gap = 30
                elif turn_flag :
                    min_line_lenght = 13
                elif speed_flag == False and traffic_flag :
                     min_line_lenght = 60
                else :
                    min_line_lenght = 30
                    max_line_gap = 20
                
                line_img_2 = line_img.copy()
                
                # if turn_left_flag and turn_right_flag :
                #     line_img = line_img[110:180, :, :]
                #     # min_line_lenght = 15
                # else:
                line_img = line_img[90:160, :, :]  # h*w
                line_img_2 = line_img.copy()
                line_roi = line_preprocess(line_img)
                
                if change_flag == False:# Red processing of right line during lane change
                    line_roi_2 = line_preprocess_2(line_img_2)
                    line_roi = cv2.bitwise_or(line_roi,line_roi_2)# Merge right line with left line
                if (turn_flag_2 == False and side_walk_flag ) or change_flag == False :
                    slope_max = 5
                else:
                    slope_max = 3.0
                line_roi = cv2.bitwise_and(line_roi,mask)
                line_shape = line_img.shape
                cv2.imshow("frame",line_roi)
                left_results, right_results, left_fit, right_fit = HoughLines(line_roi) # Moved this line up
                error = how_to_turn(line_shape,left_results , right_results, left_fit, right_fit)
                if speed == 0.0 :
                    error = 0
                # if speed_flag == False and traffic_flag :
                #     if error <= -50 :
                #         error = -50
                print("error:",error)
                if change_flag == False and change_flag_2 == False :
                    Servo_Kp = 0.020
                    Servo_Turn_Kp = 0.039
                    Kd = 0.070# 0.057
                else:
                    Servo_Kp = 0.013
                    Servo_Turn_Kp = 0.016
                    Kd = 0.065# 0.057
                if abs(error) > 60:
                    Kp = Servo_Turn_Kp
                elif 60 >= abs(error) > 30:
                    Kp = (Servo_Turn_Kp+Servo_Kp)*0.5
                else:
                    Kp = Servo_Kp
                # if speed_x > 0.88 and speed == 0.7:
                #     Kp = 0.013
                output = Servo.calc_servo_pd(error,Kp,Kd)
                # twist.angular.z = output
                # cv2.imshow("mask",mask)
                # if turn_flag == False:
                draw_lines(line_img,left_results, right_results, left_fit, right_fit)


            cls_id = 5
            area = 0

            if yolo_flag:
            # image = cv2.resize(img, (640, 360), interpolation=cv2.INTER_AREA)
                frame = img[:180, :320, :]
                frame = cv2.resize(frame,(192,144),cv2.INTER_AREA)
                # frame = img[:192, 64:320, :]
                result_boxes, result_scores, result_classid, use_time = yolov5_wrapper.infer(frame)
                if len(result_classid) != 0:
                    cls_id, area, max_box,score = get_max_area(result_boxes, result_classid,result_scores)
                    if area > 100 and score >= 0.3:
                        draw_rerectangle(frame,max_box,categories[cls_id],score,area)
                cv2.imshow("yolo", frame)
                

            if traffic_flag and traffic_flag_2 == False:
                element_img = img[:180, :320, :]
                element_img = cv2.resize(element_img,(192,144),cv2.INTER_AREA)
                green_img = element_img.copy()
                # Green light must be placed first, otherwise green light area will accumulate, unknown BUG
                red_light_area =  element_preprocess(element_img,'red')
                if red_light_flag == False and green_light_flag:
                    green_light_area = element_preprocess(green_img, 'green')
                print("green_light_area: ",green_light_area)
                print("red_light_area: ",red_light_area)


            # while EN==0:
            # if EN == 0:
            #     en_sub = rospy.Subscriber("switch",UInt8,switch_callback)
            # else :
            if doll_flag and int(cls_id) == 9 and area >700:
                twist.linear.x = 0
                twist.angular.z = 0
                doll_flag = False 
                last_stop_time = time.time()
            elif (doll_flag == False and len(result_classid) == 0) or int(cls_id) != 9:
                if time.time() - last_stop_time > 3:
                    doll_flag = True 
                    twist.linear.x = speed_control(cls_id, area)
            if doll_flag:
                twist.linear.x = speed_control(cls_id, area)
                twist.angular.z = output
            pub.publish(twist)


            print("fps: ",fps)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                twist.linear.x = 0.0
                twist.angular.z = 0
                pub.publish(twist)
                break
    finally:
        # Ensure resources are cleaned up before exiting
        rospy.loginfo("exit opencv_main")
        yolov5_wrapper.destroy()
        cap.release()
        cv2.destroyAllWindows()
        
        # No longer try to pop context directly
        # Let the system naturally clean up CUDA resources








