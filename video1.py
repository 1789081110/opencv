import numpy as np
import cv2

cap = cv2.VideoCapture(0) #web-camera 
while True:
    ret, frame = cap.read() #the video starts reading
    width = int(cap.get(3))
    height = int(cap.get(4))
    image = np.zeros(frame.shape, np.uint8)
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(small_frame, cv2.ROTATE_180) #create 4 video images together first is rotated to 180 degree
    image[height // 2:, :width // 2] = small_frame #all other remaining videos are displayed
    image[:height // 2, width // 2:] = small_frame
    image[height // 2:, width // 2:] = small_frame

    cv2.imshow('frame', image) #video is displayed on the screen
    if cv2.waitKey(1) == ord('q'): #after pressing q it ends
        break
cap.release()
cv2.destroyAllWindows()

