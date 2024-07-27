
import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Kha\OneDrive\Desktop\loppython\picture\img\nhung-cung-duong-di-lagi-gan-nhat-voi-moi-phuong-tien-3.jpg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(blur, 10, 150)


height = img.shape[0]
a= int(height*1.0/1.5)    
polygons = np.array([
         [(0, height), (300, a), (600, height)]   
    ])
mask = np.zeros_like(canny)
cv2.fillPoly(mask, polygons, 255)
masked_image = cv2.bitwise_and(canny, mask)


line_img=np.zeros_like(img)
lines=cv2.HoughLinesP(masked_image, 2, np.pi/180, 100, minLineLength=40, maxLineGap=5)
if lines is not None:
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 5)
    

result=cv2.bitwise_and(img,line_img )
a= cv2.addWeighted(img, 1, line_img, 1, 1)



#print("lines", lines)
#cv2.imshow('2', line_img)
#cv2.imshow('0', canny)
#cv2.imshow('1', masked_image)
cv2.imshow('000', result)
cv2.imshow('111', a)

print('chieu cao anh', a)
print(polygons)
cv2.waitKey(0)
cv2.destroyAllWindow()

