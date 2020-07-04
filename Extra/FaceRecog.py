import tkinter as tk
from tkinter import *
import numpy as np
import sqlite3
import webbrowser
import cv2
import time
import os
from datetime import date
from PIL import Image, ImageTk

master = tk.Tk()
master.geometry('1370x1000')
master.configure(bg="#b56969")

load = Image.open("mainpic.jpg")
load = load.resize((750, 650), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)

img = tk.Label(master, image=render)
img.image = render
img.place(x=310, y=120)

text = tk.Label(master, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
text.place(x=0,y=0)

def selection():
    a=radio.get()
    
    img.destroy()
    R1.destroy()
    R2.destroy()
    R3.destroy()
    text.destroy()

    if(a==1):
        str="ADMIN"
    elif(a==2):
        str="FACULTY"
    elif(a==3):
        str="STUDENT"

    if(a==1):
        str1="Username:"
    elif(a==2):
        str1="Faculty Id:"
    elif(a==3):
        str1="Student Id:"

    def callback4():
        conn=sqlite3.connect("facedatabase.db")
        cursor=conn.cursor()
        if(a==1):   
            id=e1.get()
            pwd=e2.get()
            id="admin"
            pwd="admin"
            b4.destroy()
            e1.destroy()
            e2.destroy()
            #text3.destroy()
            #text4.destroy()

            if(id=="admin" and pwd=="admin"):
                """today=date.today()
                conn=sqlite3.connect("facedatabase.db")
                cursor=conn.cursor()
                cursor.execute("ALTER TABLE DataStud ADD '"+str(today)+"' VARCHAR(50) DEFAULT('A')")
                conn.commit()
                cursor.close()"""

                text = tk.Label(master, text="ATTENDENCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                text.place(x=0,y=0)

                load = Image.open("mainpic.jpg")
                load = load.resize((550, 450), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)

                img = tk.Label(master, image=render)
                img.image = render
                img.place(x=710, y=210)

                text1 = tk.Label(master, text="   STEPS   \n\n1. Dataset Creation\n\n2. Dataset Training\n\n3. Face Recognizer" ,fg="#e8edf3",bg="#22264b",width=20,height=8,font=("Courier", 50),anchor="center")
                text1.place(x=50,y=230)

                text2 = tk.Label(master, text="Welcome ",fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                text2.place(x=0,y=120)

                text3 = tk.Label(master, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
                text3.place(x=35,y=700)

                e3 = tk.Entry(master,width=20,font=("Courier", 50))
                e3.pack()
                e3.place(x = 685, y = 698)

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
                        elif count >= 50:
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

                    text = tk.Label(master, text="Datasets are Trained...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center")
                    text.place(x=0,y=880)  

                b1= tk.Button(master, text="DATASET COLLECTION", command=callback,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
                b1.pack()
                b1.place(x=630,y=830,anchor="e",height=50,width=500)
            else:
                top.destroy()
                selection1()
        elif(a==2):
            id=e1.get()
            pwd=e2.get()
            b4.destroy()
            e1.destroy()
            e2.destroy()
            id="1"
            pwd="Nil"
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataTea WHERE Id='%s' and Pass='%s'"%(id,pwd))
            isRecordExist2=0
            rows = cursor.fetchall()
            for row in rows:
                name=row[1]
                isRecordExist2=1
            if(isRecordExist2!=1):
                top.destroy()
                selection1()
            else:
                text = tk.Label(master, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                text.place(x=0,y=0)

                load = Image.open("mainpic.jpg")
                load = load.resize((750, 650), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)

                img = tk.Label(master, image=render)
                img.image = render
                img.place(x=310, y=160)
                #img.place(x=20, y=160)
                str1=str(id)

                text4 = tk.Label(master, text="Select Subject:",fg="#22264b",bg="#e8edf3",width=15,height=1,font=("Courier", 50),anchor="center")
                text4.place(x=35,y=830)

                OptionList = ["Information Security","Software Engineering","Theory of Computation","Advance Java","Mini Project","Electronics Communication"]
                variable = StringVar(top)
                variable.set(OptionList[0])

                def check(OptionList):
                    sub=variable.get()
                    return sub

                def check1(OptionList):
                    check(OptionList)
                    a=variable.get()
                    globals()['sub']=a

                opt = tk.OptionMenu(master, variable, *OptionList,command=check1)
                opt.config(width=24,font=("Courier", 40))
                opt.grid(row=10)
                opt.pack(side="top",pady=20)
                opt.place(x = 545, y = 835)

                b = tk.Button(master, text="GO", command=callback9,relief=RAISED,width=2,fg="#22264b",bg='#e6cf8b',font=("Courier", 20))
                b.pack()
                b.place(x=1325,y=860,anchor="e",height=50,width=100)

                c=0
                if(c==0):
                    today=date.today()
                    conn=sqlite3.connect("facedatabase.db")
                    cursor=conn.cursor()
                    cursor.execute("ALTER TABLE DataStud ADD '"+str(today)+"' VARCHAR(50) DEFAULT('A')")
                    conn.commit()
                    cursor.close()
                    #OptionList1 = ["IS","SE","TOC","ADVJAVA","MIPRO","EL"]
                    OptionList1 = ["IS"]
                    for op in OptionList1:
                        conn=sqlite3.connect("facedatabase.db")
                        cursor=conn.cursor()
                        cursor.execute("ALTER TABLE '"+op+"' ADD '"+str(today)+"' VARCHAR(50) DEFAULT('A')")
                        conn.commit()
                        cursor.close()
                    c+=1

                def callback9():
                    top2=Toplevel()
                    top2.geometry('1370x1000')
                    top2.configure(bg="#b56969")

                    text = Label(top2, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                    text.place(x=0,y=0)

                    load = Image.open("mainpic.jpg")
                    load = load.resize((750, 650), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(load)

                    img = Label(top2, image=render)
                    img.image = render
                    img.place(x=310, y=160)
                    #img.place(x=20, y=160)

                    text = Label(top2, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                    text.place(x=0,y=120)

                    sub1=sub
                    if(sub1=="Information Security"):
                        sub2="IS"
                    elif(sub1=="Software Engineering"):
                        sub2="SE"           
                    elif(sub1=="Theory of Computation"):
                        sub2="TOC"
                    elif(sub1=="Advance Java"):
                        sub2="ADVJAVA"
                    elif(sub1=="Mini Project"):
                        sub2="MIPRO"
                    elif(sub1=="Electronics Communication"):
                        sub2="EL"
                    def callback8():
                        file = open('Attend/'+sub2+'.xls','w')
                        conn=sqlite3.connect("facedatabase.db")
                        conn.row_factory = sqlite3.Row
                        cursor=conn.cursor()
                        cursor.execute("SELECT * FROM '"+sub2+"'")
                        colnames = cursor.description
                        con=len(colnames)
                        for row in colnames:
                            file.write(row[0]+" ")
                        conn.commit()
                        cursor.close()
                        file.close()
                        file = open('Attend/'+sub2+'.xls','a')
                        conn=sqlite3.connect("facedatabase.db")
                        cursor=conn.cursor()
                        cursor.execute("SELECT * FROM '"+sub2+"'")
                        rows = cursor.fetchall()
                        file.write("\n")
                        for row in rows:
                            file.write(row[0]+" "+row[1]+"   "+row[2])
                            j=3
                            while(j<con):
                                file.write("          "+row[j])
                                j+=1
                            file.write("\n")
                        conn.commit()
                        cursor.close()
                        file.close()
                        filename="Attend/"+sub2+".xls"
                        webbrowser.open('file://' + os.path.realpath(filename),new=1)

                    b6 = Button(top2, text="VIEW ATTENDANCE", command=callback8,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
                    b6.pack()
                    b6.place(x=635,y=875,anchor="e",height=50,width=500)
                    
                    def callback2():
                        recognizer = cv2.face.LBPHFaceRecognizer_create()
                        recognizer.read('trainer.yml')
                        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                        id = 0
                        names=['None']
                        conn=sqlite3.connect("facedatabase.db")
                        cursor=conn.cursor()
                        cursor.execute("SELECT * FROM DataStud")
                        rows = cursor.fetchall()
                        for row in rows:
                            name1=row[1]
                            names.append(name1)
                        names.append('Null')
                        conn.commit()
                        cursor.close()
                        #names = ['None', 'Priyal', 'Ruchi', 'Dhruv', 'Hema']
                        cam = cv2.VideoCapture(0)
                        # Define min window size to be recognized as a face
                        minW = 0.1*cam.get(3)
                        minH = 0.1*cam.get(4)
                        i=0
                        while i<=30:
                            ret, img =cam.read()
                            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            i=i+1
                            faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors = 5,minSize = (int(minW), int(minH)))
                            for(x,y,w,h) in faces:
                                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                                # If confidence is less then 100 ==> "0" : perfect match 
                                id1=id
                                flag=0
                                if (confidence <=40 and confidence>=25):
                                    id = names[id]
                                    flag=1
                                    confidence = "  {0}%".format(round(100 - confidence))
                                else:
                                    id ='unknown'
                                    confidence = "  {0}%".format(round(100 - confidence))
                                    cv2.putText(img,str(id),(x+5,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                                    cv2.putText(img,str(confidence),(x+5,y+h-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1)
                                if(flag==0):
                                    continue
                                if(flag==1):
                                    conn=sqlite3.connect("facedatabase.db")
                                    cursor=conn.cursor()
                                    cursor.execute("UPDATE '"+sub2+"' SET '"+str(today)+"'='P' WHERE id="+str(id1))
                                    conn.commit()
                                    cursor.close()
                                cv2.putText(img,str(id),(x+5,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                                cv2.putText(img,str(confidence),(x+5,y+h-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1)
                            cv2.imshow('Recognition',img) 
                            if(cv2.waitKey(1)==ord('q')):
                                break
                        cam.release()
                        cv2.destroyAllWindows()

                    b2 = Button(top2, text="TAKE ATTENDENCE", command=callback2,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
                    b2.pack()
                    b2.place(x=1235,y=875,anchor="e",height=50,width=500)

                    text = Label(top2, text="Subject: "+sub2 ,fg="#e8edf3",bg="#22264b",width=24,height=1,font=("Courier", 50),anchor="center")
                    text.place(x=312,y=180)

                text = Label(master, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                text.place(x=0,y=120)
                top.destroy()
        elif(a==3):
            id1=e1.get()
            pwd=e2.get()
            cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id1,pwd))
            rows=cursor.fetchall()
            isRecordExist2=0
            if(rows):
                isRecordExist2=1
            for row in rows:
                name=row[1]
            if(isRecordExist2!=1):
                top.destroy()
                selection1()
            else:
                master=Toplevel()
                master.geometry('1370x1000')
                master.configure(bg="#b56969")

                text = Label(master, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                text.place(x=0,y=0)

                load = Image.open("mainpic.jpg")
                load = load.resize((750, 650), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)

                img = Label(master, image=render)
                img.image = render
                img.place(x=310, y=160)
                str1=str(id1)

                def callback8():
                    file = open('Attend/'+str1+'.xls','w')
                    conn=sqlite3.connect("facedatabase.db")
                    conn.row_factory = sqlite3.Row
                    cursor=conn.cursor()
                    cursor.execute("SELECT * FROM DataStud")
                    colnames = cursor.description
                    con=len(colnames)
                    for row in colnames:
                        file.write(row[0]+" ")
                    conn.commit()
                    cursor.close()
                    file.close()
                    file = open('Attend/'+str1+'.xls','a')
                    conn=sqlite3.connect("facedatabase.db")
                    cursor=conn.cursor()
                    cursor.execute("SELECT * FROM DataStud WHERE Id='"+id1+"'")
                    rows = cursor.fetchall()
                    file.write("\n")
                    for row in rows:
                        file.write(row[0]+" "+row[1]+" "+row[2])
                        j=3
                        while(j<con):
                            file.write("          "+row[j])
                            j+=1
                    conn.commit()
                    cursor.close()
                    file.close()
                    filename="Attend/"+str1+".xls"
                    webbrowser.open('file://' + os.path.realpath(filename),new=1)

                b6 = Button(master, text="VIEW ATTENDANCE", command=callback8,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
                b6.pack()
                b6.place(x=935,y=875,anchor="e",height=50,width=500)

                text = Label(master, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                text.place(x=0,y=120)
                top.destroy()

    text1 = tk.Label(master, text=str+" LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
    text1.place(x=0,y=0)

    text3 = tk.Label(master, text="Enter "+str1,fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
    text3.place(x=35,y=300)

    e1 = tk.Entry(master,width=20,font=("Courier", 50))
    e1.pack()
    e1.place(x = 685, y = 298)

    text4 = tk.Label(master, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
    text4.place(x=35,y=400)

    e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
    e2.pack()
    e2.place(x = 685, y = 398)

    b4 = tk.Button(master, text="LOGIN", command=callback4,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
    b4.pack()
    b4.place(x=960,y=525,anchor="e",height=50,width=500)


    """if(a==2 or a==3):
        def callback5():
            top1=Toplevel()
            top1.geometry('1370x1000')
            top1.configure(bg="#b56969")

            text = Label(top1, text="SIGNUP ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
            text.place(x=0,y=0)

            if(a==1):
                text = Label(top1, text="Enter Username:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
                text.place(x=35,y=400)

                e1 = Entry(top1,width=20,font=("Courier", 50))
                e1.pack()
                e1.place(x = 685, y = 398)
            elif(a==2):
                text = Label(top1, text="Enter Faculty Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
                text.place(x=35,y=400)

                e1 = Entry(top1,width=20,font=("Courier", 50))
                e1.pack()
                e1.place(x = 685, y = 398)
            elif(a==3):
                text = Label(top1, text="Enter Student Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
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
                
                if(a==1):
                    text = Label(top, text="Enter Username:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
                    text.place(x=35,y=300)

                    e1 = Entry(top,width=20,font=("Courier", 50))
                    e1.pack()
                    e1.place(x = 685, y = 298)
                elif(a==2):
                    text = Label(top, text="Enter Faculty Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
                    text.place(x=35,y=300)

                    e1 = Entry(top,width=20,font=("Courier", 50))
                    e1.pack()
                    e1.place(x = 685, y = 298)
                elif(a==3):
                    text = Label(top, text="Enter Student Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
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
                        id=e1.get()
                        pwd=e2.get()
                        if(id=="admin" and pwd=="admin"):
                            master=Toplevel()
                            master.geometry('1370x1000')
                            master.configure(bg="#b56969")

                            today=date.today()
                            conn=sqlite3.connect("facedatabase.db")
                            cursor=conn.cursor()
                            cursor.execute("ALTER TABLE DataStud ADD '"+str(today)+"' VARCHAR(50) DEFAULT('A')")
                            conn.commit()
                            cursor.close()

                            text = Label(master, text="ATTANDENCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                            text.place(x=0,y=0)

                            load = Image.open("mainpic.jpg")
                            load = load.resize((550, 450), Image.ANTIALIAS)
                            render = ImageTk.PhotoImage(load)

                            img = Label(master, image=render)
                            img.image = render
                            img.place(x=710, y=210)

                            text = Label(master, text="   STEPS   \n\n1. Dataset Creation\n\n2. Dataset Training\n\n3. Face Recognizer" ,fg="#e8edf3",bg="#22264b",width=20,height=8,font=("Courier", 50),anchor="center")
                            text.place(x=50,y=230)

                            text = Label(master, text="Welcome ",fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                            text.place(x=0,y=120)

                            text = Label(master, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center")
                            text.place(x=35,y=700)

                            e3 = Entry(master,width=20,font=("Courier", 50))
                            e3.pack()
                            e3.place(x = 685, y = 698)

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
                                    elif count >= 50:
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

                                text = Label(master, text="Datasets are Trained...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center")
                                text.place(x=0,y=880)  

                            b1= Button(master, text="DATASET COLLECTION", command=callback,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
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
                                cursor.execute("SELECT * FROM DataStud")
                                rows = cursor.fetchall()
                                for row in rows:
                                    name1=row[1]
                                    names.append(name1)
                                names.append('Null')
                                conn.commit()
                                cursor.close()
                                #names = ['None', 'Priyal', 'Ruchi', 'Dhruv', 'Hema']
                                cam = cv2.VideoCapture(0)
                                # Define min window size to be recognized as a face
                                minW = 0.1*cam.get(3)
                                minH = 0.1*cam.get(4)
                                i=0
                                while i<=30:
                                    ret, img =cam.read()
                                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                    i=i+1
                                    faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors = 5,minSize = (int(minW), int(minH)))
                                    for(x,y,w,h) in faces:
                                        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                                        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                                        # If confidence is less then 100 ==> "0" : perfect match 
                                        id1=id
                                        flag=0
                                        if (confidence <=40 and confidence>=25):
                                            id = names[id]
                                            flag=1
                                            confidence = "  {0}%".format(round(100 - confidence))
                                        else:
                                            id ='unknown'
                                            confidence = "  {0}%".format(round(100 - confidence))
                                            cv2.putText(img,str(id),(x+5,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                                            cv2.putText(img,str(confidence),(x+5,y+h-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1)
                                        if(flag==0):
                                            continue
                                        if(flag==1):
                                            conn=sqlite3.connect("facedatabase.db")
                                            cursor=conn.cursor()
                                            cursor.execute("UPDATE DataStud SET '"+str(today)+"'='P' WHERE id="+str(id1))
                                            conn.commit()
                                            cursor.close()
                                        cv2.putText(img,str(id),(x+5,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                                        cv2.putText(img,str(confidence),(x+5,y+h-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1)
                                    cv2.imshow('Recognition',img) 
                                    if(cv2.waitKey(1)==ord('q')):
                                        break
                                cam.release()
                                cv2.destroyAllWindows()

                            b2 = Button(master, text="FACE RECOGNIZER", command=callback2,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
                            b2.pack()
                            b2.place(x=1230,y=830,anchor="e",height=50,width=500)
                        else:
                            top.destroy()
                            selection1()
                    elif(a==2):
                        id=e1.get()
                        pwd=e2.get()
                        conn=sqlite3.connect("facedatabase.db")
                        cursor=conn.cursor()
                        cursor.execute("SELECT * FROM DataTea WHERE Id='%s' and Pass='%s'"%(id,pwd))
                        isRecordExist2=0
                        rows = cursor.fetchall()
                        for row in rows:
                            name=row[1]
                            isRecordExist2=1
                        if(isRecordExist2!=1):
                            top.destroy()
                            selection1()
                        else:
                            master=Toplevel()
                            master.geometry('1370x1000')
                            master.configure(bg="#b56969")

                            text = Label(master, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                            text.place(x=0,y=0)

                            load = Image.open("mainpic.jpg")
                            load = load.resize((750, 650), Image.ANTIALIAS)
                            render = ImageTk.PhotoImage(load)

                            img = Label(master, image=render)
                            img.image = render
                            img.place(x=310, y=160)
                            str1=str(id)

                            def callback8():
                                file = open('Attend/'+str1+'.xls','w')
                                conn=sqlite3.connect("facedatabase.db")
                                conn.row_factory = sqlite3.Row
                                cursor=conn.cursor()
                                cursor.execute("SELECT * FROM DataStud")
                                colnames = cursor.description
                                con=len(colnames)
                                for row in colnames:
                                    file.write(row[0]+" ")
                                conn.commit()
                                cursor.close()
                                file.close()
                                file = open('Attend/'+str1+'.xls','a')
                                conn=sqlite3.connect("facedatabase.db")
                                cursor=conn.cursor()
                                cursor.execute("SELECT * FROM DataStud")
                                rows = cursor.fetchall()
                                file.write("\n")
                                for row in rows:
                                    file.write(row[0]+" "+row[1]+"   "+row[2])
                                    j=3
                                    while(j<con):
                                        file.write("          "+row[j])
                                        j+=1
                                    file.write("\n")
                                conn.commit()
                                cursor.close()
                                file.close()
                                filename="Attend/"+str1+".xls"
                                webbrowser.open('file://' + os.path.realpath(filename),new=1)

                            b6 = Button(master, text="VIEW ATTENDANCE", command=callback8,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
                            b6.pack()
                            b6.place(x=935,y=875,anchor="e",height=50,width=500)

                            text = Label(master, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                            text.place(x=0,y=120)
                            top.destroy()
                        conn.commit()
                        cursor.close()
                    elif(a==3):
                        id1=e1.get()
                        pwd=e2.get()
                        cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id1,pwd))
                        rows=cursor.fetchall()
                        isRecordExist2=0
                        if(rows):
                            isRecordExist2=1
                        for row in rows:
                            name=row[1]
                        if(isRecordExist2!=1):
                            top.destroy()
                            selection1()
                        else:
                            master=Toplevel()
                            master.geometry('1370x1000')
                            master.configure(bg="#b56969")

                            text = Label(master, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                            text.place(x=0,y=0)

                            load = Image.open("mainpic.jpg")
                            load = load.resize((750, 650), Image.ANTIALIAS)
                            render = ImageTk.PhotoImage(load)

                            img = Label(master, image=render)
                            img.image = render
                            img.place(x=310, y=160)
                            str1=str(id1)

                            def callback8():
                                file = open('Attend/'+str1+'.xls','w')
                                conn=sqlite3.connect("facedatabase.db")
                                conn.row_factory = sqlite3.Row
                                cursor=conn.cursor()
                                cursor.execute("SELECT * FROM DataStud")
                                colnames = cursor.description
                                con=len(colnames)
                                for row in colnames:
                                    file.write(row[0]+" ")
                                conn.commit()
                                cursor.close()
                                file.close()
                                file = open('Attend/'+str1+'.xls','a')
                                conn=sqlite3.connect("facedatabase.db")
                                cursor=conn.cursor()
                                cursor.execute("SELECT * FROM DataStud WHERE Id='"+id1+"'")
                                rows = cursor.fetchall()
                                file.write("\n")
                                for row in rows:
                                    file.write(row[0]+" "+row[1]+" "+row[2])
                                    j=3
                                    while(j<con):
                                        file.write("          "+row[j])
                                        j+=1
                                conn.commit()
                                cursor.close()
                                file.close()
                                filename="Attend/"+str1+".xls"
                                webbrowser.open('file://' + os.path.realpath(filename),new=1)

                            b6 = Button(master, text="VIEW ATTENDANCE", command=callback8,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
                            b6.pack()
                            b6.place(x=935,y=875,anchor="e",height=50,width=500)

                            text = Label(master, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center")
                            text.place(x=0,y=120)
                            top.destroy()

                b4 = Button(top, text="LOGIN", command=callback4,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
                b4.pack()
                b4.place(x=930,y=525,anchor="e",height=50,width=500)

                text = Label(top, text="ACCOUNT CREATED. PLEASE LOGIN...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center")
                text.place(x=0,y=600)

            def callback6():
                if(a==2):
                    id=e1.get()
                    pwd=e2.get()
                    name=e3.get()
                    conn=sqlite3.connect("facedatabase.db")
                    cursor=conn.cursor()
                    cursor.execute("INSERT INTO DataTea(Id,Name,Pass) VALUES('%s','%s','%s')"%(id,name,pwd))
                    conn.commit()
                    cursor.close()
                    top1.destroy()
                    top.destroy()
                    callback7()
                if(a==3):
                    id=e1.get()
                    pwd=e2.get()
                    name=e3.get()
                    conn=sqlite3.connect("facedatabase.db")
                    cursor=conn.cursor()
                    cursor.execute("INSERT INTO DataStud(Id,Name,Pass) VALUES('%s','%s','%s')"%(id,name,pwd))
                    conn.commit()
                    cursor.close()
                    OptionList1 = ["IS","SE","TOC","ADVJAVA","MIPRO","EL"]
                    #OptionList1 = ["IS"]
                    for op in OptionList1:
                        id=e1.get()
                        pwd=e2.get()
                        name=e3.get()
                        conn=sqlite3.connect("facedatabase.db")
                        cursor=conn.cursor()
                        cursor.execute("INSERT INTO '"+op+"' (Id,Name,Pass) VALUES('%s','%s','%s')"%(id,name,pwd))
                        conn.commit()
                        cursor.close()
                    top1.destroy()
                    top.destroy()
                    callback7()

            b6 = Button(top1, text="CREATE ACCOUNT", command=callback6,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
            b6.pack()
            b6.place(x=940,y=725,anchor="e",height=50,width=500)

        b5 = tk.Button(master, text="SIGNUP", command=callback5,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30))
        b5.pack()
        b5.place(x=1200,y=525,anchor="e",height=50,width=500)"""

radio = IntVar()

R1 = tk.Radiobutton(master, text="ADMIN",bg="#22264b",fg="#e8edf3",variable=radio, value=1,command=selection,width=10,height=1,font=("Courier", 50),selectcolor="pink")  
R1.pack( anchor = W )  
R1.place(x=100,y=850)
        
R2 = tk.Radiobutton(master, text="TEACHER",bg="#22264b",fg="#e8edf3", variable=radio, value=2,command=selection,width=10,height=1,font=("Courier", 50))  
R2.pack( anchor = W ) 
R2.place(x=500,y=850) 
        
R3 = tk.Radiobutton(master, text="STUDENT",bg="#22264b",fg="#e8edf3", variable=radio, value=3,command=selection,width=10,height=1,font=("Courier", 50))  
R3.pack( anchor = W) 
R3.place(x=900,y=850) 

master.mainloop()