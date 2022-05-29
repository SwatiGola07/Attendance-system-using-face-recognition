from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System 


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\lenovo\OneDrive\Desktop\Attendance system\images\bg3.webp")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,width=1550,height=800)

        frame=Frame(self.root,bg="black")
        frame.place(x=590,y=205,width=350,height=440)  

        img1=Image.open(r"C:\Users\lenovo\OneDrive\Desktop\Attendance system\images\user.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=720,y=210,width=100,height=100)

        get_str=Label(frame,text="GET STARTED",font=("times new roman",18,"bold"),bg="black",fg="white")
        get_str.place(x=94,y=109)


        #LABEL
        username=lbl=Label(frame,text="Username",font=("times new roman",14,"bold"),bg="black",fg="white")
        username.place(x=70,y=160)

        self.txtuser=ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.txtuser.place(x=40,y=190,width=260)

        password=lbl=Label(frame,text="Password",font=("times new roman",14,"bold"),bg="black",fg="white")
        password.place(x=70,y=235)

        self.txtpass=ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.txtpass.place(x=40,y=265,width=260)


        #icon images
        img2=Image.open(r"C:\Users\lenovo\OneDrive\Desktop\Attendance system\images\name1.png")
        img2=img2.resize((20,20),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(frame,image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=45,y=164,width=20,height=20)

        img3=Image.open(r"C:\Users\lenovo\OneDrive\Desktop\Attendance system\images\pass.png")
        img3=img3.resize((20,20),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(frame,image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=45,y=239,width=20,height=20)


        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=115,y=315,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="Create New Account",command=self.register_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=375,width=150,height=20)

        #forget password button
        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=15,y=400,width=150,height=20)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    #login button function
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtuser.get()=="Swati" and self.txtpass.get()=="gola":
            messagebox.showinfo("Success","Welcome!!",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="112233",database="recognitionface")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    #Reset password button function
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="112233",database="recognitionface")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login via new password",parent=self.root2)




    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter your Username first",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="112233",database="recognitionface")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x450+550+200")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)
                

                #FP Security questiion
                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",16,"bold"),bg="white smoke",fg="black")
                security_Q.place(x=70,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",14),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Best Friend Name")
                self.combo_security_Q.place(x=70,y=110,width=250)
                self.combo_security_Q.current(0)


                #FP Security Answer
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",16,"bold"),bg="white smoke",fg="black")
                security_A.place(x=70,y=170)

                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",14))
                self.txt_security_A.place(x=70,y=200,width=250)


                #FP new password
                new_password=Label(self.root2,text="New Password",font=("times new roman",16,"bold"),bg="white smoke",fg="black")
                new_password.place(x=70,y=260)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",14))
                self.txt_newpass.place(x=70,y=290,width=250)


                #Reset password button
                btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",14,"bold"),fg="white",bg="dark green")
                btn.place(x=125,y=355)






class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #text variables
        self.var_fname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        

        #background image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\lenovo\OneDrive\Desktop\Attendance system\images\bg3.webp")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,width=1600,height=800)



        #main frame
        frame=Frame(self.root,bg="white smoke")
        frame.place(x=400,y=165,width=797,height=522)


        register_lbl=Label(frame,text="REGISTER YOURSELF HERE !!",font=("times new roman",22,"bold"),bg="white smoke",fg="dark green")
        register_lbl.place(x=20,y=20)


        #===========entry fields==============
        #name
        fname=Label(frame,text="Name",font=("times new roman",18,"bold"),bg="white smoke",fg="black")
        fname.place(x=50,y=80)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.txt_fname.place(x=50,y=115,width=250)


        #contact
        contact=Label(frame,text="Contact No",font=("times new roman",18,"bold"),bg="white smoke",fg="black")
        contact.place(x=450,y=80)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=450,y=115,width=250)


        #email
        email=Label(frame,text="Username",font=("times new roman",18,"bold"),bg="white smoke",fg="black")
        email.place(x=50,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=50,y=205,width=250)


        #password
        password=Label(frame,text="Password",font=("times new roman",18,"bold"),bg="white smoke",fg="black")
        password.place(x=450,y=170)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=450,y=205,width=250)


        #Security Question
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",18,"bold"),bg="white smoke",fg="black")
        security_Q.place(x=50,y=260)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Best Friend Name")
        self.combo_security_Q.place(x=50,y=295,width=250)
        self.combo_security_Q.current(0)


        #Security Answer
        security_A=Label(frame,text="Security Answer",font=("times new roman",18,"bold"),bg="white smoke",fg="black")
        security_A.place(x=450,y=260)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security_A.place(x=450,y=295,width=250)


        #Check box
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the Terms & Conditions",font=("times new roman",15,"bold"),bg="white smoke",fg="black",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=350)


        #Login and Register button
        img=Image.open(r"C:\Users\lenovo\OneDrive\Desktop\Attendance system\images\register.jpg")
        img=img.resize((160,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=410,width=160,height=50)

        
    #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_password.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to the Terms & Conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="112233",database="recognitionface")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another Username",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_password.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)





if __name__=="__main__":
    main()