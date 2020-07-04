import cv2
import sqlite3
import numpy as np

fdetect =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("facedatabase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(Name)+" WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO People(ID,Name) Values("+str(Id)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id=input("Enter User Id:")
name=input("Enter Your Name:")
insertOrUpdate(id,name)
count=0
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=fdetect.detectMultiScale(gray,1.1,10)
    for(x,y,w,h,) in faces:
        count+=1
        cv2.imwrite("Face Datasets/User."+str(id)+"."+str(count)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray) 
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(count>20):
        break
cap.release()
cv2.destroyAllWindows()