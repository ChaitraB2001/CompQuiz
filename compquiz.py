import numpy
import cv2
import mymodule
mymodule.welcome()
a=0

img=cv2.imread("intro.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img=cv2.imread("intro2.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img=cv2.imread("prank.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img=cv2.imread("cat.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
q1=input("enter your answer here:")
if q1=="C":
    print("CORRECT ANS")
    a=a+1
else:
    print("WRONG ANSWER")
img=cv2.imread("kermit.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
q2=input("enter your answer here:")
if q2=="C":
    print("CORRECT ANSWER")
    a=a+1
else:
    print("WRONG ANSWER")
img=cv2.imread("pigeon.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
q3=input("enter your answer here:")
if q3=="B":
    print("CORRECT ANSWER")
    a=a+1
else:
    print("WRONG ANSWER")
img=cv2.imread("cheetoh.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
q4=input("enter your answer here:")
if q4=="B":
    print("CORRECT ANSWER")
    a=a+1
else:
    print("WRONG ANSWER")
img=cv2.imread("final.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('your score is',a)




    








             
          
    
   
        
    
