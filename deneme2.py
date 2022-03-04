# -- coding: utf-8 --



import cv2
import numpy as np
img=cv2.imread("ben.jpg")
img2=cv2.imread("gri.jpg")


cv2.imshow("Ben", img)

#Burada resmin boyutunu yazdırıyoruz.
print(img.shape)



#Üst kısımda görüntü işlemeyi yaptık. Bundan sonraki kısımda
#görüntüyü siyah beyaz yapacağız.

def griTonYap(img):
    #burda en,boy,ve katmana yüklediğimiz resmin en boy ve katman değerleri veriliyor.
    en,boy,katman=np.shape(img)
    newimg=np.zeros((en,boy,katman),dtype=np.uint8)
    
    for i in range(en):
        for j in range(boy):
            newimg[i:,j]=img[i,j,0]
            
    cv2.imshow("Yeni gri resim",newimg)
   





#Buradan aşağıda parlaklıkla oynama işlemleriyle
#çalışacağız
#2-a
def parlaklıklaOynaA(img,k):
    en,boy,katman=np.shape(img)
    newimg=np.zeros((en,boy,katman),dtype=np.uint8)
    for i in range(en):
        for j in range(boy):
            newimg[i:,j]=img[i,j]+k
    cv2.imshow("Yeni resim a",newimg)
    
    
#2-b
def parlaklıklaOynab(img,k):
    en,boy,katman=np.shape(img)
    newimg=np.zeros((en,boy,katman),dtype=np.uint8)
    
    for i in range(en):
        for j in range(boy):
            newimg[i:,j]=img[i,j]*k
            
    cv2.imshow("Yeni resim b",newimg)
    


#Gözü dikdörtgen içerisine alma

def BolgeSec(img):
    newimg=cv2.imread("gri.jpg")
    newimg2=cv2.rectangle(newimg, (330,420), (485,500), (100,200,255),3)
    cv2.imshow("Göz", newimg2)
    

griTonYap(img) 
parlaklıklaOynaA(img2, -50)
parlaklıklaOynab(img2,-5)
BolgeSec(img2)
    
cv2.waitKey()
cv2.destroyAllWindows()