# Developed By: Yuvashree S
# Register Number: 212223040251

import cv2
import matplotlib.pyplot as plt 
Gray_image=cv2.imread("/content/Screenshot 2025-09-27 133008.png")
plt.imshow(Gray_image)
plt.show()
Color_image=cv2.imread("/content/Screenshot 2025-09-27 133008.png")
plt.imshow(Color_image)
plt.show()
### code to find the histogram of gray scale image and color image channels.

hist = cv2.calcHist([Gray_image],[0],None,[256],[0,256])
plt.figure()
plt.title("Histogram")
plt.xlabel('gray_scale value')
plt.ylabel('pixel count')
plt.stem(hist)
plt.show()

# Display the histogram of gray scale image and any one channel histogram from color image

hist1 = cv2.calcHist([Color_image],[0],None,[256],[0,256]) 
plt.figure()
plt.title("Histogram")
plt.xlabel('color_scale value') 
plt.ylabel('pixel count')
plt.stem(hist1)
plt.show()

# Write the code to perform histogram equalization of the image.

equ1=cv2.equalizeHist(cv2.imread('/content/Screenshot 2025-09-27 133008.png',0)) 
equ=cv2.cvtColor(equ1,cv2.COLOR_BGR2RGB) 
plt.title("Equalised Image")
plt.axis("off")
plt.imshow(equ) 
plt.show()




