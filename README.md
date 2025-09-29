# Exp-03  Histogram-of-an-images

# Name : Yuvashree S
# Register Number: 212223040251

## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Read the gray and color image using imread()

### Step2:
Print the image using imshow().



### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### step4:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step5:
The Histogram of gray scale image and color image is shown.


## Program:
```python

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





```
## Output:
### Input Grayscale Image and Color Image
<img width="467" height="267" alt="image" src="https://github.com/user-attachments/assets/b709dff6-9219-472c-8936-8e1920022af9" />

<img width="545" height="320" alt="image" src="https://github.com/user-attachments/assets/0e1454b3-213f-4f86-95a2-e00c07ebefae" />

### Histogram of Grayscale Image and any channel of Color Image
<img width="567" height="420" alt="image" src="https://github.com/user-attachments/assets/4bd21462-df77-4636-b30c-ec7faa0c71d9" />
<img width="582" height="413" alt="image" src="https://github.com/user-attachments/assets/8634f55d-074b-49c6-93e4-47803938e308" />



### Histogram Equalization of Grayscale Image.
<img width="522" height="317" alt="image" src="https://github.com/user-attachments/assets/b1aefa70-b8a9-4c87-843f-c7bfcdf0e725" />




## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
