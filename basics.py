import cv2
image = cv2.imread('img.jpg', 0) #for reading an image file

img=cv2.resize(image, (500, 500)) #resizing them if they are too large

img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #rotating them in 90 degree

cv2.imshow('Image', img) #displaying the image

cv2.waitKey(0) #press any key to close the image

cv2.destroyAllWindows()


cv2.imwrite('img_1.jpg', img) #creating a new image file with the exiting one
