import  cv2
import  numpy as np
import  time
from new_main import  HoughLines,line_preprocess,draw_lines
#
# mask_points = np.array([[(0, 70),(0, 60), (60, 0), (170, 0),(240, 60), (240, 70)]])
# mask = np.zeros((70,240), dtype=np.uint8)
# cv2.fillPoly(mask,mask_points,255)
# cv2.imshow("mask",mask)
# cv2.waitKey(0)

# atime = [0,0]
# bgr = cv2.imread("1.jpg")
# bgr = cv2.resize(bgr,(1000,500))
# cv2.imshow("bgr",bgr)
#
#
# hsv = cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)
# #
# atime[0] = time.time()
# h = hsv[:,:,0]
# s = hsv[:,:,1]
# v = hsv[:,:,2]
# atime[1] = time.time()
# print(atime[1]- atime[0])
#
#
#
# # atime[0] = time.time()
# # sh,ss,sv = cv2.split(hsv)
# # atime[1] = time.time()
# # print(atime[1]- atime[0])
#
# ev = cv2.equalizeHist(v)
#
#
# # atime[0] = time.time()
# # new = cv2.merge([h,s,ev])
# # atime[1] = time.time()
# # print(atime[1]- atime[0])
#
# atime[0] = time.time()
# new2 = np.stack((h,s,ev),axis=2)
# atime[1] = time.time()
# print(atime[1]- atime[0])
#
# # new = cv2.cvtColor(new,cv2.COLOR_HSV2BGR)
# new2 = cv2.cvtColor(new2,cv2.COLOR_HSV2BGR)
# #
# # cv2.imshow("hsv",hsv)
# # cv2.imshow("new",new)
# cv2.imshow("new2",new2)
# # cv2.imshow("v",v)
# # cv2.imshow("ev",ev)
# cv2.waitKey(0)


if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.25)
    cap.set(cv2.CAP_PROP_EXPOSURE,-7.5)
    while True:
        ret,img = cap.read()
        if not ret:
            continue
        img = cv2.resize(img, (320, 240), interpolation=cv2.INTER_AREA)
        line_img = cv2.resize(img, (240, 180), interpolation=cv2.INTER_AREA)
        line_img = line_img[110:180, :, :]
        min_line_lenght = 15
        line_roi = line_preprocess(line_img)
        left_results, right_results, left_fit, right_fit = HoughLines(line_roi)
        draw_lines(line_img, left_results, right_results, left_fit, right_fit)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
