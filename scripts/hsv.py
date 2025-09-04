import cv2

# 实时获取视频的HSV值，鼠标左键点击图像上的点即可
def getpos(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 定义一个鼠标左键按下去的事件
        print(HSV[y, x])

if __name__=="__main__":
    cap = cv2.VideoCapture(0,cv2.CAP_V4L2)
    while True:
        ret,img=cap.read()
        img = cv2.resize(img, (320, 240), interpolation=cv2.INTER_AREA)
        frame = img[:192, :320, :]
        frame = cv2.resize(frame,(192,144),cv2.INTER_AREA)
        if not ret:
            continue
        #HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("img", img)
        cv2.imshow("frame", frame)
        #cv2.setMouseCallback("imageHSV", getpos)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


