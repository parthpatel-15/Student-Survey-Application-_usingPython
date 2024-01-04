#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:36:52 2022

@author: Parth Patel
student no: 301207843
"""

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

window =tk.Tk()
window.title("Centennial College")

frame = ttk.Frame(window,width = 500, height = 400 )
frame.grid()
frame['padding'] = (5,10)


lblTitle = ttk.Label(frame, text="ICET student survey",font=("Arial Bold", 25))
lblTitle.grid(column=1, row=0,pady = 20)

lblFname = ttk.Label(frame, text="Full name:            ",font=("Arial ", 15))
lblFname.grid(column=0, row=1,pady = 5, sticky = 'W')

fullName = tk.StringVar()
txtFname = ttk.Entry(frame, textvariable=fullName ,width=25)
txtFname.insert(0,"Narendra Modi")
txtFname.grid(column = 1, row = 1,pady = 5, sticky = 'W')

lblRes = ttk.Label(frame, text="Residency:            ",font=("Arial ", 15))
lblRes.grid(column=0, row=2 ,pady = 5 , sticky = 'W')

residency = tk.StringVar()
residency.set('Domestic')
RbuttonRes1 = ttk.Radiobutton(frame, text='Domestic', variable = residency,  state= tk.NORMAL  ,value='Domestic' , )
RbuttonRes1.grid(column = 1, row = 2,pady = 5, sticky = 'W')
RbuttonRes2 = ttk.Radiobutton(frame, text='International', variable = residency, value='International' )
RbuttonRes2.grid(column = 1, row = 3,pady = 5, sticky = 'W')


lblProg = ttk.Label(frame, text="Program:            ",font=("Arial ", 15))
lblProg.grid(column=0, row=4,pady = 5, sticky = 'W')

prog = tk.StringVar()
comboProg = ttk.Combobox(frame,textvariable  = prog)
comboProg['values']= ('AI', 'Gaming', 'Health', 'Software')
comboProg.current(2)
comboProg.grid(column=1, row=4,pady = 5, sticky = 'W')

lblCourses = ttk.Label(frame, text="Courses:            ",font=("Arial ", 15))
lblCourses.grid(column=0, row=5,pady = 5, sticky = 'W')

cv100 = tk.StringVar()
cv213 = tk.StringVar()
cv120 = tk.StringVar()
cv100.set("COMP100")

CButton1 = ttk.Checkbutton(frame, text = "Programming 1",variable= cv100,onvalue = 'COMP100',offvalue = '',)
CButton1.grid(column=1, row=5,pady = 5, sticky = 'W')

CButton2 = ttk.Checkbutton(frame, text = "Web Page Design",variable= cv213,onvalue = 'COMP213',offvalue = '',)
CButton2.grid(column=1, row=6,pady = 5, sticky = 'W')

CButton3 = ttk.Checkbutton(frame, text = "Software Engineering", variable= cv120,onvalue = 'COMP120',offvalue = '',)
CButton3.grid(column=1, row=7,pady = 5, sticky = 'W')

def reset():
    txtFname.delete(0,tk.END)
    txtFname.insert(0,"Narendra Modi")
    residency.set('Domestic')
    comboProg.current(2)
    cv120.set('')
    cv213.set('')
    cv100.set("COMP100")
    return


resetBtn = ttk.Button(frame, text="Reset", command = reset)
resetBtn.grid(column=0, row=8)

def info(*args):
    tkinter.messagebox.showinfo(
        title = "information",
        message=  f'Fullname:  {fullName.get()}'
                f'\nResidency: {residency.get()}'
                f'\nProgram:   {prog.get()}'
                f'\nCourses:   {cv100.get()} {cv120.get()} {cv213.get()} ')

okBtn = ttk.Button(frame, text="OK" , command = info )
okBtn.grid(column=1, row=8  )

exitBtn = ttk.Button(frame, text="Exit" , command =  window.destroy)
exitBtn.grid(column=3, row=8)


window.mainloop()
