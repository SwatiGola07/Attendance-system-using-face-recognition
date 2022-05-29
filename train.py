from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train :
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recognition System")


         #title
         title_lbl=Label(self.root, text="TRAIN DATASET",font=("cambria",35,"bold"),bg="dark blue",fg="white")
         title_lbl.place(x=0,y=0,width=1540,height=55)
         

         #top image
         img_top = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/data.jpg")
         img_top = img_top.resize((1540,175), Image.Resampling.LANCZOS)
         self.photoimg_top = ImageTk.PhotoImage(img_top)

         f_lbl=Label(self.root,image=self.photoimg_top)
         f_lbl.place(x=0,y=55,width=1540,height=175)

         
         #button
         img_train = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/traindata.png")
         img_train = img_train.resize((250,180), Image.Resampling.LANCZOS)
         self.photoimg_train = ImageTk.PhotoImage(img_train)

         b1=Button(self.root,image=self.photoimg_train,command=self.train_classifier,cursor="hand2")
         b1.place(x=650,y=265,width=250,height=180)

         b1_1=Button(self.root,text="Train Dataset",command=self.train_classifier,cursor="hand2",font=("cambria",15,"bold"),bg="black",fg="white")
         b1_1.place(x=650,y=435,width=250,height=40)


         #bottom image
         img_bottom = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/data1.jpg")
         img_bottom = img_bottom.resize((1540,300), Image.Resampling.LANCZOS)
         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

         f_lbl=Label(self.root,image=self.photoimg_bottom)
         f_lbl.place(x=0,y=500,width=1540,height=300)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #Train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create() 
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training of datasets completed!!",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

