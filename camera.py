import cv2

def main():
    # 打开默认摄像头（通常是 0）
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("无法打开摄像头")
        exit()

    while True:
        # 读取一帧图像
        ret, frame = cap.read()

        if not ret:
            print("无法获取帧，请检查摄像头是否正常工作")
            break

        # 显示图像
        cv2.imshow('Camera Stream', frame)

        # 按 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头资源
    cap.release()

    # 关闭所有窗口
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
