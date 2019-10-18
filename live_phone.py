import cv2

# add your ip address and port number
cap = cv2.VideoCapture('http://192.168.43.1:8084/video')

while(True):
    # read frame by frame
    ret, frame = cap.read()
    # display frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
