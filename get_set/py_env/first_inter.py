from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


# y = 0





def inter_face(login):
    def sayHi():
        global zz
        zz += 1
        print(zz)
        
    def exiit():
        win.quit()

    win = tk.Tk()
    win.geometry("255x500")
    win.minsize(255, 500)
    win.maxsize(255, 500)
    frame = Frame(win, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.220)
    img = ImageTk.PhotoImage(Image.open("pro.png"))
    label = Label(frame, image = img)
    label.pack()

    def helloCallBack():
        messagebox.showinfo( "Hello Python", "Hello World")
    b = tk.Button(win, bg='red', text="Click me", command=helloCallBack,background = "green")
    a = tk.Button(win, bg='red', text="exit", command=exiit)
    b.place(x=80,y=420)
    a.place(x=95,y=450)

    # Label(win, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white").place(x=15, y=0)
    Label(win, text="Login : " + login, fg="white").place(x=80, y=250)
    Label(win, text="Num : " + login, fg="white").place(x=80, y=280)
    Label(win, text="Email : " + login, fg="white").place(x=30, y=310)
    Label(win, text="Email : " + login, fg="white").place(x=30, y=310)

    win.mainloop()
# Famous man that directly believed in ???

login = input ("give : ")
inter_face(login)

