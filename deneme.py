# -- coding: utf-8 --



import cv2
import numpy as np
img=cv2.imread("ben.jpg")


cv2.imshow("Ben", img)

#Burda resmin boyutunu yazdırıyoruz.
print(img.shape)



#Üst kısımda görüntü işlemeyi yaptık. Bundan sonraki kısımda
#görüntüyü siyah beyaz yapacağız.

def griTonYap(img):
    en,boy,katman=np.shape(img)
    newimg=np.zeros((en,boy,katman),dtype=np.uint8)
    k=0.114 
    y=0.299
    x=0.587
    for i in range(en):
        for j in range(boy):
            newimg[i:,j]=img[i,j,0]*k+img[i,j,1]*x+img[i,j,2]*y
            
    cv2.imshow("Yeni gri resim",newimg)

griTonYap(img) 
cv2.imwrite('gri.jpg',img) 

cv2.waitKey()
cv2.destroyAllWindows() 

#Burdan aşağıda parlaklıkla oynama işlemleriyle
#çalışacağız