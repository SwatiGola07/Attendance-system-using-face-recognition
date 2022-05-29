from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance :
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Attendance Sheet")


         #text variables
         self.var_atten_id=StringVar()
         self.var_atten_name=StringVar()
         self.var_atten_date=StringVar()
         self.var_atten_time=StringVar()
         self.var_atten_dep=StringVar()
         self.var_atten_attendance=StringVar()


         #bg image
         img1 = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/bg2.png")
         img1 = img1.resize((1540,800), Image.Resampling.LANCZOS)
         self.photoimg1 = ImageTk.PhotoImage(img1)

         bg_img=Label(self.root,image=self.photoimg1)
         bg_img.place(x=0,y=0,width=1540,height=800)


         #title
         title_lbl=Label(bg_img, text="ATTENDANCE RECORD",font=("cambria",35,"bold"),bg="gold",fg="black")
         title_lbl.place(x=0,y=0,width=1540,height=55)


         main_frame=Frame(bg_img,bd=2,bg="white")
         main_frame.place(x=15,y=65,width=1495,height=680)

         
         #right label frame
         Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Sheet",font=("cambria",15,"bold"))
         Right_frame.place(x=20,y=10,width=1440,height=668)


         table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
         table_frame.place(x=500,y=180,width=800,height=440)


         import_btn=Button(Right_frame,text="Import Data",command=self.importCsv,font=("cambria",13 ,"bold"),bg="light blue",fg="black")
         import_btn.place(x=70,y=280,width=320,height=48)

         export_btn=Button(Right_frame,text="Export Data",command=self.exportCsv,font=("cambria",13 ,"bold"),bg="light blue",fg="black")
         export_btn.place(x=70,y=360,width=320,height=48)

         
         #scrollbar table
         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)

         scroll_x.config(command=self.AttendanceReportTable.xview)
         scroll_y.config(command=self.AttendanceReportTable.yview)

         self.AttendanceReportTable.heading("id",text="Student ID")
         self.AttendanceReportTable.heading("name",text="Name")
         self.AttendanceReportTable.heading("department",text="Department")
         self.AttendanceReportTable.heading("time",text="Time")
         self.AttendanceReportTable.heading("date",text="Date")
         self.AttendanceReportTable.heading("attendance",text="Attendance")

         self.AttendanceReportTable["show"]="headings"

         self.AttendanceReportTable.column("id",width=150)
         self.AttendanceReportTable.column("name",width=150)
         self.AttendanceReportTable.column("department",width=150)
         self.AttendanceReportTable.column("time",width=150)
         self.AttendanceReportTable.column("date",width=150)
         self.AttendanceReportTable.column("attendance",width=150)


         self.AttendanceReportTable.pack(fill=BOTH,expand=1)

         self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
 
         img_right = Image.open("C:/Users/lenovo/OneDrive/Desktop/Attendance system/college_images/1a.png")
         img_right = img_right.resize((690,150), Image.Resampling.LANCZOS)
         self.photoimg_right = ImageTk.PhotoImage(img_right)

         f_lbl=Label(Right_frame,image=self.photoimg_right)
         f_lbl.place(x=370,y=0,width=690,height=150)


    #fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    

    #import csv function
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #export csv function
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported to "+os.path.basename(fln)+" Successfully!!",parent=self.root)
        except Exception as es:
                      messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    # get cursor function
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_date.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_dep.set(rows[4])
        self.var_atten_attendance.set(rows[5])       

    
    

















if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
