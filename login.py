import csv 
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
from menu import Menu


def main():
    root = Tk()
    app= MainWindow(root)
#MAIN WINDOW FOR LOG IN
class MainWindow:
    def __init__(self,master):
        def show_password():
            if self.lblPassword.cget('show') =="*":
                self.lblPassword.config(show='')
            else:
                self.lblPassword.config(show='*')

        # public data mambers
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="darkred")
        self.frame = Frame(self.master,bg="darkred")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text = "HOSPITAL MANAGEMENT SYSTEM", font="Bodoni 20 bold",bg="white",fg="black")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=40)
        #==========Owners======
        self.Owners = Label(self.frame,text ="Project done by Abram, Nikhil and Aarif",font="Bodoni 10 bold",bg="darkred")
        self.Owners.grid(row=5,column=0,columnspan=2,padx=20,pady=10)

        #======================
        self.LoginFrame1 = Frame(self.frame,width=400,height=80,relief="ridge",bg="white",bd=20)
        self.LoginFrame1.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="white",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #======LABEL AND ENTRY=========
        self.lblUsername = Label(self.LoginFrame1,text="Username",font="Helvetica 14 bold",bg="white",bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.lblUsername = Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable= self.Username,bd=2)
        self.lblUsername.grid(row=0,column=1)
        self.lblPassword = Label(self.LoginFrame1,text="Password ",font="Helvetica 14 bold",bg="white",bd=22)
        self.lblPassword .grid(row=1,column=0)
        self.lblPassword  = Entry(self.LoginFrame1,font="Helvetica 14 bold",show="*",textvariable= self.Password,bd=2)
        self.lblPassword .grid(row=1,column=1)
        #===========BUTTONS====
        self.btnLogin = Button(self.LoginFrame2,text = "Login" ,font="Helvetica 10 bold", width =10 ,bg="white",command = self.Login_system)
        self.btnLogin.grid(row=3,column=0)
        
        self.btnCreate= Button(self.LoginFrame2,text = "Create ID" ,font="Helvetica 10 bold", width =10 ,bg="white",command = self.idcreate)
        self.btnCreate.grid(row=3,column=1)
       
        self.btnExit = Button(self.LoginFrame2,text = "Exit" ,font="Helvetica 10 bold", width =10 ,bg="white",command = self.Exit)
        self.btnExit.grid(row=3,column=2)

        self.btnshow = Checkbutton(self.LoginFrame1,text="Show Password",command=show_password)
        self.btnshow.grid(row=1,column=2)
        


    # public member function  
    #Function for LOGIN
    def Login_system(self):

        S1=(self.Username.get())
        S2=(self.Password.get())
        cnt=0
        f=open("ID.csv","r")
        wr=csv.reader(f)    
        for row in wr:
            if S1 == "1":
                if S2 == "2":    
                    cnt+=1
                else:
                    cnt+=0
        if cnt==0:
                tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM" , "PLEASE ENTER VALID USERNAME AND PASSWORD")
        else:
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow) 
    def idcreate(self):
        S1=(self.Username.get())
        S2=(self.Password.get())
        f=open("ID.csv","a")
        wr=csv.writer(f)
        id=[S1,S2]
        wr.writerow(id)
        tkinter.messagebox.askokcancel("HOSPITAL MANAGEMENT SYSTEM" , "ID CREATED")

    #Function for Exit
    def Exit(self):
        self.master.destroy()

if __name__ == "__main__":
    main()
mainloop()










