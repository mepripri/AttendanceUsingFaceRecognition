import cv2
import numpy as np
import os 

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
id = 0

names = ['None', 'Priyal', 'Heli', 'Simran', 'Nilesh Sir', 'W']
cam = cv2.VideoCapture(0)
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors = 5,minSize = (int(minW), int(minH)))
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # If confidence is less then 100 ==> "0" : perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(img,str(id),(x+5,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        cv2.putText(img,str(confidence),(x+5,y+h-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1)  
    cv2.imshow('Recognition',img) 
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()