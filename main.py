from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from time import strftime
from datetime import datetime
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System :
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recognition System")
         
         
         #bg image
         img1 = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/extra.jpg")
         img1 = img1.resize((1540,800), Image.Resampling.LANCZOS)
         self.photoimg1 = ImageTk.PhotoImage(img1)

         bg_img=Label(self.root,image=self.photoimg1)
         bg_img.place(x=0,y=0,width=1540,height=800)


         #title
         title_lbl=Label(bg_img, text="WELCOME TO FACIAL RECOGNITION BASED ATTENDANCE SYSTEM",font=("cambria",35,"bold"),bg="indigo",fg="white")
         title_lbl.place(x=0,y=0,width=1540,height=60)


         b1_1=Button(bg_img,text="CREATE DATASET",cursor="hand2",command=self.student_detail,font=("cambria",20,"bold"),bg="white",fg="dark blue")
         b1_1.place(x=70,y=220,width=500,height=50)

         
         b1_1=Button(bg_img,text="TRAIN DATASET",cursor="hand2",command=self.train_data,font=("cambria",20,"bold"),bg="white",fg="dark blue")
         b1_1.place(x=70,y=310,width=500,height=50)


         b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("cambria",20,"bold"),bg="white",fg="dark blue")
         b1_1.place(x=70,y=400,width=500,height=50)


         b1_1=Button(bg_img,text="ATTENDANCE SHEET",cursor="hand2",command=self.attendance_data,font=("cambria",20,"bold"),bg="white",fg="dark blue")
         b1_1.place(x=70,y=490,width=500,height=50)


         b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("cambria",20,"bold"),bg="white",fg="dark blue")
         b1_1.place(x=70,y=580,width=500,height=50)


    def open_img(self):
        os.startfile("data")

    
    #Exit function
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit the application?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


    #function buttons
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    #Train function buttons
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    #face data function buttons
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    #attendance function buttons
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    
if __name__ == "__main__":
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()