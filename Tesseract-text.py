#!/usr/bin/env python
# coding: utf-8
# In[1]:
import pytesseract

# In[22]:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe

# In[3]:


import cv2


# In[37]:


img=cv2.imread('C:/Users/vknsr/Downloads/ML/Lab/images.jpg')


# In[41]:


cv2.imshow('rr',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[29]:


text=pytesseract.image_to_string(img)
print(text)


# In[5]:


import cv2
img=cv2.imread('C:/Users/vknsr/Downloads/ML/Lab/download.jpg')
cv2.imshow("hi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[26]:


import pytesseract
text=pytesseract.image_to_string(img)
print(text)


# In[12]:



img=cv2.imread('C:/Users/vknsr/Downloads/ML/Lab/download1.jpg')
cv2.imshow("hi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[25]:


text=pytesseract.image_to_string(img)
print(text)


# In[14]:


img=cv2.imread('C:/Users/vknsr/Downloads/ML/Lab/text.jpg')


# In[23]:


cv2.imshow("hi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[24]:


text=pytesseract.image_to_string(img)
print(text)


# In[ ]:




