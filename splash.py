from tkinter import *
from PIL import ImageTk
def sign():
    win.destroy()
    import login
win=Tk()
win.geometry("600x600+500+130")
win.config(bg='blue')
win.title("Developed by HORIZON")
bgImage = ImageTk.PhotoImage(file='5153829.jpg')
bgLabel= Label(win, image=bgImage)
bgLabel.place(x=1,y=0)
l1=Label(win,text= "STUDENT MANAGEMENT SYSTEM",bg='blue',font=('roboto',30,'bold'),fg='yellow')
l1.place(x=35,y=70)
l2=Label(win,text= "MY APPLICATION IS RUNNING NOW, Plz,Wait......",bg='Blue',font=('roboto',20,'italic'),fg='yellow')
l2.place(x=35,y=180)
win.after(6000, sign)
win.mainloop()