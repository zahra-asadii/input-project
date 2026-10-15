from tkinter import *
from tkinter import messagebox
import data

db=data.Database('c:/project/data.db')

win = Tk()
win.geometry('500x300')
win.title('login form')
# function =====================================
def add():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    
    db.insert(fname,lname,email,password)
    messagebox.showinfo('insert','record inserted')
    
def login():
    pass

#   widget ========================================


lbl_fname=Label(win,text="fname:",font='tahoma 15 bold')
lbl_fname.place(x=40,y=20)

ent_fname=Entry(win,width=30)
ent_fname.place(x=155,y=25)

lbl_lname=Label(win,text="lname:",font='tahoma 15 bold')
lbl_lname.place(x=40,y=60)

ent_lname=Entry(win,width=30)
ent_lname.place(x=155,y=65)

lbl_star=Label(win,text="*",font='tahoma 15 bold' ,fg='red')
lbl_star.place(x=15,y=100)

lbl_email=Label(win,text="email:",font='tahoma 15 bold')
lbl_email.place(x=40,y=100)

ent_email=Entry(win,width=30)
ent_email.place(x=155,y=105)


lbl_star=Label(win,text="*",font='tahoma 15 bold' ,fg='red')
lbl_star.place(x=15,y=140)

lbl_password=Label(win,text="password:",font='tahoma 15 bold')
lbl_password.place(x=40,y=140)

ent_password=Entry(win,width=30)
ent_password.place(x=155,y=145)

btn_signup=Button(win,width=20,text='sign up',command=add)
btn_signup.place(x=20,y=200)

btn_signin=Button(win,width=20,text='sign in',command=login)
btn_signin.place(x=200,y=200)




















win.mainloop()