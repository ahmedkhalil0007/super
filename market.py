import webbrowser
from tkinter import *
from tkinter import messagebox 
from webbrowser import *
from os import *
from sys import *
pro = Tk()
pro.geometry("800x450+280+50")
pro.resizable(False,False)
pro.title("SuperMarket")
pro.iconbitmap("logo.ico")
title = Label(pro, text="Super Maket syatem",fg="gold",bg="black",font=("tajawal",20,"bold"))
title.pack(fill=X)


u1 = "https://www.facebook.com/"
u2 = "https://web.telegram.org/a/"
u3 = "https://www.youtube.com/"

def open1():
    webbrowser.open_new(u1)


def open2():
    webbrowser.open_new(u2)


def open3():
    webbrowser.open_new(u3)

def about1():
    messagebox.showinfo("احمد ماهر","المطور")

def about2():
    messagebox.showinfo("مشروع سوبير ماركيت","عن البرنامج")

def log():
    us = En1.get()
    ps = En2.get()
    if us in ["ahmed" , "maher" , "rody" , "mona"] and ps == "778899445566":
        messagebox.showinfo("راع كل البينات صحيح","..........................ترحب.....................")   
    else:
        messagebox.showerror("خطا في البينات",".............................خطا...........................")

F1 = Frame(pro, width=230,height=420,bg="#0B2F3A")
F1.place(x=570,y=37)

title1 = Label(F1, text="مشروع سوبر ماركيت", bg="#0B2F3A",fg="white",font=("tajawal",13,"bold"))
title1.place(x=42,y=10)
title2 = Label(F1, text="المطور احمد ماهر", bg="#0B2F3A",fg="white",font=("tajawal",13,"bold"))
title2.place(x=52,y=50)
title3 = Label(F1, text="وسال الاتصال بنا", bg="#0B2F3A",fg="white",font=("tajawal",13,"bold"))
title3.place(x=52,y=90)

B1 = Button(F1, text="حسابنا على الفيسبوك",width=26, fg="black",bg="#DBA901",font=("tajawal",11,"bold"),command=open1)
B1.place(x=6,y=130)
B2 = Button(F1, text="حسابنا على تليجرام",width=26, fg="black",bg="#DBA901",font=("tajawal",11,"bold"),command=open2)
B2.place(x=6,y=177)
B3 = Button(F1, text="قناتنا على يوتىوب",width=26, fg="black",bg="#DBA901",font=("tajawal",11,"bold"),command=open3)
B3.place(x=6,y=225)
B4 = Button(F1, text="لمحة عن المطور",width=26, fg="black",bg="#DBA901",font=("tajawal",11,"bold"),command=about1)
B4.place(x=6,y=272)
B5 = Button(F1, text="لمحة عن مشروع",width=26, fg="black",bg="#DBA901",font=("tajawal",11,"bold"),command=about2)
B5.place(x=6,y=318)
B6 = Button(F1, text="اغلاق البرنامج",width=26, fg="black",bg="#DBA901",font=("tajawal",11,"bold"),command=quit)
B6.place(x=6,y=365)

photo = PhotoImage(file=r"C:\Users\AHMED\Desktop\super\shop.png")
imo = Label(pro,image=photo)
imo.place(x=0,y=43, width=570, height=290)

F2 = Frame(pro, width=570 , height=120, bg="#0B2F3A")
F2.place(x=0 , y=330)
photo1 = PhotoImage(file=r"C:\Users\AHMED\Desktop\super\log.png")
imo1 = Label(pro,image=photo1)
imo1.place(x=450,y=335, width=110, height=110)
l1 = Label(F2, text = "اسم المستخدم", fg="gold", bg="#0B2F3A", font=("tajawal",13))
l1.place(x=330,y=25)
l2 = Label(F2, text = "كلمة المرور", fg="gold", bg="#0B2F3A", font=("tajawal",13))
l2.place(x=330,y=70)
En1 = Entry(F2, font=("tajawal",13), justify="center")
En1.place(x=133,y=26)
En2 = Entry(F2, font=("tajawal",13), justify="center")
En2.place(x=133,y=71)
B = Button(F2, text="تسجيل الدخول",bg="#DBA901",font=("tajawal",15), width=12 , height=3,command=log)
B.place(x=10,y=20)
pro.mainloop()