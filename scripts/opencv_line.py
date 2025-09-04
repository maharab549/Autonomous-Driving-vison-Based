import cv2
import numpy as np

# 需要保留的颜色的阈值
# 使用hsv.py获取
H_min = 20
H_max = 50
S_min = 0
S_max = 200
V_min =50
V_max = 255


HSV_Threshold = {'red_line': {'L': np.array([150, 100, 100]), 'H': np.array([200, 200, 255])}, # 红线
                 'crossing': {'L': np.array([80, 0, 200]), 'H': np.array([120, 40, 255])}, #人行道
                 'yellow': {'L': np.array([20, 0, 50]), 'H': np.array([50, 200, 255])}, #黄虚线
                 'green': {'L': np.array([20, 116, 113]), 'H': np.array([77, 255, 255])}, # 绿灯
                 'red': {'L': np.array([0, 43, 50]), 'H': np.array([9, 255, 255])}, } # 红灯

# 霍夫变换参数
rho = 1
theta = np.pi / 180
# 检测一条直线所需最少的曲线交点。
threshold = 50
# 线的最小长度。比这短的线段被拒绝
min_line_lenght = 38
# 线段之间的最大允许间隙，将它们视为一条线。
max_line_gap = 15

slope_max = 2.5
slope_min = 0.3

start_cnt = 0
road_width = 0

# 先看看效果，不行再加掩模


def line_preprocess(origin_img):
    # opencv读取就是BGR  转HSV
    hsv = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
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
    erode_img = cv2.erode(binary_img, kernel)
    # 膨胀
    dilate_img = cv2.dilate(erode_img, kernel)

    # 获取边界
    # line_img=cv2.Canny(erode_img)

    # cv2.imshow("frame",dilate_img)
    # 返回获取的车道图像
    return dilate_img



