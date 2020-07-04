from tkinter import *
import numpy as np
import sqlite3
import cv2
import os
from PIL import Image, ImageTk

master = Tk()
master.geometry('1370x1000')
master.configure(bg="#b56969")

load = Image.open("mainpic.jpg")
load = load.resize((400, 350), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)

img = Label(master, image=render)
img.image = render
img.place(x=475, y=120)

text = Label(master, text="ATTENDENCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
text.place(x=0,y=0)

text = Label(master, text="Enter Your ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
text.place(x=35,y=500)

e1 = Entry(master,width=20,font=("Courier", 50))
e1.pack()
e1.place(x = 685, y = 498)

text = Label(master, text="Creating Face Datasets:",fg="#22264b",bg="#e8edf3",width=23,height=1,font=("Courier", 50),anchor="center")
text.place(x=35,y=600)

def callback():
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    e=e1.get()
    face_id = e
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    count = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('CollectDatasets', img)
        if(cv2.waitKey(1)==ord('q')):
            break
        elif count >= 30:
            break
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

b1= Button(master, text="DATASET COLLECTION", command=callback,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
b1.pack()
b1.place(x=1275,y=630,anchor="e",height=50,width=500)

text = Label(master, text="Training of Datasets:",fg="#22264b",bg="#e8edf3",width=23,height=1,font=("Courier", 50),anchor="center")
text.place(x=35,y=700)

def callback1():
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids
    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
    recognizer.write('trainer.yml') 
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

b = Button(master, text="TRAINING DATASETS", command=callback1,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
b.pack()
b.place(x=1275,y=730,anchor="e",height=50,width=500)

text = Label(master, text="Recognizing Faces:",fg="#22264b",bg="#e8edf3",width=23,height=1,font=("Courier", 50),anchor="center")
text.place(x=35,y=800)

def callback2():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    id = 0

    names = ['None', 'Priyal', 'Ruchi', 'Pratham', 'Hema', 'Dharmendra']
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
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

b2 = Button(master, text="FACE RECOGNIZER", command=callback2,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
b2.pack()
b2.place(x=1275,y=830,anchor="e",height=50,width=500)

def callback3():
    top=Toplevel()
    top.geometry('1370x1000')
    top.configure(bg="#b56969")

    text = Label(top, text="LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
    text.place(x=0,y=0)

    text = Label(top, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
    text.place(x=35,y=300)

    e1 = Entry(top,width=20,font=("Courier", 50))
    e1.pack()
    e1.place(x = 685, y = 298)

    text1 = Label(top, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
    text1.place(x=35,y=400)

    e2 = Entry(top,width=20,font=("Courier", 50))
    e2.pack()
    e2.place(x = 685, y = 398)

    def callback4():
        id=e1.get()
        pwd=e2.get()
        conn=sqlite3.connect("facedatabase.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id,pwd))
        for row in cursor:
            isRecordExist=1
        if(isRecordExist==1):
            cursor.execute("""UPDATE DataStud SET Name=? WHERE Id=?""",("Priyaldp",id))
        else:
            print("Error")
        conn.commit()
        cursor.close()

    b4 = Button(top, text="LOGIN", command=callback4,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
    b4.pack()
    b4.place(x=670,y=525,anchor="e",height=50,width=500)

    def callback5():
        top=Toplevel()
        top.geometry('1370x1000')
        top.configure(bg="#b56969")

        text = Label(top, text="SIGNUP ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
        text.place(x=0,y=0)

        def selection():  
            selection = "You selected the option " + str(radio.get())  
            label.config(text = selection) 

        radio = IntVar()

        R1 = Radiobutton(top, text="Admin", variable=radio, value=1,  
                        command=selection,width=6,height=1,font=("Courier", 50))  
        R1.pack( anchor = W )  
        R1.place(x=50,y=250)
        
        R2 = Radiobutton(top, text="Teacher", variable=radio, value=2,  
                        command=selection,width=8,height=1,font=("Courier", 50))  
        R2.pack( anchor = W ) 
        R2.place(x=450,y=250) 
        
        R3 = Radiobutton(top, text="Student", variable=radio, value=3,  
                        command=selection,width=8,height=1,font=("Courier", 50))  
        R3.pack( anchor = W) 
        R3.place(x=800,y=250) 
        
        label = Label(top)  
        label.pack()

        text = Label(top, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
        text.place(x=35,y=400)

        e1 = Entry(top,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 398)

        text2 = Label(top, text="Enter Name:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
        text2.place(x=35,y=500)

        e3 = Entry(top,width=20,font=("Courier", 50))
        e3.pack()
        e3.place(x = 685, y = 498)

        text1 = Label(top, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
        text1.place(x=35,y=600)

        e2 = Entry(top,width=20,font=("Courier", 50))
        e2.pack()
        e2.place(x = 685, y = 598)

        def callback6():
            id=e1.get()
            pwd=e2.get()
            name=e3.get()
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("INSERT INTO DataStud(Id,Name,Pass) VALUES('%s','%s','%s')"%(id,name,pwd))
            conn.commit()
            cursor.close()
            top.destroy()

        b6 = Button(top, text="CREATE ACCOUNT", command=callback6,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
        b6.pack()
        b6.place(x=940,y=725,anchor="e",height=50,width=500)

    b5 = Button(top, text="SIGNUP", command=callback5,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
    b5.pack()
    b5.place(x=1200,y=525,anchor="e",height=50,width=500)

b3 = Button(master, text="Next window", command=callback3,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
b3.pack()
b3.place(x=1275,y=930,anchor="e",height=50,width=500)

mainloop()