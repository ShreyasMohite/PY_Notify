from tkinter import *
from tkinter.ttk import Combobox
from notify_run import Notify
import tkinter.messagebox
import threading

class Notifies:
    def __init__(self,root):
        self.root=root
        self.root.title("Push Notifications to mobile")
        self.root.geometry("500x500")
        self.root.iconbitmap("logo838.ico")
        self.root.resizable(0,0)


        send_by=StringVar()
        url=StringVar()
    
    #=============================================================#
        def on_enter1(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave1(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter2(e):
            but_push_notification['background']="black"
            but_push_notification['foreground']="cyan"
  
        def on_leave2(e):
            but_push_notification['background']="SystemButtonFace"
            but_push_notification['foreground']="SystemButtonText"

    #================================================================#
        def Clear():
            txt.delete("1.0","end")
            send_by.set("Only Message")
            url.set("")


        def send_messages():
            try:
                if send_by.get()=="Only Message":
                    if txt.get("1.0","end")!="":
                        notify = Notify()
                        notify.send(txt.get("1.0","end"))
                    else:
                        tkinter.messagebox.showerror("Error","Please enter Message")
                
                if send_by.get()=="Message and url":
                    if txt.get("1.0","end")!="" and url.get()!="":
                        notify = Notify()
                        mess=txt.get("1.0","end")
                        urls=url.get()
                        #notify.send('Click to open notify.run!', 'https://notify.run')
                        notify.send(mess, urls)
                    elif url.get()=="":
                        tkinter.messagebox.showerror("Error","Please Enter Url")
                    elif txt.get("1.0","end")=="":
                        tkinter.messagebox.showerror("Error","Please Enter Message")
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Message And Url")
            except:
                tkinter.messagebox.showerror("Error","Network Error")

        
        def thread_message():
            t1=threading.Thread(target=send_messages)
            t1.start()

               


#============================frame===================================================#
        mainframe=Frame(self.root,width=500,height=500,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=400,relief="ridge",bd=3,bg="#023047")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=95,relief="ridge",bd=3,bg="#6d6875")
        secondframe.place(x=0,y=400)

#===================================================================================#
        
        but_clear=Button(secondframe,width=20,height=2,text="Clear",cursor="hand2",font=('times new roman',12,'bold'),command=Clear)
        but_clear.place(x=30,y=20)
        but_clear.bind("<Enter>",on_enter1)
        but_clear.bind("<Leave>",on_leave1)

        but_push_notification=Button(secondframe,width=20,height=2,text="Send",cursor="hand2",font=('times new roman',12,'bold'),command=thread_message)
        but_push_notification.place(x=270,y=20)
        but_push_notification.bind("<Enter>",on_enter2)
        but_push_notification.bind("<Leave>",on_leave2)

#===================================================================================#
        
        lab_message=Label(firstframe,text="Enter Message",font=('times new roman',12),bg="#023047",fg="white")
        lab_message.place(x=200,y=10)


        txt=Text(firstframe,width=55,height=8,font=('times new roman',12))
        txt.place(x=20,y=50)

        lab_message_by=Label(firstframe,text="Send Message By :",font=('times new roman',12),bg="#023047",fg="white")
        lab_message_by.place(x=20,y=240)

        v=["Only Message","Message and url"]
        combo1=Combobox(firstframe,values=v,font=('arial',12),width=15,state="readonly",textvariable=send_by)
        combo1.set("Only Message")
        combo1.place(x=190,y=240)


        lab_url=Label(firstframe,text="Enter Url:",font=('times new roman',12),bg="#023047",fg="white")
        lab_url.place(x=200,y=300)

        ent_url=Entry(firstframe,width=50,relief="ridge",font=('times new roman',14),bd=3,textvariable=url)
        ent_url.place(x=15,y=345)
#====================================================================================#



if __name__ == "__main__":
    root=Tk()
    app=Notifies(root)
    root.mainloop()