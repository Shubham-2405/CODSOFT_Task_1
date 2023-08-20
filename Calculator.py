# Task 1 : Calculator

# importing libraries
from tkinter import *

result = ''

# addition function
def add():
  global result
  j = 0
  a = result.split('+')
  for i in range(len(a)):
    j = j + float(a[i])
  result = str(j)
  return result

# subtraction function
def sub():
  global result
  j = 0
  a = result.split('-')
  for i in range(len(a)):
    j = j - float(a[i])
  result = str(j)
  return result

# multiply function
def mul():
  global result
  j = 1
  a = result.split('*')
  for i in range(len(a)):
    j= j * float(a[i])
  result = str(j)
  return result

# division function
def div():
  global result
  j = 1
  a = result.split('/')
  j = float(a[0]) / float(a[1])
  result = str(j)
  return result
  
# creating calculator main frame
win = Tk()
win.title("Calculator")
win.geometry("400x465")
win.minsize(200,200)
win.maxsize(600,700)
win.iconbitmap("calculator_icon-icons.com_64876.ico")
input_frame = Frame(win, width=390, height=455, bg='black' )
input_frame.propagate(0)
input_frame.pack()


# buttons function
def click(n):
    global result
    result = result + str(n)
    inputvar.set(result)

# clear function
def clear():
    global result
    result = ''
    inputvar.set(result)

# equals function
def equals():
    global result
    if '+' in result:
       add()
       inputvar.set(result)
    elif '-' in result:
       sub()
       inputvar.set(result)
    elif '*' in result:
       mul()
       inputvar.set(result)
    elif '/' in result:
       div()
       inputvar.set(result)

# Entry
inputvar = StringVar()
ent = Entry(input_frame,justify='right',font=("Arial",40),textvariable=inputvar)
ent.place(x = 10, y = 10,width=370, height = 70)

# first row
b7 = Button(input_frame,text='7', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(7))
b7.place(x=10, y=90, width = 85)

b8 = Button(input_frame,text='8', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(8))
b8.place(x=105, y=90, width = 85)

b9 = Button(input_frame,text='9', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(9))
b9.place(x=200, y=90, width = 85)

bdiv = Button(input_frame,text='÷', font=("arial", 30), relief='groove', bd = 4,command=lambda:click('/'))
bdiv.place(x=296, y=90, width = 83)


# second row
b4 = Button(input_frame,text='4', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(4))
b4.place(x=10, y=180, width = 85)

b5 = Button(input_frame,text='5', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(5))
b5.place(x=105, y=180, width = 85)

b6 = Button(input_frame,text='6', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(6))
b6.place(x=200, y=180, width = 85)

bmul = Button(input_frame,text='x', font=("arial", 30), relief='groove', bd = 4,command=lambda:click('*'))
bmul.place(x=296, y=180, width = 83)

#third row
b1 = Button(input_frame,text='1', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(1))
b1.place(x=10, y=270, width = 85)

b2 = Button(input_frame,text='2', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(2))
b2.place(x=105, y=270, width = 85)

b3 = Button(input_frame,text='3', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(3))
b3.place(x=200, y=270, width = 85)

bsub = Button(input_frame,text='-', font=("arial", 30), relief='groove', bd = 4,command=lambda:click('-'))
bsub.place(x=296, y=270, width = 83)


#fourth row
b0 = Button(input_frame,text='0', font=("arial", 30), relief='groove', bd = 4,command=lambda:click(0))
b0.place(x=10, y=360, width = 85)

bClr = Button(input_frame,text='C', font=("arial", 30), relief='groove', bd = 4,command=lambda:clear())
bClr.place(x=105, y=360, width = 85)

beq = Button(input_frame,text='=', font=("arial", 30), relief='groove', bd = 4,command=lambda:equals())
beq.place(x=200, y=360, width = 85)

bsub = Button(input_frame,text='+', font=("arial", 30), relief='groove', bd = 4,command=lambda:click('+'))
bsub.place(x=296, y=360, width = 83)

win.mainloop()