# 这个函数区别于line_preprocess 这个是专门处理赛道中其他需要识别的颜色要素
# 如 坡道红线，人行道白线，红绿灯等
# 第二个参数传入待识别的要素 如 'red_line'
#  返回要素面积大小用于判断
def element_preprocess(img,element,mask_roi):

    element_area = 0


    gs_frame = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯模糊

    hsv_image = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)

    # 滤去背景留下车道，二值化，把大于大的小于小的滤去
    binary_img = cv2.inRange(hsv_image, HSV_Threshold[element]['L'], HSV_Threshold[element]['H'])
    # 创建膨胀腐蚀核并进行膨胀腐蚀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    erode_img = cv2.erode(binary_img, kernel)
    dilate_img = cv2.dilate(erode_img, kernel)

    mask = np.zeros_like(dilate_img)
    cv2.fillPoly(mask, mask_roi, 255)

    mask_img  = cv2.bitwise_and(dilate_img ,mask)
    # cv2.imshow(element+'_img', mask_img)

    # 查找轮廓
    contours ,h= cv2.findContours(mask_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    len_cont = len(contours)


    if len_cont > 0:
        # cv2.imshow("img", img)
        for contour in contours:
            contours_img = cv2.drawContours(img, contour, -1, (0, 255, 0), 10)
            element_area += cv2.contourArea(contour)
        # cv2.imshow(element,contours_img)
    # if element == "yellow":
    #     if element_area < 500:
    #         element_area = 0
    print(element,"_area : ", element_area)
    return element_area





# def hough_tf(line_img,img):
    # lines = cv2.HoughLinesP(line_img, rho, theta, threshold, minLineLength=min_line_lenght, maxLineGap=max_line_gap)
    # if lines is not None:
    #     line_img = judge_lines(lines,line_img,img)
    # cv2.imshow("line_img", line_img)


def find_lines(line_img, img,yellow_flag):
    lines = cv2.HoughLinesP(line_img, rho, theta, threshold,
                            minLineLength=min_line_lenght, maxLineGap=max_line_gap)
    left_results, right_results, left_fit, right_fit = [], [], [], []
    if lines is not None:
        left_lines, right_lines = [], []
        drawing = np.zeros(
            (line_img.shape[0], line_img.shape[1], 3), dtype=np.uint8)
        for line in lines:
            for x1, y1, x2, y2 in line:
                if y1 != y2:
                    k = float(x1 - x2)/(y1 - y2)
                    if slope_max > abs(k) > slope_min:
                        if k > 0:
                            if k > 1.8 and yellow_flag > 1 :
                                continue
                            right_lines.append(line)
                        elif k < 0:
                            left_lines.append(line)
                    else:
                        continue
        if len(left_lines) > 0:
            clean_lines(left_lines, 0.1)
            left_points = [(x1, y1)
                           for line in left_lines for x1, y1, x2, y2 in line]
            left_points = left_points + [(x2, y2) for line in left_lines for x1, y1, x2, y2 in line]
            ymax, ymin = find_points(left_lines)
            left_results, left_fit = least_squares_fit(left_points, ymin, ymax)
            cv2.line(drawing, left_results[0],
                     left_results[1], (0, 0, 255), 10)
            cv2.putText(drawing, str(
                "left_k:%.2f" % left_fit[0]), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        if len(right_lines) > 0:
            clean_lines(right_lines, 0.1)
            right_points = [(x1, y1)
                            for line in right_lines for x1, y1, x2, y2 in line]
            right_points = right_points + [(x2, y2) for line in right_lines for x1, y1, x2, y2 in line]
            ymax, ymin = find_points(right_lines)
            right_results, right_fit = least_squares_fit(
                right_points, ymin, ymax)
            cv2.line(drawing, right_results[0],
                     right_results[1], (0, 255, 0), 10)
            cv2.putText(drawing, str("right_k:%.2f" % right_fit[0]), (
                160, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        line_img = cv2.addWeighted(img, 0.5, drawing, 0.5, 0)
        # cv2.imshow("line_img", line_img)
    return line_img, left_results, right_results, left_fit, right_fit


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


def how_to_turn(line_roi, left_results, right_results, left_fit, right_fit):
    height = line_roi.shape[0]
    width = line_roi.shape[1]
    middle_line = width/2
    # [(xmin, ymin), (xmax, ymax)]

    global  road_width
    global  start_cnt
    # error>0  右转
    # 两条线都有
    if len(left_results) > 0 and len(right_results) > 0:
        if start_cnt < 10:
            start_cnt +=1
            road_width += (right_results[1][0]+right_results[0][0])/2-(left_results[1][0]+left_results[0][0])/2
            if start_cnt == 10:
                road_width /=10
        # X = (left_results[1][0] + right_results[1][0]) / 2
        X = (left_fit[0]*height/2+left_fit[1]+right_fit[0]*height/2+right_fit[1])/2
        if abs(left_results[1][1]-right_results[1][1])<20:
            X1 = (left_results[1][0] + right_results[1][0]) / 2
            X = (X+X1)/2
        middle_line = X
        rho = -(middle_line - width / 2)
        # if -15 < rho < 15:
        #     rho = 0
    # 只有右线-----左转
    elif len(left_results) == 0 and len(right_results) > 0:
        if start_cnt!=10:
            road_width = 156
        X_top = right_results[0][0]
        X_bottom = (height - right_results[0][1]) * (right_results[0][0] - right_results[1][0])/(
            right_results[0][1] - right_results[1][1]) + right_results[0][0]
        # X = (X_top - 10) / 2 + (X_bottom - width) / 2
        X = (X_top+X_bottom)/2
        middle_line = X - road_width/2 
        # 弯道
        # if right_fit[0] >= 1.3:
        # rho  = width/2-middle_line
        # 直道丢线
        # else:
        rho = width/2-middle_line

    # 只有左线-----右转
    elif len(right_results) == 0 and len(left_results) > 0:
        if start_cnt!=10:
            road_width = 156
        X_top = left_results[0][0]
        X_bottom = (height - left_results[0][1]) * (left_results[0][0] - left_results[1][0])/(
            left_results[0][1] - left_results[1][1]) + left_results[0][0]
        # X = (X_top + 10) / 2 + (X_bottom + width) / 2
        X = (X_top+X_bottom)/2
        middle_line = X+road_width/2
        # 弯道
        # if left_fit[0] <= -1.3:
            # rho = -middle_line 
         # 直道丢线
        # else:
        rho = width/2 - middle_line
            
    else:
        rho = 0
    print("middle_line: ", middle_line)
    # cv2.line(line_roi, (middle_line,105),(middle_line,0), (0, 255, 255), 5)
    if start_cnt == 10:
        print("road_width: ",road_width)
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


def tuple_transform(left_results,right_results):
    A_x = left_results[1][0]
    A_y = left_results[1][1]
    B_x = left_results[0][0]
    B_y = left_results[0][1]
    C_x = right_results[0][0]
    C_y = right_results[0][1]
    D_x = right_results[1][0]
    D_y = right_results[1][1]

    offset = 20

    return (A_x + offset ,A_y),(B_x + int(offset/2),B_y),(C_x ,C_y),(D_x ,D_y)


if __name__ == "__main__":
    # cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
    cap = cv2.VideoCapture(0)

    while True:
        # 摄像头640x480  w*h
        ret, img = cap.read()
        if not ret:
            continue
        # print(img.shape)
        line_roi = line_preprocess(img)
        line_img, left_results, right_results, left_fit, right_fit = find_lines(
            line_roi, img)
        error = how_to_turn(line_roi, left_results,
                            right_results, left_fit, right_fit)
        cv2.imshow("line_img", line_img)
        print(error)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
