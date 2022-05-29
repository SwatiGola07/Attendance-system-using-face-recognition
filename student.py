from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student :
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Recognition System")

         #variables
         self.var_dep=StringVar()
         self.var_year=StringVar()
         self.var_semester=StringVar()
         self.va_std_id=StringVar()
         self.var_std_name=StringVar()
         self.var_gender=StringVar()
         self.var_dob=StringVar()
         self.var_phone=StringVar()
         self.var_address=StringVar()
         self.var_email=StringVar()


         #bg image
         img1 = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/bg2.png")
         img1 = img1.resize((1540,800), Image.Resampling.LANCZOS)
         self.photoimg1 = ImageTk.PhotoImage(img1)

         bg_img=Label(self.root,image=self.photoimg1)
         bg_img.place(x=0,y=0,width=1540,height=800)


         #title
         title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",font=("cambria",35,"bold"),bg="sky blue",fg="black")
         title_lbl.place(x=0,y=0,width=1540,height=55)


         main_frame=Frame(bg_img,bd=2,bg="white")
         main_frame.place(x=15,y=65,width=1495,height=680)


         #left label frame
         Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("cambria",15,"bold"))
         Left_frame.place(x=20,y=10,width=710,height=668)

         img_left = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/img1.png")
         img_left = img_left.resize((682,140), Image.Resampling.LANCZOS)
         self.photoimg_left = ImageTk.PhotoImage(img_left)

         f_lbl=Label(Left_frame,image=self.photoimg_left)
         f_lbl.place(x=10,y=0,width=682,height=140)

         #current course information
         current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("cambria",15,"bold"))
         current_course_frame.place(x=10,y=150,width=682,height=130)


         #Department
         dep_label=Label(current_course_frame,text="Department",font=("cambria",14),bg="white")
         dep_label.grid(row=0,column=0,padx=10,sticky=W)

         dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("cambria",12),state="readonly")
         dep_combo["values"]=("Select Department","CSAI","CSE","IT","ECE","Mechanical")
         dep_combo.current(0)
         dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


         #Year
         year_label=Label(current_course_frame,text="Year",font=("cambria",14),bg="white")
         year_label.grid(row=1,column=0,padx=10,sticky=W)

         year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("cambria",12),state="readonly")
         year_combo["values"]=("Select Year","1st Year","2nd Year","3rd Year","4th Year")
         year_combo.current(0)
         year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


         #Semester
         semester_label=Label(current_course_frame,text="Semester",font=("cambria",14),bg="white")
         semester_label.grid(row=1,column=2,padx=10,sticky=W)

         semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("cambria",12),state="readonly")
         semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
         semester_combo.current(0)
         semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


         #class student information
         class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("cambria",15,"bold"))
         class_Student_frame.place(x=10,y=295,width=682,height=330)


         #Student Id
         studentId_label=Label(class_Student_frame,text="Student ID:",font=("cambria",14),bg="white")
         studentId_label.grid(row=0,column=0,padx=10,sticky=W)

         studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=20,font=("cambria",12))
         studentId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)


         #Student DOB
         dob_label=Label(class_Student_frame,text="DOB:",font=("cambria",14),bg="white")
         dob_label.grid(row=0,column=2,padx=10, pady=10,sticky=W)

         dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=12,font=("cambria",12))
         dob_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)


         #Student name
         studentName_label=Label(class_Student_frame,text="Student Name:",font=("cambria",14),bg="white")
         studentName_label.grid(row=1,column=0,padx=10, pady=10,sticky=W)

         studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("cambria",12))
         studentName_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)


         #Student Gender
         gender_label=Label(class_Student_frame,text="Gender:",font=("cambria",14),bg="white")
         gender_label.grid(row=1,column=2,padx=10, pady=10,sticky=W)

         gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=11,font=("cambria",12),state="readonly")
         gender_combo["values"]=("Select Gender","Male","Female","Other")
         gender_combo.current(0)
         gender_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


         #Student Phone no
         phone_label=Label(class_Student_frame,text="Phone No:",font=("cambria",14),bg="white")
         phone_label.grid(row=2,column=0,padx=10, pady=10,sticky=W)

         phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("cambria",12))
         phone_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)


         #Student Address
         address_label=Label(class_Student_frame,text="Address:",font=("cambria",14),bg="white")
         address_label.grid(row=2,column=2,padx=10, pady=10,sticky=W)

         address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=12,font=("cambria",12))
         address_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)


         #Student Email
         email_label=Label(class_Student_frame,text="Email:",font=("cambria",14),bg="white")
         email_label.grid(row=3,column=0,padx=10, pady=10,sticky=W)

         email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=30,font=("cambria",12))
         email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)


         #radio buttons
         self.var_radio1=StringVar()
         radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
         radiobtn1.grid(row=5,column=0)

         radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
         radiobtn2.grid(row=5,column=1)

         #buttons frame
         btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
         btn_frame.place(x=4,y=221,width=670,height=36)

         save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("cambria",13 ,"bold"),width=16,bg="light blue",fg="black")
         save_btn.grid(row=0,column=0)

         update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("cambria",13 ,"bold"),width=16,bg="light blue",fg="black")
         update_btn.grid(row=0,column=1)

         delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("cambria",13 ,"bold"),width=16,bg="light blue",fg="black")
         delete_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("cambria",13 ,"bold"),width=16,bg="light blue",fg="black")
         reset_btn.grid(row=0,column=3)
         

         #buttons frame 2
         btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
         btn_frame1.place(x=4,y=259,width=670,height=36)

         take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,font=("cambria",13 ,"bold"),width=33,bg="light blue",fg="black")
         take_photo_btn.grid(row=0,column=0)

         update_photo_btn=Button(btn_frame1,text="Update Photo Sample",font=("cambria",13 ,"bold"),width=33,bg="light blue",fg="black")
         update_photo_btn.grid(row=0,column=1)
          

         #right label frame
         Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Records",font=("cambria",15,"bold"))
         Right_frame.place(x=745,y=10,width=720,height=668)

         img_right = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/rtfr.jpg")
         img_right = img_right.resize((690,140), Image.Resampling.LANCZOS)
         self.photoimg_right = ImageTk.PhotoImage(img_right)

         f_lbl=Label(Right_frame,image=self.photoimg_right)
         f_lbl.place(x=10,y=0,width=690,height=140)


         #table frame
         table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
         table_frame.place(x=10,y=164,width=683,height=470)

         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.student_table=ttk.Treeview(table_frame,column=("dep","year","sem","id","name","dob","gender","phone","address","email","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)

         self.student_table.heading("dep",text="Department")
         self.student_table.heading("year",text="Year")
         self.student_table.heading("sem",text="Semester")
         self.student_table.heading("id",text="Student Id")
         self.student_table.heading("name",text="Student Name")
         self.student_table.heading("dob",text="DOB")
         self.student_table.heading("gender",text="Gender")
         self.student_table.heading("phone",text="Phone No")
         self.student_table.heading("address",text="Address")
         self.student_table.heading("email",text="Email")
         self.student_table.heading("photo",text="PhotoSampleStatus")
         self.student_table["show"]="headings"

         self.student_table.column("dep",width=100)
         self.student_table.column("year",width=100)
         self.student_table.column("sem",width=100)
         self.student_table.column("id",width=100)
         self.student_table.column("name",width=100)
         self.student_table.column("dob",width=100)
         self.student_table.column("gender",width=100)
         self.student_table.column("phone",width=100)
         self.student_table.column("address",width=100)
         self.student_table.column("email",width=170)
         self.student_table.column("photo",width=130)

         self.student_table.pack(fill=BOTH,expand=1)
         self.student_table.bind("<ButtonRelease>",self.get_cursor)
         self.fetch_data()

    #Function declaration
    def add_data(self):
        if (self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="112233",database="recognitionface")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.va_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_radio1.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    
    
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="112233",database="recognitionface")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_year.set(data[1])
        self.var_semester.set(data[2])
        self.va_std_id.set(data[3])
        self.var_std_name.set(data[4])
        self.var_dob.set(data[5])
        self.var_gender.set(data[6])
        self.var_phone.set(data[7])
        self.var_address.set(data[8])
        self.var_email.set(data[9])
        self.var_radio1.set(data[10])


    #update button function
    def update_data(self):
        if (self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the data?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="112233",database="recognitionface")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Year=%s,Semester=%s,Name=%s,DOB=%s,Gender=%s,Phone=%s,Address=%s,Email=%s,PhotoSample=%s where student_id=%s",(

                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get()                         
                    ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Data Updated",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Page","Do you want to delete this student detail",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="112233",database="recognitionface")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted the data",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")
    

    #Generate data set and take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="112233",database="recognitionface")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Year=%s,Semester=%s,Name=%s,DOB=%s,Gender=%s,Phone=%s,Address=%s,Email=%s,PhotoSample=%s where student_id=%s",(

                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get()==id+1                       
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined face from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets completed!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
