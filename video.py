import pyttsx3
import pytesseract
import cv2
img = cv2.imread("C:/Users/vknsr/Downloads/ML/Lab/download.jpg")
cv2.imshow("hi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
text=pytesseract.image_to_string(img)
print(text)
text_speeech = pyttsx3.init()
answer = text
text_speeech.say(answer)
text_speeech.runAndWait()
