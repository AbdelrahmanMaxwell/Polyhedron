from tkinter import *
from cvxpy import *
import numpy as np
from fractions import Fraction
from tkinter import ttk
from PIL import Image, ImageTk
from webbrowser import *
import time

# This software is developed by Abdelrahman Magdy
version = "Version 0.1"

main_window = Tk()
main_window.title("Polyhedron")
main_window.geometry("1215x700+250+200")
main_window.resizable(width=False, height=False)
#main_window.overrideredirect(True)
#main_window.attributes("-toolwindow", True)
main_window.wm_iconbitmap("bin/bilder/convc.ico")   # To restore the app icon in taskbar

def cls(event):
    main_window.destroy()

def mini_():
    main_window.iconify()

# Drag and drop the app window
lastClickX = 0
lastClickY = 0
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + main_window.winfo_x(), event.y - lastClickY + main_window.winfo_y()
    main_window.geometry("+%s+%s" % (x , y))

#need to pass number of vars + objecFun + constrains
def solv(vars, problem):
    constraints = []
    if vars == 1:
        x = Variable()
    elif vars == 2:
        x = Variable()
        y = Variable()
    else:
        pass

    # Maximize
    if problem[1] == 1: objective = Maximize(problem[0])
    else: objective = Minimize(problem[0])

    # append constraints from problem after max/min paramenter..

    #return optiValue + optiPoints..
    return

constrains_num = ["1","2","3","4","5"]
prob_type = ["Maximize","Minimize"]

def program_start():
    frame_main = Frame(main_window, bg="white")
    frame_title = Frame(main_window, bg="#059eff")

    def curva():
        frame_main.destroy()
        frame_curva = Frame(main_window, bg="white")

        def back_home():
            frame_curva.destroy()
            program_start()

        def curva_check():
            x = Variable()
            f = eval(entry1.get())
            print(f.curvature)
            lab2 = Label(frame_curva, font=("Noto Sans Math", 16), fg="#059eff", bg="white")
            if f.curvature == "CONVEX" or f.curvature == "AFFINE":
                lab2.config(text="Convex")
            elif f.curvature == "CONCAVE":
                lab2.config(text="Not Convex")
            else:
                lab2.config(text="Unknown..")
            lab2.place(x=520,y=87)

        lab1 = Label(frame_curva, text="Objective Function", font=("Noto Sans Math", 16), fg="#7f7f7f", bg="white")
        entry1 = Entry(frame_curva, font=("Noto Sans Math", 16))
        checkbtn = Button(frame_curva, text="Check", font=("Noto Sans Math",16), fg="white", bg="#059eff", relief="flat", command=curva_check)
        back = Button(frame_curva, text="Back", font=("Noto Sans Math",16), fg="white", bg="#059eff", relief="flat", command=back_home)

        frame_curva.place(x=0, y=87,width=1215, height=613)
        lab1.place(x=61,y=87)
        entry1.place(x=290, y=87, width=200, height=30)
        checkbtn.place(x=290, y=146,width=200, height=43)
        back.place(x=290, y=210,width=200, height=43)

    def var1():
        frame_main.destroy()
        frame_var1 = Frame(main_window, bg="white")

        def back_home():
            frame_var1.destroy()
            program_start()

        def create_constraints_fields(event):
            #cont.get()
            print(cont.get())

        def optimal():
            solve.place_forget()
            back = Button(frame_var1, text="Back", font=("Noto Sans Math",16), fg="white", bg="#059eff", relief="flat", command=back_home)
            back.place(x=949, y=506,width=116, height=43)
            print(entry1.get())
            if len(entry1.get()) == 0:
                print("Empty...")

        # Frame GUI
        lab1 = Label(frame_var1, text="Find an optimal solution for this convex function", font=("Noto Sans Math", 16), fg="#7f7f7f", bg="white")
        lab2 = Label(frame_var1, text="Objective Function", font=("Noto Sans Math", 16), fg="#7f7f7f", bg="white")
        lab3 = Label(frame_var1, text="Constraints", font=("Noto Sans Math", 16), fg="#7f7f7f", bg="white")
        entry1 = Entry(frame_var1, font=("Noto Sans Math", 16))
        type = ttk.Combobox(frame_var1, value=prob_type, font=("Noto Sans Math", 16)); type.current(0)
        #type.bind("<<ComboboxSelected>>", create_constraints_fields)
        # Constrants...
        cont = ttk.Combobox(frame_var1, value=constrains_num, font=("Noto Sans Math", 16)); cont.current(0)
        cont.bind("<<ComboboxSelected>>", create_constraints_fields)
        solve = Button(frame_var1, text="Solve", font=("Noto Sans Math",16), fg="white", bg="#059eff", relief="flat", command=optimal)

        frame_var1.place(x=0, y=87,width=1215, height=613)
        lab1.place(x=61,y=87); lab2.place(x=61,y=146); lab3.place(x=61,y=262)
        entry1.place(x=290, y=146, width=200, height=30)
        type.place(x=290, y=200, width=200, height=30)
        cont.place(x=290, y=265, width=60, height=30)
        solve.place(x=325, y=506,width=116, height=43)

    def var2():
        pass


    l1 = Label(frame_main, text="Curvature:", font="24", bg="white", fg="black")
    l2 = Label(frame_main, text="Select Problem Type:", font="24", bg="white", fg="black")
    btn1 = Button(frame_main, text="Convexity Check", font="20", bg="#059eff", fg="white", relief="flat", command=curva)
    btn2 = Button(frame_main, text="1-Variable", font="20", bg="#059eff", fg="white", relief="flat", command=var1)
    btn3 = Button(frame_main, text="2-Variables", font="20", bg="#059eff", fg="white", relief="flat", command=var2)
    #btn4 = Button(frame_main, text="2-Variable", font="20", bg="#059eff", fg="white", relief="flat")

    convex_title = Label(frame_title, image=title, bg="#059eff")
    exit = Button(frame_title, image=ex, bg="#059eff", relief="flat", command=lambda:cls(0))
    mini = Button(frame_title, image=mi, bg="#059eff", relief="flat", command=mini_)
    ver = Label(frame_main, text=version, font="20", bg="white", fg="black")

    frame_main.place(x=0, y=87,width=1215, height=613)
    frame_title.place(x=0, y=0,width=1215, height=87)
    convex_title.place(x=31, y=32,width=198, height=30)
    exit.place(x=1140, y=20,width=47, height=47)
    mini.place(x=1084, y=20,width=47, height=47)
    l1.place(x=56, y=78)
    l2.place(x=56, y=210)
    btn1.place(x=83, y=120,width=227, height=54)
    btn2.place(x=83, y=255,width=227, height=54)
    btn3.place(x=346, y=255,width=227, height=54)
    ver.place(x=35, y=570)

def progress():
    frame_splash.destroy()
    print("Started..")
    program_start()

# Frames
frame_splash= Frame(main_window, bg="#059eff")

splsh_text = "Polyhedron is a Python-based open-source software provides a user-friendly interface for defining and solving convex optimization problems in a simple and efficient manner. "

# Splash screen
alexu_image = PhotoImage(file="bin/bilder/alexu.png")
alexu = Label(frame_splash, image=alexu_image, bg="#059eff")
convex_image = PhotoImage(file="bin/bilder/convex.png")
convex = Label(frame_splash, image=convex_image, bg="#059eff")
#txt = Label(frame_splash, text=splsh_text, font=("Noto Sans Math", 16), fg="white", bg="#059eff")
txt = Text(frame_splash, font=("Noto Sans Math",18), fg="white",bg="#059eff", relief="flat")
txt.insert(INSERT, "Polyhedron is a Python-based open-source software provides a user-friendly interface for defining and solving convex optimization problems in a simple and efficient manner. \n\nPowered by CVXPY, users can easily define optimization problems using a declarative syntax that is similar to mathematical notation then automatically transforms the optimization \nproblem into a canonical form that can be solved using a variety of optimization algorithms")
title = PhotoImage(file="bin/bilder/convextitle.png")
ex = PhotoImage(file="bin/bilder/quit.png")
mi = PhotoImage(file="bin/bilder/minimize.png")

main_window.after(3500, progress)

main_window.bind('<Escape>', cls)
main_window.bind('<Button-1>', SaveLastClickPos)
main_window.bind('<B1-Motion>', Dragging)

# Pack
frame_splash.place(x=0, y=0,width=1215, height=700)
alexu.place(x=1082, y=0,width=78, height=120)
convex.place(x=416, y=38,width=388, height=201)
txt.place(x=100, y=300, width=1035)

main_window.mainloop()
