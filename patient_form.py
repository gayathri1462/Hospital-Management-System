from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3


conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")
                      
#Class for PATIENT REGISTRATION 
class Patient:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.pat_ID=IntVar()
        self.pat_name=StringVar()
        self.pat_dob=StringVar()
        self.pat_address=StringVar()
        self.pat_sex=StringVar()
        self.pat_BG=StringVar()
        self.pat_email=StringVar()
        self.pat_contact=IntVar()
        self.pat_contactalt=IntVar()
        self.pat_CT=StringVar()


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "PATIENT REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpatid.grid(row=0,column=1)
        
        self.lblPatname = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblPatname.grid(row=1,column=0)
        self.lblPatname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_name)
        self.lblPatname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.lblsex  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_sex)
        self.lblsex.grid(row=2,column=1)

        self.lblDOB = Label(self.LoginFrame,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblDOB.grid(row=3,column=0)
        self.lblDOB  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_dob)
        self.lblDOB.grid(row=3,column=1)
        
        self.lblbgrp = Label(self.LoginFrame,text="BLOOD GROUP",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblbgrp.grid(row=4,column=0)
        self.lblbgrp  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_BG)
        self.lblbgrp.grid(row=4,column=1)
        
        self.lblCon = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contact)
        self.lblCon.grid(row=0,column=3)
        
        self.lblAlt = Label(self.LoginFrame,text="ALTERNATE CONTACT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblAlt.grid(row=1,column=2)
        self.lblAlt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contactalt)
        self.lblAlt.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_email)
        self.lbleid.grid(row=2,column=3)

        self.lbldoc = Label(self.LoginFrame,text="CONSULTING TEAM / DOCTOR",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldoc.grid(row=3,column=2)
        self.lbldoc  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_CT)
        self.lbldoc.grid(row=3,column=3)

        self.lbladd = Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbladd.grid(row=4,column=2)
        self.lbladd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_address)
        self.lbladd.grid(row=4,column=3)
        
        #===========BUTTONS============= 
        self.button2 = Button(self.LoginFrame2, text="SUBMIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_PAT)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.UPDATE_PAT)
        self.button3.grid(row=3,column=2)
        
        self.button4 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.D_DISPLAY)
        self.button4.grid(row=3,column=3)
        
        self.button5 = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.S_DISPLAY)
        self.button5.grid(row=3,column=4)
        
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=5)
            

    #FUNCTION TO INSERT DATA IN PATIENT FORM
    def INSERT_PAT(self):
        global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
        conn=sqlite3.connect("HospitalDB.db")
        conn.cursor()
        p1=(self.pat_ID.get())
        p2=(self.pat_name.get())
        p3=(self.pat_sex.get())
        p4=(self.pat_BG.get())
        p5=(self.pat_dob.get())
        p6=(self.pat_contact.get())
        p7=(self.pat_contactalt.get())
        p8=(self.pat_address.get())
        p9=(self.pat_CT.get())
        p10=(self.pat_email.get())
        p = list(conn.execute("SELECT * FROM PATIENT  WHERE PATIENT_ID =?",(p1,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT_ID ALREADY EXISTS")
        else:
            conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(p1,p2,p3,p4,p5,p8,p9,p10,))
            conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)',(p1,p6,p7,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM","DETAILS INSERTED INTO DATABASE")
        conn.commit()
        
    #FUNCTION TO UPDATE DATA IN PATIENT FORM

    def UPDATE_PAT(self):
        global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
        conn.cursor()
        u1 = (self.pat_ID.get())
        u2 = (self.pat_name.get())
        u3 = (self.pat_sex.get())
        u4 = (self.pat_dob.get())
        u5 = (self.pat_BG.get())
        u6 = (self.pat_contact.get())
        u7 = (self.pat_contactalt.get())
        u8 = (self.pat_email.get())
        u9 = (self.pat_CT.get())
        u10 = (self.pat_address.get())
        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("Select * from PATIENT where PATIENT_ID=?", (u1,)))
        if len(p) != 0:
            conn.execute('UPDATE PATIENT SET NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,ADDRESS=?,CONSULT_TEAM=?,EMAIL=? where PATIENT_ID=?', ( u2, u3, u4, u5, u10, u9, u8,u1,))
            conn.execute('UPDATE CONTACT_NO set CONTACTNO=?,ALT_CONTACT=? WHERE PATIENT_ID=?', ( u6, u7,u1,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS UPDATED INTO DATABASE")
            conn.commit()

        else:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")
            
    #FUNCTION TO EXIT PATIENT REGISTRATION WINDOW
    def Exit(self):            
        self.master.destroy()

    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def D_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DMenu(self.newWindow)
        
    #FUNCTION TO OPEN SEARCH PATIENT DISPLAY WINDOW
    def S_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SMenu(self.newWindow)

#CLASS FOR DISPLAY MENU FOR DELETE PATIENT
class DMenu:
    def __init__(self,master):    
        global inp_d,entry1,DeleteB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.del_pid=IntVar()
        self.lblTitle = Label(self.frame,text = "DELETE WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.del_pid)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_PAT)
        self.DeleteB.grid(row=3,column=1)

    #FUNCTION TO DELETE DATA IN PATIENT FORM
    def DELETE_PAT(self):        
        global inp_d,del_pid
        c1= conn.cursor()
        inp_d = (self.del_pid.get())
        p=list(conn.execute("select * from PATIENT where PATIENT_ID=?", (inp_d,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
        else:
            conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(inp_d,))
            conn.execute('DELETE FROM CONTACT_NO WHERE PATIENT_ID=?', (inp_d,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS DELETED FROM DATABASE")
            conn.commit()

#CLASS FOR SEARCH MENU FOR SEARCH PATIENT
class SMenu:
    def __init__(self,master):    
        global inp_s,s_pid,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.s_pid=IntVar()
        self.lblTitle = Label(self.frame,text = "SEARCH WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.s_pid)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_PAT)
        self.SearchB.grid(row=0,column=1)
        
    #FUNCTION TO SEARCH DATA IN PATIENT FORM
    def SEARCH_PAT(self):
        global inp_s,s_pid,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
        c1=conn.cursor()
        inp_s=(self.s_pid.get())                
        p=list(conn.execute('select * from PATIENT where PATIENT_ID=?',(inp_s,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
                    
        else:
            t=c1.execute('SELECT * FROM PATIENT NATURAL JOIN CONTACT_NO where PATIENT_ID=?',(inp_s,));
            for i in t:
                        self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l1.grid(row=1,column=0)
                        self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                        self.dis1.grid(row=1,column=1)
                        
                        self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l2.grid(row=2,column=0)
                        self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                        self.dis2.grid(row=2,column=1)

                        self.l3 = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l3.grid(row=3,column=0)
                        self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                        self.dis3.grid(row=3,column=1)

                        self.l4 = Label(self.LoginFrame,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l4.grid(row=4,column=0)
                        self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[4])
                        self.dis4.grid(row=4,column=1)
                        
                        self.l5 = Label(self.LoginFrame,text="BLOOD GROUP",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l5.grid(row=5,column=0)
                        self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                        self.dis5.grid(row=5,column=1)
                        
                        self.l6 = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l6.grid(row=1,column=2)
                        self.dis6  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[8])
                        self.dis6.grid(row=1,column=3)
                        
                        self.l7 = Label(self.LoginFrame,text="ALTERNATE CONTACT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l7.grid(row=2,column=2)
                        self.dis7  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[9])
                        self.dis7.grid(row=2,column=3)
                        
                        self.l8 = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l8.grid(row=3,column=2)
                        self.dis8  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[7])
                        self.dis8.grid(row=3,column=3)

                        self.l9 = Label(self.LoginFrame,text="CONSULTING TEAM / DOCTOR",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l9.grid(row=4,column=2)
                        self.dis9  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[6])
                        self.dis9.grid(row=4,column=3)

                        self.l10 = Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l10.grid(row=5,column=2)
                        self.dis10 = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[5])
                        self.dis10.grid(row=5,column=3)
                
      
