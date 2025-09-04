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
# 添加PyCUDA导入以解决上下文清理问题
import pycuda.driver as cuda


# 需要保留的颜色的阈值
# 使用hsv.py获取
H_min = 20#20
H_max = 80
S_min = 80 #80,78   46反光调小，但是会把其他识别成线
S_max = 255
V_min = 40 #40
V_max = 255
# 变道时红色边线阈值
H_min_2 = 140
H_max_2 = 190
S_min_2 = 50#78   46反光调小，但是会把其他识别成线
S_max_2 = 255
V_min_2 = 40
V_max_2 = 255


HSV_Threshold = {'red_line': {'L': np.array([150, 100, 100]), 'H': np.array([200, 200, 255])}, # 红线
                 'crossing': {'L': np.array([80, 0, 200]), 'H': np.array([120, 40, 255])}, #人行道
                 'yellow': {'L': np.array([15, 50, 50]), 'H': np.array([35, 255, 255])}, #黄虚线
                 'green': {'L': np.array([50, 70, 40]), 'H': np.array([70, 255, 255])}, # 绿灯
                 'red': {'L': np.array([170, 70, 40]), 'H': np.array([190, 255, 255])}, } # 红灯
# RGB_Threshold = { 
#                 'green': {'L': np.array([50, 54, 40]), 'H': np.array([90, 255, 255])}, # 绿灯
#                 'red': {'L': np.array([150, 90, 40]), 'H': np.array([180, 190, 255])}, # 红灯  255 73 134
#                 } 

# R_min = 0
# G_min = 56
# B_min = 0
# R_max =48
# G_max =255
# B_max =255
# 霍夫变换参数
rho = 1
theta = np.pi / 180
# 检测一条直线所需最少的曲线交点。
threshold = 50
# 线的最小长度。比这短的线段被拒绝
min_line_lenght = 40
# 线段之间的最大允许间隙，将它们视为一条线。
max_line_gap = 20
#斜率限制
slope_max = 3.0 ##2.7
slope_min = 0.3

start_cnt = 0
road_width = 0#路宽


side_walk_flag = True#人行道状态
speed_limit_flag = True#限速状态
speed_flag = True#解除限速状态
turn_flag = True#转弯是否完成
turn_flag_2 = True
turn_left_flag = True#左转状态
turn_right_flag = True#右转
speed_4_flag = False#控制限速
clean_flag = True

change_flag = True#变道
change_flag_2 = False#变道左右边线筛选
change_flag_3 = True
change_flag_4 = True

clean_right_flag = True#限速右边线清理
red_light_flag = True#红灯标志
red_light_area = 0#红灯面积
green_light_flag = True#绿灯标志
green_light_area = 0#绿灯面积
traffic_flag = True#红绿灯状态
traffic_flag_2 = True

# ========== PROGRESSIVE DANGER DETECTION SYSTEM ==========
# TUNING PARAMETERS - MODIFY THESE VALUES TO TUNE BEHAVIOR:
DANGER_DETECTION_THRESHOLD = 370         # 初始危险检测阈值 - 开始监控危险
DANGER_ACTION_THRESHOLD = 1200           # 危险行动阈值 - 开始左转避让
DANGER_GENTLE_LEFT_FORCE = 195            # 温和左转力度 (30% of normal turn) - 调整此值改变避让幅度
DANGER_AVOIDANCE_SPEED = 0.30            # 危险避让时速度 - 稍微减速但继续前进
DANGER_RECOVERY_TIME = 195.0               # 危险恢复时间(秒) - 避让后恢复正常的时间

