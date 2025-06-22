from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
win=Tk()
win.geometry("450x500+500+130")
win.config(bg='white')
win.title('Anurag')
bgImage = ImageTk.PhotoImage(file='5153829.jpg')
bgLabel= Label(win, image=bgImage)
bgLabel.place(x=0,y=0)

def close():
    win.destroy()
def submit():
    if(e1.get()=='HORIZON' and e2.get()=='SOLUTION'):
        import database
    else:
        messagebox.showinfo('HORIZON','You enter wrong data')
def reset():
    e1.delete(0,END)
    e2.delete(0,END)
l1=Label(win,text="Login Validation",font=('arial',24,'bold'),bg='white',fg='blue')
l1.place(x=130,y=50)
l2=Label(win,text='Enter UserId',font=('arial',12,'bold'))
l2.place(x=70,y=130)
l3=Label(win,text='Enter Password',font=('arial',12,'bold'))
l3.place(x=70,y=160)
e1=Entry(win)
e1.place(x=210,y=130)
e1.place(x=210,y=130)
e2=Entry(win)
e2.place(x=210,y=160)
b1=Button(win,text='Submit',font=('arial',15,'bold'),fg='blue',command=submit)
b1.place(x=100,y=240)
b2=Button(win,text="Reset",font=('arial',15,'bold'),fg='blue',command=reset)
b2.place(x=210,y=240)
b3=Button(win,text='Close',font=('arial',15,'bold'),fg='blue',command=close)
b3.place(x=300,y=240)
win.mainloop()

