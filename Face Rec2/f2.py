import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
path='Face Datasets'

def getImageWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        #print (faceImg.mode)
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("Training",faceNp)
        cv2.waitKey(10)
    return np.array(IDs),faces

Ids,faces=getImageWithID(path)
recognizer.train(faces,Ids)
recognizer.save('trainingData.yml')
print("Model Trained")
cv2.destroyAllWindows()