# 危险检测状态变量
danger_detected = False                  # 是否检测到危险
danger_avoidance_active = False          # 是否正在进行危险避让
danger_start_time = 0                    # 危险避让开始时间
current_danger_area = 0                  # 当前危险区域面积

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
    # opencv读取就是BGR  转HSV
    hsv = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
    # h = hsv[:,:,0]
    # s = hsv[:,:,1]
    # v = hsv[:,:,2]
    # ev = cv2.equalizeHist(v)
    # new_hsv = np.stack((h,s,ev),axis=2)
    # 把背景滤掉，里面的数字是需要留下的颜色的HSV的色域，需要自己找出来
    lower_color = np.array([H_min, S_min, V_min])
    higher_color = np.array([H_max, S_max, V_max])
    # 滤去背景留下车道，二值化，把大于大的小于小的滤去
    binary_img = cv2.inRange(hsv, lower_color, higher_color)
    # # 高斯模糊滤波
    # gs_img = cv2.GaussianBlur(binary_img, (5, 5), 0)
    # 创建腐蚀膨胀核，3*3矩形对二值化图像进行先膨胀再腐蚀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # 腐蚀
        
    erode_img = cv2.erode(binary_img, kernel,iterations=1)
    # 膨胀
    dilate_img = cv2.dilate(erode_img, kernel,iterations=2)

    # 获取边界
    # line_img=cv2.Canny(erode_img)

    # cv2.imshow("frame",dilate_img)
    # 返回获取的车道图像
    return dilate_img

def line_preprocess_2(origin_img):
    # opencv读取就是BGR  转HSV
    hsv = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
    # h = hsv[:,:,0]
    # s = hsv[:,:,1]
    # v = hsv[:,:,2]
    # ev = cv2.equalizeHist(v)
    # new_hsv = np.stack((h,s,ev),axis=2)
    # 把背景滤掉，里面的数字是需要留下的颜色的HSV的色域，需要自己找出来
    lower_color = np.array([H_min_2, S_min_2, V_min_2])
    higher_color = np.array([H_max_2, S_max_2, V_max_2])
    # 滤去背景留下车道，二值化，把大于大的小于小的滤去
    binary_img = cv2.inRange(hsv, lower_color, higher_color)
    # # 高斯模糊滤波
    # gs_img = cv2.GaussianBlur(binary_img, (5, 5), 0)
    # 创建腐蚀膨胀核，3*3矩形对二值化图像进行先膨胀再腐蚀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # 腐蚀
    erode_img = cv2.erode(binary_img, kernel,iterations=1)
    # 膨胀
    dilate_img = cv2.dilate(erode_img, kernel,iterations=2)

    # 获取边界
    # line_img=cv2.Canny(erode_img)

    # cv2.imshow("frame_2",dilate_img)
    # 返回获取的车道图像
    return dilate_img

