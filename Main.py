try:
    import Tkinter as tk
except:
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
    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.configure(bg="#b56969")
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.geometry('1370x1050+0+0')
        master.resizable(0,0)
        master.configure(bg="#b56969")
        load = Image.open("mainpic.jpg")
        load = load.resize((750, 650), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=310, y=120)

        tk.Label(self, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)

        def selection():
            a=radio.get()

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
            if(a==1):
                master.switch_frame(PageOne)
            elif(a==2):
                master.switch_frame(PageThree)
            elif(a==3):
                master.switch_frame(PageSix)

        radio = IntVar()

        tk.Radiobutton(self, text="ADMIN",bg="#22264b",fg="#e8edf3",variable=radio, value=1,command=selection,width=10,height=1,font=("Courier", 50),selectcolor="pink").place_configure(x=100,y=850)
        tk.Radiobutton(self, text="FACULTY",bg="#22264b",fg="#e8edf3", variable=radio, value=2,command=selection,width=10,height=1,font=("Courier", 50)).place_configure(x=500,y=850) 
        tk.Radiobutton(self, text="STUDENT",bg="#22264b",fg="#e8edf3", variable=radio, value=3,command=selection,width=10,height=1,font=("Courier", 50)).place_configure(x=900,y=850) 
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=750,pady=500)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,pwd):
            if(id=="admin" and pwd=="admin"):
                master.switch_frame(PageTwo)
            else:
                master.switch_frame(PageNine)

        tk.Label(self, text="ADMIN LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Username:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        tk.Button(self, text="LOGIN", command=lambda:callback4(e1.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=960,y=525,anchor="e",height=50,width=500)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)
        
        tk.Label(master, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((550, 450), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=710, y=210)

        load1 = Image.open("logout.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        tk.Label(master, text="   STEPS   \n\n1. Dataset Creation\n\n2. Dataset Training\n\n3. Face Recognizer" ,fg="#e8edf3",bg="#22264b",width=20,height=8,font=("Courier", 50),anchor="center").place_configure(x=50,y=230)
        tk.Label(master, text="Welcome ",fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)
        tk.Label(master, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=700)

        e3 = tk.Entry(master,width=20,font=("Courier", 50))
        e3.pack()
        e3.place(x = 685, y = 698)

        def callback():
            if(e3.get()==''):
                master.switch_frame(PageFourteen)
            else:
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

            tk.Label(self, text="Datasets are Trained...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=880)  

        tk.Button(self, text="DATASET COLLECTION", command=callback,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=950,y=830,anchor="e",height=50,width=500)
        tk.Button(master,image=render1,command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        load1 = Image.open("logout.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        def callback4(id,pwd):
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataTea WHERE Id='%s' and Pass='%s'"%(id,pwd))
            isRecordExist2=0
            rows = cursor.fetchall()    
            for row in rows:
                name=row[1]
                isRecordExist2=1
            if(isRecordExist2!=1):
                master.switch_frame(PageTen)
            else:
                globals()['name']=name
                master.switch_frame(PageFour)

        tk.Label(self, text="FACULTY LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Faculty Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        tk.Button(self, text="LOGIN", command=lambda:callback4(e1.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=525,anchor="e",height=50,width=500)
        tk.Button(self, text="SIGNUP", command=lambda :master.switch_frame(PageTwelve),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=525,anchor="e",height=50,width=500)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)
        globals()['sub']=""

        tk.Label(self, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((750, 650), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=310, y=120)

        load1 = Image.open("logout.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1
        #str1=str(id)

        tk.Label(self, text="Subject:",fg="#22264b",bg="#e8edf3",width=15,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=830)

        OptionList = ["Please Select Subject","Information Security","Software Engineering","Theory of Computation","Advance Java","Mini Project","Electronics Communication"]
        variable = StringVar(self)
        variable.set(OptionList[0])

        def callback9():
            a=variable.get()
            globals()['sub']=a
            if(sub=="Information Security"):
                sub2="IS"
            elif(sub=="Software Engineering"):
                sub2="SE"           
            elif(sub=="Theory of Computation"):
                sub2="TOC"
            elif(sub=="Advance Java"):
                sub2="ADVJAVA"
            elif(sub=="Mini Project"):
                sub2="MIPRO"
            elif(sub=="Electronics Communication"):
                sub2="EL"
            if(sub=="Please Select Subject"):
                master.switch_frame(PageTwenty)
            else:
                conn=sqlite3.connect("facedatabase.db")
                conn.row_factory = sqlite3.Row
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM '"+sub2+"'")
                colnames = cursor.description
                con=len(colnames)
                for row in colnames:
                    if(str(row[0])==str(date.today())):
                        globals()['b']=1
                    else:
                        globals()['b']=0
                    if(b==1):
                        master.switch_frame(PageTwentyOne)
                    else:
                        master.switch_frame(PageFive)
                conn.commit()
                cursor.close()

        opt = tk.OptionMenu(master, variable,*OptionList)
        opt.config(width=24,font=("Courier", 40))
        opt.pack(side="top",pady=20)
        opt.place(x = 545, y = 835)

        tk.Label(self, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)
        tk.Button(self, text="GO", command=callback9,relief=RAISED,width=2,fg="#22264b",bg='#e6cf8b',font=("Courier", 20)).place_configure(x=1325,y=860,anchor="e",height=50,width=100)
        tk.Button(master,image=render1,command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageFive(tk.Frame):
    def __init__(self, master):        
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)
        c=0

        tk.Label(self, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((750, 650), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=310, y=120)
        #img.place(x=20, y=160)

        load1 = Image.open("back3.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        tk.Label(self, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)

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
        subis=""

        def callback8():
            file = open('Attend/'+sub2+'.xls','w')
            conn=sqlite3.connect("facedatabase.db")
            conn.row_factory = sqlite3.Row
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM '"+sub2+"'")
            colnames = cursor.description
            con=len(colnames)
            file.write("S_No."+"  ")
            for row in colnames:
                file.write(row[0]+" ")
            file.write("Total_Present ")
            file.write("Total_Absent")
            conn.commit()
            cursor.close()
            file.close()
            file = open('Attend/'+sub2+'.xls','a')
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM '"+sub2+"'")
            rows = cursor.fetchall()
            file.write("\n")
            co=0
            cu=1
            for row in rows:
                file.write(str(cu)+"       ")
                file.write(row[0]+" "+row[1]+"   "+row[2])
                j=3
                while(j<con):
                    file.write("          "+row[j])
                    if(row[j]=="P"):
                        co+=1
                    j+=1
                file.write("    "+str(co))
                file.write("              "+str(con-3-co))
                co=0
                cu+=1
                file.write("\n")
            conn.commit()
            cursor.close()
            file.close()
            filename="Attend/"+sub2+".xls"
            webbrowser.open('file://' + os.path.realpath(filename),new=1)

        tk.Button(self, text="VIEW ATTENDANCE", command=callback8,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=635,y=875,anchor="e",height=50,width=500)
     
        def callback2():
            today=date.today()
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("ALTER TABLE '"+sub2+"' ADD '"+str(today)+"' VARCHAR(50) DEFAULT('A')")
            conn.commit()
            cursor.close()
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
                        today=date.today()
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
            globals()['b']=1
            master.switch_frame(PageTwentyOne)
            
        tk.Button(self, text="TAKE ATTENDANCE", command=callback2,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1235,y=875,anchor="e",height=50,width=500)
        tk.Label(self, text="Subject: "+sub1 ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=178)
        tk.Button(self,image=render1,text="BACK",command=lambda: master.switch_frame(PageFour),height=80,width=90).place_configure(x=30,y=15)

class PageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,pwd):
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id,pwd))
            isRecordExist2=0
            rows = cursor.fetchall()    
            for row in rows:
                name=row[1]
                isRecordExist2=1
            if(isRecordExist2!=1):
                master.switch_frame(PageEleven)
            else:
                globals()['name']=name
                globals()['id']=id
                master.switch_frame(PageSeven)

        tk.Label(self, text="STUDENT LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Student Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        tk.Button(self, text="LOGIN", command=lambda: callback4(e1.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=525,anchor="e",height=50,width=500)
        tk.Button(self, text="SIGNUP", command=lambda :master.switch_frame(PageSixteen),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=525,anchor="e",height=50,width=500)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageSeven(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        tk.Label(self, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((750, 650), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=310, y=120)

        load1 = Image.open("logout.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        tk.Label(self, text="Subject:",fg="#22264b",bg="#e8edf3",width=15,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=830)

        OptionList = ["Please Select Subject","Information Security","Software Engineering","Theory of Computation","Advance Java","Mini Project","Electronics Communication"]
        variable = StringVar(self)
        variable.set(OptionList[0])

        def callback9():
            a=variable.get()
            globals()['sub']=a
            if(sub=="Please Select Subject"):
                master.switch_frame(PageNineteen)
            else:
                master.switch_frame(PageEight)

        opt = tk.OptionMenu(master, variable,*OptionList)
        opt.config(width=24,font=("Courier", 40))
        opt.pack(side="top",pady=20)
        opt.place(x = 545, y = 835)

        tk.Label(self, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)
        tk.Button(self, text="GO", command=callback9,relief=RAISED,width=2,fg="#22264b",bg='#e6cf8b',font=("Courier", 20)).place_configure(x=1325,y=860,anchor="e",height=50,width=100)
        tk.Button(master,image=render1,command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageEight(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        tk.Label(self, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((750, 650), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=310, y=120)
        #img.place(x=20, y=160)

        load1 = Image.open("back3.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        tk.Label(self, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)

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

        conn=sqlite3.connect("facedatabase.db")
        conn.row_factory = sqlite3.Row
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM '"+sub2+"'")
        colnames = cursor.description
        con=len(colnames)
        conn.commit()
        cursor.close()
        conn=sqlite3.connect("facedatabase.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM '"+sub2+"' WHERE id='"+str(id)+"'")
        rows = cursor.fetchall()
        j=3
        co=0
        for row in rows:
            while(j<con):
                if(row[j]=="P"):
                    co+=1
                j+=1
        conn.commit()
        cursor.close()
        ans=co/(con-3)*100

        if(ans>75):
            tk.Label(self, text="Your Attendance is: "+"{:.2f}".format(ans)+"%" ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=900)
        else:
            tk.Label(self, text="Your Attendance is: "+"{:.2f}".format(ans)+"%" ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=900)
            tk.Label(self, text="You are in Low Attendance" ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=950)

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
            file.write("Total_Present ")
            file.write("Total_Absent")
            conn.commit()
            cursor.close()
            file.close()
            file = open('Attend/'+sub2+'.xls','a')
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM '"+sub2+"' WHERE id='"+str(id)+"'")
            rows = cursor.fetchall()
            file.write("\n")
            co=0
            for row in rows:
                file.write(row[0]+" "+row[1]+"   "+row[2])
                j=3
                while(j<con):
                    file.write("          "+row[j])
                    if(row[j]=="P"):
                        co+=1
                    j+=1
                file.write("    "+str(co))
                file.write("              "+str(con-3-co))
                co=0
                file.write("\n")
            conn.commit()
            cursor.close()
            file.close()
            filename="Attend/"+sub2+".xls"
            webbrowser.open('file://' + os.path.realpath(filename),new=1)

        tk.Button(self, text="VIEW ATTENDANCE", command=callback8,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=950,y=850,anchor="e",height=50,width=500)
        tk.Label(self, text="Subject: "+sub1 ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=178)
        tk.Button(self,image=render1,text="BACK",command=lambda: master.switch_frame(PageSeven),height=80,width=90).place_configure(x=30,y=15)

class PageNine(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,pwd):
            if(id=="admin" and pwd=="admin"):
                master.switch_frame(PageTwo)
            else:
                master.switch_frame(PageNine)

        tk.Label(self, text="ADMIN LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Username:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        tk.Button(self, text="LOGIN", command=lambda:callback4(e1.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=960,y=525,anchor="e",height=50,width=500)
        tk.Label(self, text="INVALID LOGIN...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=600)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageTen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,pwd):
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataTea WHERE Id='%s' and Pass='%s'"%(id,pwd))
            isRecordExist2=0
            rows = cursor.fetchall()    
            for row in rows:
                name=row[1]
                isRecordExist2=1
            if(isRecordExist2!=1):
                master.switch_frame(PageTen)
            else:
                globals()['name']=name
                master.switch_frame(PageFour)

        tk.Label(self, text="FACULTY LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Faculty Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        tk.Button(self, text="LOGIN", command=lambda: callback4(e1.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=525,anchor="e",height=50,width=500)
        tk.Button(self, text="SIGNUP", command=lambda :master.switch_frame(PageTwelve),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=525,anchor="e",height=50,width=500)
        tk.Label(self, text="INVALID LOGIN...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=600)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageEleven(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,pwd):
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id,pwd))
            isRecordExist2=0
            rows = cursor.fetchall()    
            for row in rows:
                name=row[1]
                isRecordExist2=1
            if(isRecordExist2!=1):
                master.switch_frame(PageEleven)
            else:
                globals()['name']=name
                globals()['id']=id
                master.switch_frame(PageSeven)

        tk.Label(self, text="STUDENT LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Student Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        tk.Button(self, text="LOGIN", command=lambda: callback4(e1.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=525,anchor="e",height=50,width=500)
        tk.Button(self, text="SIGNUP", command=lambda :master.switch_frame(PageSixteen),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=525,anchor="e",height=50,width=500)
        tk.Label(self, text="INVALID LOGIN...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=600)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageTwelve(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,name,pwd):
            id1=""
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataTea WHERE Id='%s'"%(id))
            rows = cursor.fetchall()    
            for row in rows:
                id1=row[0]
            if(id=='' or name=='' or pwd=='' or id==id1):
                master.switch_frame(PageFifteen)
            else:
                conn=sqlite3.connect("facedatabase.db")
                cursor=conn.cursor()
                cursor.execute("INSERT INTO DataTea(Id,Name,Pass) VALUES('%s','%s','%s')"%(id,name,pwd))
                conn.commit()
                cursor.close()
                master.switch_frame(PageThirteen)

        tk.Label(self, text="FACULTY SIGNUP ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Faculty Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Name:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e3 = Entry(master,width=20,font=("Courier", 50))
        e3.pack()
        e3.place(x = 685, y = 398)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=500)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 498)
        tk.Button(self, text="LOGIN", command=lambda: master.switch_frame(PageThree),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=625,anchor="e",height=50,width=500)
        tk.Button(self, text="SIGNUP", command=lambda :callback4(e1.get(),e3.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=625,anchor="e",height=50,width=500)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(PageThree),height=80,width=90).place_configure(x=30,y=15)

class PageThirteen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,pwd):
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataTea WHERE Id='%s' and Pass='%s'"%(id,pwd))
            isRecordExist2=0
            rows = cursor.fetchall()    
            for row in rows:
                name=row[1]
                isRecordExist2=1
            if(isRecordExist2!=1):
                master.switch_frame(PageTen)
            else:
                globals()['name']=name
                master.switch_frame(PageFour)

        tk.Label(self, text="FACULTY LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Faculty Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        tk.Button(self, text="LOGIN", command=lambda:callback4(e1.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=525,anchor="e",height=50,width=500)
        tk.Button(self, text="SIGNUP", command=lambda :master.switch_frame(PageTwelve),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=525,anchor="e",height=50,width=500)
        tk.Label(self, text="ACCOUNT CREATED. PLEASE LOGIN...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=600)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageFourteen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)
        
        tk.Label(master, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((550, 450), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=710, y=210)

        load1 = Image.open("logout.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        tk.Label(master, text="   STEPS   \n\n1. Dataset Creation\n\n2. Dataset Training\n\n3. Face Recognizer" ,fg="#e8edf3",bg="#22264b",width=20,height=8,font=("Courier", 50),anchor="center").place_configure(x=50,y=230)
        tk.Label(master, text="Welcome ",fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)
        tk.Label(master, text="Enter ID No.:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=700)

        e3 = tk.Entry(master,width=20,font=("Courier", 50))
        e3.pack()
        e3.place(x = 685, y = 698)

        def callback():
            if(e3.get()==''):
                master.switch_frame(PageFourteen)
            else:
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

            tk.Label(self, text="Datasets are Trained...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=880)  

        tk.Button(self, text="DATASET COLLECTION", command=callback,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=950,y=830,anchor="e",height=50,width=500)
        tk.Button(master,image=render1,command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)
        tk.Label(self, text="Please Enter Id...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=880)

class PageFifteen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,name,pwd):
            id1=""
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataTea WHERE Id='%s'"%(id))
            rows = cursor.fetchall()    
            for row in rows:
                id1=row[0]
            if(id=='' or name=='' or pwd=='' or id==id1):
                master.switch_frame(PageFifteen)
            else:
                conn=sqlite3.connect("facedatabase.db")
                cursor=conn.cursor()
                cursor.execute("INSERT INTO DataTea(Id,Name,Pass) VALUES('%s','%s','%s')"%(id,name,pwd))
                conn.commit()
                cursor.close()
                master.switch_frame(PageThirteen)

        tk.Label(self, text="FACULTY SIGNUP ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Faculty Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Name:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e3 = Entry(master,width=20,font=("Courier", 50))
        e3.pack()
        e3.place(x = 685, y = 398)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=500)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 498)
        tk.Button(self, text="LOGIN", command=lambda: master.switch_frame(PageThree),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=625,anchor="e",height=50,width=500)
        tk.Label(self, text="INVALID CREDENTIALS...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=700)
        tk.Button(self, text="SIGNUP", command=lambda :callback4(e1.get(),e3.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=625,anchor="e",height=50,width=500)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(PageThree),height=80,width=90).place_configure(x=30,y=15)

class PageSixteen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,name,pwd):
            id1=""
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataStud WHERE Id='%s'"%(id))
            rows = cursor.fetchall()    
            for row in rows:
                id1=row[0]
            if(id=='' or name=='' or pwd=='' or id==id1):
                master.switch_frame(PageEighteen)
            else:
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
                master.switch_frame(PageSeventeen)

        tk.Label(self, text="STUDENT SIGNUP ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Student Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Name:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e3 = Entry(master,width=20,font=("Courier", 50))
        e3.pack()
        e3.place(x = 685, y = 398)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=500)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 498)
        tk.Button(self, text="LOGIN", command=lambda: master.switch_frame(PageSix),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=625,anchor="e",height=50,width=500)
        tk.Button(self, text="SIGNUP", command=lambda :callback4(e1.get(),e3.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=625,anchor="e",height=50,width=500)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(PageSix),height=80,width=90).place_configure(x=30,y=15)

class PageSeventeen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,pwd):
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataStud WHERE Id='%s' and Pass='%s'"%(id,pwd))
            isRecordExist2=0
            rows = cursor.fetchall()    
            for row in rows:
                name=row[1]
                isRecordExist2=1
            if(isRecordExist2!=1):
                master.switch_frame(PageEleven)
            else:
                globals()['name']=name
                master.switch_frame(PageSeven)

        tk.Label(self, text="STUDENT LOGIN ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Student Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 398)
        tk.Button(self, text="LOGIN", command=lambda:callback4(e1.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=525,anchor="e",height=50,width=500)
        tk.Button(self, text="SIGNUP", command=lambda :master.switch_frame(PageSixteen),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=525,anchor="e",height=50,width=500)
        tk.Label(self, text="ACCOUNT CREATED. PLEASE LOGIN...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=600)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageEighteen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        load = Image.open("back3.png")
        load = load.resize((70, 70), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        def callback4(id,name,pwd):
            id1=""
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM DataStud WHERE Id='%s'"%(id))
            rows = cursor.fetchall()    
            for row in rows:
                id1=row[0]
            if(id=='' or name=='' or pwd=='' or id==id1):
                master.switch_frame(PageEighteen)
            else:
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
                master.switch_frame(PageSeventeen)

        tk.Label(self, text="STUDENT SIGNUP ACCOUNT",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        tk.Label(self, text="Enter Student Id:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=300)
        e1 = tk.Entry(master,width=20,font=("Courier", 50))
        e1.pack()
        e1.place(x = 685, y = 298)
        tk.Label(self, text="Enter Name:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=400)
        e3 = Entry(master,width=20,font=("Courier", 50))
        e3.pack()
        e3.place(x = 685, y = 398)
        tk.Label(self, text="Enter Password:",fg="#22264b",bg="#e8edf3",width=20,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=500)
        e2 = tk.Entry(master,width=20,font=("Courier", 50),show="*")
        e2.pack()
        e2.place(x = 685, y = 498)
        tk.Button(self, text="LOGIN", command=lambda: master.switch_frame(PageSix),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=660,y=625,anchor="e",height=50,width=500)
        tk.Label(self, text="INVALID CREDENTIALS...",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=700)
        tk.Button(self, text="SIGNUP", command=lambda :callback4(e1.get(),e3.get(),e2.get()),relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1200,y=625,anchor="e",height=50,width=500)
        tk.Button(self,image=render,text="BACK",command=lambda: master.switch_frame(PageSix),height=80,width=90).place_configure(x=30,y=15)

class PageNineteen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        tk.Label(self, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((750, 650), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=310, y=120)

        load1 = Image.open("logout.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        tk.Label(self, text="Subject:",fg="#22264b",bg="#e8edf3",width=15,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=830)

        OptionList = ["Please Select Subject","Information Security","Software Engineering","Theory of Computation","Advance Java","Mini Project","Electronics Communication"]
        variable = StringVar(self)
        variable.set(OptionList[0])

        def callback9():
            a=variable.get()
            globals()['sub']=a
            if(sub=="Please Select Subject"):
                master.switch_frame(PageNineteen)
            else:
                master.switch_frame(PageEight)

        opt = tk.OptionMenu(master, variable,*OptionList)
        opt.config(width=24,font=("Courier", 40))
        opt.pack(side="top",pady=20)
        opt.place(x = 545, y = 835)

        tk.Label(self, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)
        tk.Button(self, text="GO", command=callback9,relief=RAISED,width=2,fg="#22264b",bg='#e6cf8b',font=("Courier", 20)).place_configure(x=1325,y=860,anchor="e",height=50,width=100)
        tk.Label(self, text="Please Select a Subject...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=910)  
        tk.Button(master,image=render1,command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageTwenty(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)
        globals()['sub']=""

        tk.Label(self, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((750, 650), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=310, y=120)

        load1 = Image.open("logout.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        tk.Label(self, text="Subject:",fg="#22264b",bg="#e8edf3",width=15,height=1,font=("Courier", 50),anchor="center").place_configure(x=35,y=830)

        OptionList = ["Please Select Subject","Information Security","Software Engineering","Theory of Computation","Advance Java","Mini Project","Electronics Communication"]
        variable = StringVar(self)
        variable.set(OptionList[0])

        def callback9():
            a=variable.get()
            globals()['sub']=a
            if(sub=="Information Security"):
                sub2="IS"
            elif(sub=="Software Engineering"):
                sub2="SE"           
            elif(sub=="Theory of Computation"):
                sub2="TOC"
            elif(sub=="Advance Java"):
                sub2="ADVJAVA"
            elif(sub=="Mini Project"):
                sub2="MIPRO"
            elif(sub=="Electronics Communication"):
                sub2="EL"
            if(sub=="Please Select Subject"):
                master.switch_frame(PageTwenty)
            else:
                conn=sqlite3.connect("facedatabase.db")
                conn.row_factory = sqlite3.Row
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM '"+sub2+"'")
                colnames = cursor.description
                con=len(colnames)
                for row in colnames:
                    if(str(row[0])==str(date.today())):
                        globals()['b']=1
                    else:
                        globals()['b']=0
                    if(b==1):
                        master.switch_frame(PageTwentyOne)
                    else:
                        master.switch_frame(PageFive)
                conn.commit()
                cursor.close()

        opt = tk.OptionMenu(master, variable,*OptionList)
        opt.config(width=24,font=("Courier", 40))
        opt.pack(side="top",pady=20)
        opt.place(x = 545, y = 835)

        tk.Label(self, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)
        tk.Button(self, text="GO", command=callback9,relief=RAISED,width=2,fg="#22264b",bg='#e6cf8b',font=("Courier", 20)).place_configure(x=1325,y=860,anchor="e",height=50,width=100)
        tk.Label(self, text="Please Select a Subject...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=910)  
        tk.Button(master,image=render1,command=lambda: master.switch_frame(StartPage),height=80,width=90).place_configure(x=30,y=15)

class PageTwentyOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#b56969")
        tk.Label(self, text="", font=('Helvetica', 18, "bold")).pack(side="top",padx=700,pady=700)

        tk.Label(self, text="ATTENDANCE USING FACE RECOGNITION",fg="#e8edf3",bg="#22264b",width=44,height=2,font=("Courier", 50),anchor="center").place_configure(x=0,y=0)
        load = Image.open("mainpic.jpg")
        load = load.resize((750, 650), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        globals()['d']=b

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=310, y=120)
        #img.place(x=20, y=160)

        load1 = Image.open("back3.png")
        load1 = load1.resize((70, 70), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)

        img1 = tk.Label(self, image=render1)
        img1.image = render1

        tk.Label(self, text="Welcome "+name ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=120)

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
            file.write("S_No."+"  ")
            for row in colnames:
                file.write(row[0]+" ")
            file.write("Total_Present ")
            file.write("Total_Absent")
            conn.commit()
            cursor.close()
            file.close()
            file = open('Attend/'+sub2+'.xls','a')
            conn=sqlite3.connect("facedatabase.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM '"+sub2+"'")
            rows = cursor.fetchall()
            file.write("\n")
            co=0
            cu=1
            for row in rows:
                file.write(str(cu)+"       ")
                file.write(row[0]+" "+row[1]+"   "+row[2])
                j=3
                while(j<con):
                    file.write("          "+row[j])
                    if(row[j]=="P"):
                        co+=1
                    j+=1
                file.write("    "+str(co))
                file.write("              "+str(con-3-co))
                co=0
                cu+=1
                file.write("\n")
            conn.commit()
            cursor.close()
            file.close()
            filename="Attend/"+sub2+".xls"
            webbrowser.open('file://' + os.path.realpath(filename),new=1)

        tk.Button(self, text="VIEW ATTENDANCE", command=callback8,relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=635,y=875,anchor="e",height=50,width=500)
        tk.Button(self,state=DISABLED, text="TAKE ATTENDANCE",relief=RAISED,width=20,fg="#22264b",bg='#e6cf8b',font=("Courier", 30)).place_configure(x=1235,y=875,anchor="e",height=50,width=500)
        tk.Label(self, text="Subject: "+sub1 ,fg="#e8edf3",bg="#22264b",width=44,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=178)
        tk.Label(self, text="Attendance Taken...",fg="#e8edf3",bg="#22264b",width=45,height=1,font=("Courier", 50),anchor="center").place_configure(x=0,y=910) 
        tk.Button(self,image=render1,text="BACK",command=lambda: master.switch_frame(PageFour),height=80,width=90).place_configure(x=30,y=15)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()