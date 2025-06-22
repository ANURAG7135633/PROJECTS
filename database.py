from tkinter import *
import pymysql as py
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk

ban = Tk()
ban.geometry("800x600+500+130")
ban.config(bg='sky blue')
ban.title('DATABASE')

def close():
    ban.destroy()

def search():
    roll = e2.get()
    con = py.connect(host='localhost', user='root', password='', database='anurag')
    messagebox.showinfo('Anurag', 'Database connected successfully')
    c = con.cursor()
    c.execute("select * from student where roll="+roll+"")
    data = c.fetchall()
    for x in data:
        e3.insert(0, x[1])
        e4.insert(0, x[2])
        e5.insert(0, x[3])
        e6.insert(0, x[4])

def insert():
    roll = e2.get()
    name = e3.get()
    age = e4.get()
    address = e5.get()
    phonenumber = e6.get()
    con = py.connect(host='localhost', user='root', password='', database='anurag')
    messagebox.showinfo('Anurag', 'Database connected')
    c = con.cursor()
    c.execute("insert into student values("+roll+",'"+name+"',"+age+",'"+address+"',"+phonenumber+")")
    con.commit()
    messagebox.showinfo('Anurag ', "Data inserted successfully")

def reset():
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

def update():
    roll = e2.get()
    name = e3.get()
    age = e4.get()
    address = e5.get()
    phonenumber = e6.get()
    if not all([roll, name, age, address, phonenumber]):
        messagebox.showwarning('Anurag', 'Please fill all fields.')
        return
    try:
        if not age.isdigit():
            messagebox.showwarning('Anurag', 'Age must be a number.')
            return
        if not phonenumber.isdigit():
            messagebox.showwarning('Anurag', 'Phone number must be numeric.')
            return
        con = py.connect(host='localhost', user='root', password='', database='anurag')
        c = con.cursor()
        c.execute(
            "UPDATE student SET name=%s, age=%s, address=%s, phone=%s WHERE roll=%s",
            (name, age, address, phonenumber, roll)
        )
        if c.rowcount > 0:
            con.commit()
            messagebox.showinfo('Anurag', 'Data updated successfully')
            fetch_data()
        else:
            messagebox.showinfo('Anurag', 'No record found for Roll No: ' + roll)
    except py.Error as e:
        messagebox.showerror('Anurag', f'Database error: {e}')
    finally:
        if con:
            con.close()

def delete():
    roll = e2.get()
    name = e3.get()
    age = e4.get()
    address = e5.get()
    phonenumber = e6.get()
    con = py.connect(host='localhost', user='root', password='', database='anurag')
    messagebox.showinfo('Anurag', 'Database connected')
    c = con.cursor()
    c.execute("delete into student values(" + roll + ",'" + name + "'," + age + ",'" + address + "'," + phonenumber +")")
    con.commit()
    messagebox.showinfo('Anurag ', "Data deleted successfully")

def fetch_data():
    con = py.connect(host='localhost', user='root', password='', database='anurag')
    cur = con.cursor()
    cur.execute('select * from student')
    rows = cur.fetchall()
    if len(rows) != 0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('', END, values=row)
        con.commit()
    con.close()

def get_cursor(ev):
    # Placeholder to prevent errors; not used in current GUI
    pass

def search_data():
    con = py.connect(host='localhost', user='root', password='', database='anurag')
    cur = con.cursor()
    cur.execute("select * from student where roll="+e7.get()+"")
    rows = cur.fetchall()
    if len(rows) != 0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('', END, values=row)
        con.commit()
    con.close()

l1 = Label(ban, text="STUDENT MANAGEMENT SYSTEM", font=('arial', 60, 'bold'), bg='white', fg='black')
l1.place(x=100, y=10)
l2 = Label(ban, text=" ENTER ROLL", font=('arial', 15, 'bold'), bg='white', fg='blue')
l2.place(x=130, y=155)
l3 = Label(ban, text=" ENTER NAME", font=('arial', 15, 'bold'), bg='white', fg='blue')
l3.place(x=130, y=225)
l4 = Label(ban, text="ENTER AGE ", font=('arial', 15, 'bold'), bg='white', fg='blue')
l4.place(x=130, y=290)
l5 = Label(ban, text="ENTER ADDRESS", font=('arial', 15, 'bold'), bg='white', fg='blue')
l5.place(x=100, y=357)
l6 = Label(ban, text="ENTER PHONE NUMBER", font=('arial', 15, 'bold'), bg='white', fg='blue')
l6.place(x=40, y=430)
l7 = Label(ban, text="SEARCH BY ROLL", font=('arial', 15, 'bold'), bg='white', fg='blue')
l7.place(x=600, y=155)
e2 = Entry(ban, font=20)
e2.place(x=280, y=155)
e3 = Entry(ban, font=20)
e3.place(x=280, y=225)
e4 = Entry(ban, font=20)
e4.place(x=280, y=290)
e5 = Entry(ban, font=20)
e5.place(x=285, y=360)
e6 = Entry(ban, font=20)
e6.place(x=290, y=430)
e7 = Entry(ban, font=10, width=10)
e7.place(x=800, y=155)

# Table
Table_Frame = Frame(ban, bd=4, relief=RIDGE, bg='crimson')
Table_Frame.place(x=600, y=200, width=900, height=500)

scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

Student_table = ttk.Treeview(
    Table_Frame,
    columns=('roll', 'name', 'age', 'address', 'phone number'),
    xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set
)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=Student_table.xview)
scroll_y.config(command=Student_table.yview)

Student_table.heading("roll", text="Roll No")
Student_table.heading("name", text="Name")
Student_table.heading("age", text="Age")
Student_table.heading("address", text="Address")
Student_table.heading("phone number", text="Phone Number")

Student_table['show'] = 'headings'
Student_table.column("roll", width=100)
Student_table.column("name", width=100)
Student_table.column("age", width=100)
Student_table.column("address", width=100)
Student_table.column("phone number", width=100)

Student_table.pack(fill=BOTH, expand=1)
Student_table.bind("<ButtonRelease-1>", get_cursor)
fetch_data()

# Buttons
b1 = Button(ban, text='INSERT', font=('arial', 15, 'bold'), bg='white', fg='blue', command=insert)
b1.place(x=180, y=510)
b2 = Button(ban, text='SEARCH', font=('arial', 15, 'bold'), bg='white', fg='blue', command=search)
b2.place(x=180, y=600)
b3 = Button(ban, text='RESET', font=('arial', 15, 'bold'), bg='white', fg='blue', command=reset)
b3.place(x=290, y=600)
b4 = Button(ban, text='CLOSE', font=('arial', 15, 'bold'), bg='white', fg='blue', command=close)
b4.place(x=410, y=600)
b5 = Button(ban, text='UPDATE', font=('arial', 15, 'bold'), bg='white', fg='blue', command=update)
b5.place(x=290, y=510)
b6 = Button(ban, text='DELETE', font=('arial', 15, 'bold'), bg='white', fg='blue', command=delete)
b6.place(x=410, y=510)
b7 = Button(ban, text="SEARCH ", font=('arial', 15, 'bold'), bg='white', fg='blue', command=search_data)
b7.place(x=1000, y=155)
b8 = Button(ban, text="SHOW ALL", font=('arial', 15, 'bold'), bg='white', fg='blue', command=fetch_data)
b8.place(x=1170, y=155)

ban.mainloop()