# 这个函数区别于line_preprocess 这个是专门处理赛道中其他需要识别的颜色要素
# 如 坡道红线，人行道白线，红绿灯等
# 第二个参数传入待识别的要素 如 'red_line'
#  返回要素面积大小用于判断
def element_preprocess(img,element):

    


    blur_frame = cv2.medianBlur(img, 7)  
    hsv_image = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow("rgb_image",rgb_image)

    # 滤去背景留下车道，二值化，把大于大的小于小的滤去
    binary_img = cv2.inRange(hsv_image, HSV_Threshold[element]['L'], HSV_Threshold[element]['H'])
    # binary_img = cv2.inRange(rgb_image, np.array([R_min, G_min,B_min ]), np.array([  R_max,G_max,B_max])) 
    # cv2.imshow("binary_img", binary_img)

    # 创建膨胀腐蚀核并进行膨胀腐蚀
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

    # 查找轮廓
    # 修复: 在新版OpenCV中，findContours只返回两个值而不是三个
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
                            if (k > 0.2 and clean_right_flag == False) or (k > 0.2 and change_flag == False and change_flag_2 == False):#限速时去掉右线 变道时去掉右线，变道结束恢复
                                continue
                            if (x1>x2 and x1<120) or (x2>x1 and x2<120):
                                continue
                            right_lines.append(line)
                                # right_lines.pop(line)
                        elif k < 0:
                            if k > -1.4 and change_flag == False and change_flag_2 == False: #变道时筛选左线，变道结束恢复
                                continue
                            if (x1>x2 and x2>120) or (x2>x1 and x1>120):
                                continue
                            # midpoint_x = (x1 + x2) / 2
                            # distance_to_center = abs(midpoint_x - 120)  # 假设center_x是中心线的x坐标
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
    # 最小二乘法拟合
    x = [p[0] for p in point_list]
    y = [p[1] for p in point_list]
    # polyfit第三个参数为拟合多项式的阶数，所以1代表线性
    # 这是反过来输入的所以竖直时K=0
    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)  # 获取拟合的结果
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
    渐进式危险避让控制函数
    返回: (steering_adjustment, speed_adjustment, status_message)
    """
    global danger_avoidance_active, danger_start_time, current_danger_area
    
    # 如果没有检测到危险，返回正常控制
    if not danger_detected:
        return 0, 0, "NORMAL"
    
    # 如果危险面积小于行动阈值，继续前进但监控
    if current_danger_area < DANGER_ACTION_THRESHOLD:
        return 0, 0, f"MONITORING - Area: {current_danger_area}"
    
    # 危险面积达到行动阈值，开始温和左转避让
    if not danger_avoidance_active:
        danger_avoidance_active = True
        danger_start_time = time.time()
        print(f"�� DANGER AVOIDANCE ACTIVATED - Area: {current_danger_area} > {DANGER_ACTION_THRESHOLD}")
    
    current_time = time.time()
    elapsed_time = current_time - danger_start_time
    
    # 在恢复时间内进行温和左转
    if elapsed_time <= DANGER_RECOVERY_TIME:
        # 计算渐进式恢复 - 开始时左转力度最大，逐渐减小
        recovery_factor = max(0, 1.0 - (elapsed_time / DANGER_RECOVERY_TIME))
        steering_adjustment = DANGER_GENTLE_LEFT_FORCE * recovery_factor
        
        status = f"GENTLE LEFT TURN - Force: {steering_adjustment:.1f}, Time: {elapsed_time:.1f}s"
        return steering_adjustment, 0, status
    
    # 恢复时间结束，重置状态
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
    
    # error>0  右转
    # 两条线都有
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
    # 只有右线-----左转
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
        middle_line = X - road_width / 2
        # 弯道
        # if right_fit[0] >= 1.3:
        # rho  = width/2-middle_line
        # 直道丢线
        # else:
        rho = width / 2 - middle_line
        rho = abs(rho)
        if change_flag_3 == False and change_flag_4:
            rho = 0
        # if danger_flag == False:
        #     rho = 40

    # 只有左线-----右转
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
        # 弯道
        # if left_fit[0] <= -1.3:
        # rho = -middle_line
        # 直道丢线
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
    # 获取危险避让的转向调整
    steering_adjustment, speed_adjustment, status = progressive_danger_control()
    
    if steering_adjustment != 0:
        # 应用温和的左转调整，但不完全覆盖正常转向
        rho += steering_adjustment
        print(f"DANGER STEERING ADJUSTMENT: +{steering_adjustment} -> Total rho: {rho}")
    
    if status != "NORMAL":
        print(f"DANGER STATUS: {status}")
    # ============================================================
    
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
    # 迭代计算斜率均值，排除掉与差值差异较大的数据
    slope = [(y2 - y1) / (x2 - x1)
             for line in lines for x1, y1, x2, y2 in line]
    while len(lines) > 0:
        # 斜率平均值
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



# 速度控制函数，根据检测到的交通标志(cls_id)及其面积(area)调整车辆速度
def speed_control(cls_id ,area):
    # 声明所有使用的全局变量（用于在不同函数调用间保持状态）
    global side_walk_flag        # 人行道标志状态
    global side_time             # 人行道计时器 [开始时间, 当前时间]
    global speed_limit_flag      # 限速标志状态
    global speed_flag            # 解除限速标志状态
    global turn_left_flag        # 左转标志状态
    global turn_right_flag       # 右转标志状态
    global turn_flag             # 转弯主标志
    global turn_flag_2           # 转弯辅助标志
    global red_light_flag        # 红灯标志状态
    global red_light_area        # 红灯检测面积
    global green_light_flag      # 绿灯标志状态
    global green_light_area      # 绿灯检测面积
    global danger_flag           # 危险标志状态
    global danger_flag_2         # 危险第二阶段标志
    global danger_flag_3         # 危险第三阶段标志
    global danger_time           # 危险区域计时器 [开始时间, 当前时间]
    global speed_4_flag          # 限速4标志（特定限速）
    global yolo_flag             # YOLO检测开关
    global traffic_flag          # 交通灯主标志
    global traffic_flag_2        # 交通灯辅助标志
    global speed                 # 当前速度值
    global clean_right_flag      # 清除右侧标志
    global clean_time            # 清除计时器 [开始时间, 当前时间]
    global clean_flag            # 清除标志状态
    global delayed_stop_flag     # 延迟停止标志
    global delayed_stop_time     # 延迟停止时间点
    global doll_flag             # 玩偶标志（未使用）
    global last_stop_time        # 上次停止时间（未使用）
    global stop_time             # 停车计时器 [开始时间, 当前时间]
    global turn_time             # 转弯计时器 [开始时间, 当前时间]
    global change_flag           # 变道标志
    global change_flag_2         # 变道第二阶段标志
    global change_flag_3         # 变道第三阶段标志
    global change_flag_4         # 变道第四阶段标志
    global change_time           # 变道计时器 [开始时间, 当前时间]
    global traffic_time          # 交通灯计时器 [开始时间, 当前时间]
    global speed_x               # 基础速度值
    
    # ========== PROGRESSIVE DANGER DETECTION ==========
    global danger_detected, current_danger_area
    
    # 重置危险检测状态
    danger_detected = False
    current_danger_area = 0
    
    # 检测危险标志 - 渐进式逻辑
    if int(cls_id) == 0 and area > DANGER_DETECTION_THRESHOLD:
        danger_detected = True
        current_danger_area = area
        
        if area < DANGER_ACTION_THRESHOLD:
            print(f"⚠️  DANGER DETECTED - MONITORING: Area {area} < {DANGER_ACTION_THRESHOLD} (continue forward)")
        else:
            print(f"�� DANGER CLOSE - AVOIDANCE: Area {area} >= {DANGER_ACTION_THRESHOLD} (gentle left turn)")
    
    # 检查是否需要危险避让速度调整
    _, speed_adjustment, status = progressive_danger_control()
    if "GENTLE LEFT TURN" in status:
        # 在危险避让期间稍微减速，但继续前进
        pass  # 速度调整在下面的正常逻辑中处理
    # ================================================
    
    # 逻辑1：检测到左转标志(4)且面积足够大
    if turn_left_flag and turn_right_flag and int(cls_id) == 4 and area > 1100:
        turn_left_flag = False  # 关闭左转标志
        turn_time[0] = time.time()  # 记录转弯开始时间
    
    # 逻辑2：检测到右转标志(5)且面积足够大
    elif turn_right_flag and turn_left_flag and int(cls_id) == 5 and area > 1100:
        turn_right_flag = False  # 关闭右转标志
        turn_time[0] = time.time()  # 记录转弯开始时间
    
    # 逻辑3：检测到人行道标志(1)且面积足够大（转弯后）
    elif side_walk_flag and int(cls_id) == 1 and turn_flag == False and area >= 1300:
        side_walk_flag = False  # 关闭人行道标志
        stop_time[0] = time.time()  # 开始停车计时
        side_time[0] = time.time()  # 开始人行道计时
    
    # 逻辑4：检测到限速标志(3)且面积足够大
    elif speed_limit_flag and int(cls_id) == 3 and side_walk_flag == False and area > 780:
        speed_limit_flag = False  # 关闭限速标志
        clean_right_flag = False  # 禁用右侧清除
        speed_4_flag = True      # 启用限速4模式
        clean_flag = False       # 清除标志复位
        clean_time[0] = time.time()  # 开始清除计时
    
    # 逻辑5：检测到解除限速标志(2)且面积足够大
    elif speed_flag and int(cls_id) == 2 and speed_limit_flag == False and area > 850:
        speed_flag = False  # 关闭解除限速标志
    
    # 逻辑6：交通灯处理（限速结束后）
    elif traffic_flag and speed_flag == False:
        traffic_flag_2 = False  # 关闭辅助交通标志
        # 红灯检测（红灯面积大于绿灯+阈值）
        if speed_flag == False and red_light_flag and (red_light_area > green_light_area+100  and red_light_area > 900):
            red_light_flag = False  # 关闭红灯标志
            delayed_stop_time = time.time() + 0.45  # 设置延迟停止时间点
            traffic_time[0] = time.time()  # 开始交通灯计时
        # 绿灯检测（绿灯面积大于红灯+阈值）
        elif red_light_flag == False and green_light_flag and (green_light_area > red_light_area+100  and green_light_area > 350):
            green_light_flag = False  # 关闭绿灯标志
            traffic_flag = False      # 关闭交通灯主标志
            yolo_flag = True          # 启用YOLO检测
        # 交通灯超时处理（超过5秒直接通行）
        elif traffic_time[1]-traffic_time[0] > 5:
            traffic_flag = False  # 关闭交通灯主标志
            yolo_flag = True      # 启用YOLO检测
    
    # 逻辑7：检测到变道标志(6)且面积足够大
    elif traffic_flag == False and change_flag and int(cls_id) == 6 and area > 370:
        change_flag = False  # 关闭变道标志
        change_time[0]=time.time()  # 开始变道计时
    
    # 逻辑8：检测到危险标志(0)且面积足够大
   # elif change_flag == False and danger_flag and int(cls_id)== 0 and area > 370:
    #   danger_flag = False  # 关闭危险标志
       # danger_time[0] = time.time()  # 开始危险区域计时



    # 停车控制逻辑
    if stop_time[0]!=-1:
        speed = 0.0  # 立即停车
        stop_time[1] = time.time()  # 更新停车结束时间
    
    # 停车结束后的速度控制逻辑
    if stop_time[0] == -1  or stop_time[1]-stop_time[0] > 2:  # 停车结束或超过2秒
        # ========== DANGER AVOIDANCE SPEED CONTROL ==========
        # 如果正在进行危险避让，使用危险避让速度
        if danger_avoidance_active:
            speed = DANGER_AVOIDANCE_SPEED
            print(f"DANGER AVOIDANCE SPEED: {speed}")
        # ===================================================
        # 限速4模式（0.28速度）
        elif speed_4_flag:
            speed = 0.25
            if speed_flag == False:  # 解除限速后退出该模式
                speed_4_flag = False
        # 初始转弯速度（0.3）
        elif (turn_left_flag == True and turn_right_flag == True) and turn_flag:
            speed = 0.2
        # 转弯中速度（0.3）
        elif turn_flag:
            speed = 0.2 
        # 转弯结束到人行道阶段（0.3）
        elif turn_flag_2 == False and side_walk_flag:
            speed = 0.3
        # 转弯结束到人行道过渡阶段（0.4）
        elif turn_flag == False and turn_flag_2 and side_walk_flag:
            speed = 0.3
        # 人行道到限速阶段（0.38）
        elif side_walk_flag == False and speed_limit_flag:
            speed = 0.35
        # 解除限速到红绿灯阶段（0.33）
        elif speed_flag == False and red_light_flag:
            speed = 0.20
        # 红灯停车控制
        elif traffic_flag and red_light_flag == False and green_light_flag and time.time() >= delayed_stop_time:
            speed = 0.0  # 完全停车
            traffic_time[1] = time.time()  # 更新交通灯结束时间
        # 变道准备阶段（0.18低速）
        elif traffic_flag == False and change_flag:
            speed = 0.18
        # 变道后阶段（0.3）
        elif change_flag == False and change_flag_4:
            speed = 0.3
        # 危险区域前阶段（0.3）
        elif change_flag_4 == False and danger_flag:
            speed = 0.3
        # 危险区域中阶段（0.2低速）
        elif danger_flag == False and danger_flag_2:
            speed = 0.2
        # 默认行驶速度（0.4）
        elif danger_flag == False and danger_flag_2 == False:
            speed = 0.4
        # 保底速度（使用外部定义的speed_x）
        else:
            speed = speed_x
        
        # 重置停车计时器
        stop_time = [-1,-1]
        
        # 转弯时间控制
        if turn_time[0] != 0 and (turn_left_flag == False or turn_right_flag == False):
            turn_time[1] = time.time()
            if turn_time[1]-turn_time[0] > 1.2:  # 1.2秒后关闭主转弯标志
                turn_flag = False
            if turn_time[1]-turn_time[0] > 4.2:  # 4.2秒后关闭辅助转弯标志
                turn_flag_2 = False
        
        # 变道时间控制
        if change_time[0] != 0 and change_flag == False:
            change_time[1] = time.time()
            if change_time[1] - change_time[0] > 1.7:  # 1.7秒后进入第二阶段
                change_flag_2 = True
            if change_time[1] - change_time[0] > 3.8:  # 3.8秒后关闭第三阶段
                change_flag_3 = False
            if change_time[1] - change_time[0] > 4.5:  # 4.5秒后关闭第四阶段
                change_flag_4 = False
        
        # 危险区域时间控制
        if danger_time[0] != 0 and danger_flag == False:
            danger_time[1] = time.time()
            if danger_time[1] - danger_time[0] > 0.476:  # 0.476秒后关闭第二阶段
                danger_flag_2 = False
            if danger_time[1] - danger_time[0] > 1.5:   # 1.5秒后关闭第三阶段
                danger_flag_3 = False
                danger_time = [0,0]  # 重置计时器
        
        # 清除操作时间控制
        if clean_time[0] !=0 and clean_flag == False:
            clean_time[1] = time.time()
            if clean_time[1] - clean_time[0] > 4:  # 4秒后启用右侧清除
                clean_right_flag = True
            if clean_time[1] - clean_time[0] > 6:  # 6秒后重置计时器
                clean_time = [0,0]
        
        # 人行道时间控制
        if side_time[0] !=0 and side_walk_flag == False:
            side_time[1] = time.time()
            if side_time[1]-side_time[0] > 6:  # 6秒后重置计时器
                side_time = [0,0]
    
    # 打印当前速度并返回
    print("speed: ",speed)
    return speed


def switch_callback(msg):
    global EN
    EN = msg.data

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

    # 初始化CUDA
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
                
                if change_flag == False:#变道状态时右边线红色处理
                    line_roi_2 = line_preprocess_2(line_img_2)
                    line_roi = cv2.bitwise_or(line_roi,line_roi_2)#右边线与左边线合并
                if (turn_flag_2 == False and side_walk_flag ) or change_flag == False :
                    slope_max = 5
                else:
                    slope_max = 3.0
                line_roi = cv2.bitwise_and(line_roi,mask)
                line_shape = line_img.shape
                cv2.imshow("frame",line_roi)
                left_results, right_results, left_fit, right_fit = HoughLines(line_roi)
                error = how_to_turn(line_shape,left_results , right_results, left_fit, right_fit)
                if speed == 0.0 :
                    error = 0
                # if speed_flag == False and traffic_flag :
                #     if error <= -50 :
                #         error = -50
                print("error:",error)
                if change_flag == False and change_flag_2 == False :
                    Servo_Kp = 0.014
                    Servo_Turn_Kp = 0.021
                    Kd = 0.065# 0.057
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
                # 必须把绿灯放前面，否则绿灯面积会累加，未知BUG
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
        # 确保在退出前清理资源
        rospy.loginfo("exit opencv_main")
        yolov5_wrapper.destroy()
        cap.release()
        cv2.destroyAllWindows()
        
        # 不再尝试直接pop context
        # 让系统自然清理CUDA资源


