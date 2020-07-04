import cv2
import numpy as np
import sqlite3

faceDetect =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('trainingData.yml')
path='Face Datasets'
id=0

def getProfile(id):
    conn=sqlite3.connect("facedatabase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h,) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        print (conf)
        profile=getProfile(id)
        conn=sqlite3.connect("facedatabase.db")
        cmd='UPDATE People SET Attendance="P" WHERE ID='+str(id)
        conn.execute(cmd)
        conn.commit()
        conn.close()
        if(profile!=None):
            cv2.putText(img,str(profile[1]),(x,y+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow("Face",img)
    if(cv2.waitKey(1)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()