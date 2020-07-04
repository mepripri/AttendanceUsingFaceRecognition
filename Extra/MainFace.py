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
load = load.resize((750, 650), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)

img = Label(master, image=render)
img.image = render
img.place(x=310, y=120)

text = Label(master, text="ATTENDENCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
text.place(x=0,y=0)

def callback8():
    conn=sqlite3.connect("facedatabase.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM DataStud")
    rows = cursor.fetchall()
    for row in rows:
        id=row[0]
        name=row[1]
        pwd=row[2]
        att=row[3]
        print(id+" "+name+" "+pwd+" "+att)
    conn.commit()
    cursor.close()

b6 = Button(top, text="VIEW ATTENDANCE", command=callback8,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
b6.pack()
b6.place(x=540,y=525,anchor="e",height=50,width=500)

def callback():
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    e=e3.get()
    face_id = e
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
    cam.release()
    cv2.destroyAllWindows()

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
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
    recognizer.write('trainer.yml') 

    text = Label(top, text="Datasets are Trained...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center")
    text.place(x=0,y=880)  

b1= Button(top, text="DATASET COLLECTION", command=callback,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
b1.pack()
b1.place(x=630,y=830,anchor="e",height=50,width=500)

def callback2():
    id1=e1.get()
    pwd=e2.get()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    id = 0
    names=['None']
    conn=sqlite3.connect("facedatabase.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id1,pwd))
    rows = cursor.fetchall()
    for row in rows:
        name1=row[1]
    isRecordExist1=1
    if(isRecordExist1==1):
        names.append(pwd)
        print(names[1])
    else:
        print("Error")
    conn.commit()
    cursor.close()

    #names = ['None', 'Priyal', 'Ruchi', 'Dhruv', 'Hema', 'Ravi']
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

b2 = Button(top, text="FACE RECOGNIZER", command=callback2,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
b2.pack()
b2.place(x=1230,y=830,anchor="e",height=50,width=500)

def callback5():
    top1=Toplevel()
    top1.geometry('1370x1000')
    top1.configure(bg="#b56969")

    text = Label(top1, text="SIGNUP ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
    text.place(x=0,y=0)

    text = Label(top1, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
    text.place(x=35,y=400)

    e1 = Entry(top1,width=20,font=("Courier", 50))
    e1.pack()
    e1.place(x = 685, y = 398)

    text2 = Label(top1, text="Enter Name:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
    text2.place(x=35,y=500)

    e3 = Entry(top1,width=20,font=("Courier", 50))
    e3.pack()
    e3.place(x = 685, y = 498)

    text1 = Label(top1, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
    text1.place(x=35,y=600)

    e2 = Entry(top1,width=20,font=("Courier", 50),show="*")
    e2.pack()
    e2.place(x = 685, y = 598)
    def callback7():
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

        e2 = Entry(top,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        def callback4():
            id=e1.get()
            pwd=e2.get()
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            if(a==1):
                if(id=="14" and pwd=="pripri"):
                    print("hii")
            elif(a==3):
                cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id,pwd))
                rows = cursor.fetchall()
                for row in rows:
                    name=row[1]
                    isRecordExist=1
                if(isRecordExist==1):
                    top.destroy()
                    top1=Toplevel()
                    top1.geometry('1370x1000')
                    top1.configure(bg="#b56969")

                    text = Label(top1, text="ATTENDENCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                    text.place(x=0,y=0)

                    load = Image.open("mainpic.jpg")
                    load = load.resize((550, 450), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(load)

                    img = Label(top1, image=render)
                    img.image = render
                    img.place(x=710, y=210)

                    text = Label(top1, text="   STEPS   \n\n1. Dataset Creation\n\n2. Dataset Training\n\n3. Face Recognizer" ,fg="#e8edf3",bg="#22264b",width=20,height=8,font=("Courier", 50),anchor="center")
                    text.place(x=50,y=230)

                    text = Label(top1, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                    text.place(x=0,y=120)

                    text = Label(top1, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
                    text.place(x=35,y=700)

                    e3 = Entry(top1,width=20,font=("Courier", 50))
                    e3.pack()
                    e3.place(x = 685, y = 698)

def selection():
    a=radio.get()
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

    e2 = Entry(top,width=20,font=("Courier", 50),show="*")
    e2.pack()
    e2.place(x = 685, y = 398)
    def callback4():
        id=e1.get()
        pwd=e2.get()
        conn=sqlite3.connect("facedatabase.db")
        cursor=conn.cursor()
        if(a==1):
            if(id=="admin" and pwd=="admin"):
                print("hii")
        elif(a==2):
            cursor.execute("SELECT * FROM DataTea WHERE Id='%s' and Pass='%s'"%(id,pwd))
            rows = cursor.fetchall()
            for row in rows:
                name=row[1]
            isRecordExist1=1
            if(isRecordExist1==1):
                top=Toplevel()
                top.geometry('1370x1000')
                top.configure(bg="#b56969")

                text = Label(top, text="ATTENDENCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                text.place(x=0,y=0)

                load = Image.open("mainpic.jpg")
                load = load.resize((550, 450), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)

                img = Label(top, image=render)
                img.image = render
                img.place(x=710, y=210)
                callback8()

        elif(a==3):
            cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id,pwd))
            rows = cursor.fetchall()
            for row in rows:
                name=row[1]
                isRecordExist=1
            if(isRecordExist==1):
                top=Toplevel()
                top.geometry('1370x1000')
                top.configure(bg="#b56969")

                text = Label(top, text="ATTENDENCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                text.place(x=0,y=0)

                load = Image.open("mainpic.jpg")
                load = load.resize((550, 450), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)

                img = Label(top, image=render)
                img.image = render
                img.place(x=710, y=210)

                text = Label(top, text="   STEPS   \n\n1. Dataset Creation\n\n2. Dataset Training\n\n3. Face Recognizer" ,fg="#e8edf3",bg="#22264b",width=20,height=8,font=("Courier", 50),anchor="center")
                text.place(x=50,y=230)

                text = Label(top, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                text.place(x=0,y=120)

                text = Label(top, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
                text.place(x=35,y=700)

                e3 = Entry(top,width=20,font=("Courier", 50))
                e3.pack()
                e3.place(x = 685, y = 698)

                callback()

                callback2()
                else:
                print("Error")
            elif(a==2):
                conn=sqlite3.connect("facedatabase.db")
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM DataTea WHERE Id='%s' and Pass='%s'"%(id,pwd))
                rows = cursor.fetchall()
                for row in rows:
                    name=row[1]
                    isRecordExist1=1
                if(isRecordExist1==1):
                    print("Hii"+name)
                else:
                    print("Error")
            conn.commit()
            cursor.close()

        b4 = Button(top, text="LOGIN", command=callback4,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
        b4.pack()
        b4.place(x=660,y=525,anchor="e",height=50,width=500)

        callback()
        callback2()
    else:
            print("Error")
    elif(a==2):
        conn=sqlite3.connect("facedatabase.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM DataTea WHERE Id='%s' and Pass='%s'"%(id,pwd))
        rows = cursor.fetchall()
        for row in rows:
            name=row[1]
            isRecordExist1=1
        if(isRecordExist1==1):
            print("Hii"+name)
        else:
            print("Error")
    conn.commit()
    cursor.close()

b4 = Button(top, text="LOGIN", command=callback4,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
b4.pack()
b4.place(x=930,y=525,anchor="e",height=50,width=500)

text = Label(top, text="ACCOUNT CREATED. PLEASE LOGIN...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
text.place(x=0,y=600)



radio = IntVar()

R1 = Radiobutton(master, text="ADMIN",bg="#22264b",fg="#e8edf3",variable=radio, value=1,command=selection,width=10,height=1,font=("Courier", 50),selectcolor="pink")  
R1.pack( anchor = W )  
R1.place(x=100,y=850)
        
R2 = Radiobutton(master, text="TEACHER",bg="#22264b",fg="#e8edf3", variable=radio, value=2,command=selection,width=10,height=1,font=("Courier", 50))  
R2.pack( anchor = W ) 
R2.place(x=500,y=850) 
        
R3 = Radiobutton(master, text="STUDENT",bg="#22264b",fg="#e8edf3", variable=radio, value=3,command=selection,width=10,height=1,font=("Courier", 50))  
R3.pack( anchor = W) 
R3.place(x=900,y=850) 

mainloop()