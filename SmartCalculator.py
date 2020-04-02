######################################################################  Commands After Button Click
def btnclick(number):
    global operator
    operator += str(number)
    te.set(operator)

def clear():
    global operator
    operator = ''
    te.set(operator)

def equal():
    global operator
    try:
        result = eval(te.get())
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def sin():
    global operator
    try:
        result = math.sin(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def cos():
    global operator
    try:
        result = math.cos(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def tan():
    global operator
    try:
        result = math.tan(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def log():
    global operator
    try:
        result = math.log(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

def sqrt():
    global operator
    try:
        result = math.sqrt(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Try Again Something Is Wrong...',parent=win)

############################################################################# Hover Effects
def on_enter0(e):
    bt0['bg'] = 'red'
def on_leave0(e):
    bt0['bg'] = 'powder blue'

def on_enter1(e):
    bt1['bg'] = 'red'
def on_leave1(e):
    bt1['bg'] = 'powder blue'

def on_enter2(e):
    bt2['bg'] = 'red'
def on_leave2(e):
    bt2['bg'] = 'powder blue'

def on_enter3(e):
    bt3['bg'] = 'red'
def on_leave3(e):
    bt3['bg'] = 'powder blue'

def on_enter4(e):
    bt4['bg'] = 'red'
def on_leave4(e):
    bt4['bg'] = 'powder blue'

def on_enter5(e):
    bt5['bg'] = 'red'
def on_leave5(e):
    bt5['bg'] = 'powder blue'

def on_enter6(e):
    bt6['bg'] = 'red'
def on_leave6(e):
    bt6['bg'] = 'powder blue'

def on_enter7(e):
    bt7['bg'] = 'red'
def on_leave7(e):
    bt7['bg'] = 'powder blue'

def on_enter8(e):
    bt8['bg'] = 'red'
def on_leave8(e):
    bt8['bg'] = 'powder blue'

def on_enter9(e):
    bt9['bg'] = 'red'
def on_leave9(e):
    bt9['bg'] = 'powder blue'

def on_enterequal(e):
    btequal['bg'] = 'red'
def on_leaveequal(e):
    btequal['bg'] = 'powder blue'

def on_enterclear(e):
    btclear['bg'] = 'red'
def on_leaveclear(e):
    btclear['bg'] = 'powder blue'

def on_entersin(e):
    btsin['bg'] = 'red'
def on_leavesin(e):
    btsin['bg'] = 'powder blue'

def on_entercos(e):
    btcos['bg'] = 'red'
def on_leavecos(e):
    btcos['bg'] = 'powder blue'

def on_entertan(e):
    bttan['bg'] = 'red'
def on_leavetan(e):
    bttan['bg'] = 'powder blue'

def on_entersqrt(e):
    btsqrt['bg'] = 'red'
def on_leavesqrt(e):
    btsqrt['bg'] = 'powder blue'

def on_enterlog(e):
    btlog['bg'] = 'red'
def on_leavelog(e):
    btlog['bg'] = 'powder blue'

def on_enteraddition(e):
    btaddition['bg'] = 'red'
def on_leaveaddition(e):
    btaddition['bg'] = 'powder blue'

def on_entersubstraction(e):
    btsubstraction['bg'] = 'red'
def on_leavesubstraction(e):
    btsubstraction['bg'] = 'powder blue'

def on_entermultiplication(e):
    btmultiplication['bg'] = 'red'
def on_leavemultiplication(e):
    btmultiplication['bg'] = 'powder blue'

def on_enterdivision(e):
    btdivision['bg'] = 'red'
def on_leavedivision(e):
    btdivision['bg'] = 'powder blue'

def on_enterentry(e):
    eny1['bg'] = 'red'
    eny1['fg'] = 'white'
def on_leaveentry(e):
    eny1['bg'] = 'orange'
    eny1['fg'] = 'black'



############################################################################## End Hover Effects

import math
# from tkinter import *
from tkinter import messagebox,Entry,Button,Tk,StringVar
win = Tk()
win.title('Smart Calculator Developed By Rahul Mishra')
win.configure(bg='blue')
# win.resizable(False,False)
win.wm_iconbitmap('cally.ico')
win.maxsize(width=453,height=550)
win.minsize(width=362,height=488)



########################################################################  Entry Box
te = StringVar()
operator = ''
eny1 = Entry(win,bg='orange',font = ('arial',20,'italic bold'),bd=30,
             insertwidth=4,justify='right',textvariable=te)
eny1.grid(columnspan=4)
########################################################################  Buttons

btsin = Button(win,text='sin',font=('arial',15,'italic bold'),padx=14,pady=20,bd=8,
             bg='powder blue',command=cos,activebackground='green',activeforeground='white')
btsin.grid(row=0,column=4)


bt7 = Button(win,text='7',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(7),activebackground='green',activeforeground='white')
bt7.grid(row=1,column=0)

bt8 = Button(win,text='8',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(8),activebackground='green',activeforeground='white')
bt8.grid(row=1,column=1)

bt9 = Button(win,text='9',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(9),activebackground='green',activeforeground='white')
bt9.grid(row=1,column=2)

btaddition = Button(win,text='+',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick('+'),activebackground='green',activeforeground='white')
btaddition.grid(row=1,column=3)

btcos = Button(win,text='cos',font=('arial',15,'italic bold'),padx=14,pady=20,bd=8,
             bg='powder blue',command=cos,activebackground='green',activeforeground='white')
btcos.grid(row=1,column=4)

#############################################
bt4 = Button(win,text='4',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(4),activebackground='green',activeforeground='white')
bt4.grid(row=2,column=0)

bt5 = Button(win,text='5',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(5),activebackground='green',activeforeground='white')
bt5.grid(row=2,column=1)

bt6 = Button(win,text='6',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(6),activebackground='green',activeforeground='white')
bt6.grid(row=2,column=2)

btsubstraction = Button(win,text='- ',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick('-'),activebackground='green',activeforeground='white')
btsubstraction.grid(row=2,column=3)

bttan = Button(win,text='tan',font=('arial',15,'italic bold'),padx=16,pady=20,bd=8,
             bg='powder blue',command=cos,activebackground='green',activeforeground='white')
bttan.grid(row=2,column=4)

##################################################

bt1 = Button(win,text='1',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(1),activebackground='green',activeforeground='white')
bt1.grid(row=3,column=0)

bt2 = Button(win,text='2',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(2),activebackground='green',activeforeground='white')
bt2.grid(row=3,column=1)

bt3 = Button(win,text='3',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(3),activebackground='green',activeforeground='white')
bt3.grid(row=3,column=2)

btmultiplication = Button(win,text='* ',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick('*'),activebackground='green',activeforeground='white')
btmultiplication.grid(row=3,column=3)

btsqrt = Button(win,text='sqrt',font=('arial',15,'italic bold'),padx=12,pady=20,bd=8,
             bg='powder blue',command=sqrt,activebackground='green',activeforeground='white')
btsqrt.grid(row=3,column=4)


#################################################

bt0 = Button(win,text='0',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=lambda :btnclick(0),activebackground='green',activeforeground='white')
bt0.grid(row=4,column=0)

btclear = Button(win,text='C',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
                  bg='powder blue',command=clear,activebackground='yellow',activeforeground='white')
btclear.grid(row=4,column=1)


btequal = Button(win,text='=',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='powder blue',command=equal,activebackground='green',activeforeground='white')
btequal.grid(row=4,column=2)


btdivision = Button(win,text='/ ',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,bg='powder blue'
             ,command=lambda :btnclick('/'),activebackground='green',activeforeground='white')
btdivision.grid(row=4,column=3)

btlog = Button(win,text='log',font=('arial',15,'italic bold'),padx=16,pady=20,bd=8,
             bg='powder blue',command=log,activebackground='green',activeforeground='white')
btlog.grid(row=4,column=4)
###########################################################################  Button Bindings
bt0.bind("<Enter>",on_enter0)
bt0.bind("<Leave>",on_leave0)

bt1.bind("<Enter>",on_enter1)
bt1.bind("<Leave>",on_leave1)

bt2.bind("<Enter>",on_enter2)
bt2.bind("<Leave>",on_leave2)

bt3.bind("<Enter>",on_enter3)
bt3.bind("<Leave>",on_leave3)

bt4.bind("<Enter>",on_enter4)
bt4.bind("<Leave>",on_leave4)

bt5.bind("<Enter>",on_enter5)
bt5.bind("<Leave>",on_leave5)

bt6.bind("<Enter>",on_enter6)
bt6.bind("<Leave>",on_leave6)

bt7.bind("<Enter>",on_enter7)
bt7.bind("<Leave>",on_leave7)

bt8.bind("<Enter>",on_enter8)
bt8.bind("<Leave>",on_leave8)

bt9.bind("<Enter>",on_enter9)
bt9.bind("<Leave>",on_leave9)

btequal.bind("<Enter>",on_enterequal)
btequal.bind("<Leave>",on_leaveequal)

btclear.bind("<Enter>",on_enterclear)
btclear.bind("<Leave>",on_leaveclear)

btsin.bind("<Enter>",on_entersin)
btsin.bind("<Leave>",on_leavesin)

btcos.bind("<Enter>",on_entercos)
btcos.bind("<Leave>",on_leavecos)

bttan.bind("<Enter>",on_entertan)
bttan.bind("<Leave>",on_leavetan)

btsqrt.bind("<Enter>",on_entersqrt)
btsqrt.bind("<Leave>",on_leavesqrt)

btlog.bind("<Enter>",on_enterlog)
btlog.bind("<Leave>",on_leavelog)

btaddition.bind("<Enter>",on_enteraddition)
btaddition.bind("<Leave>",on_leaveaddition)

btsubstraction.bind("<Enter>",on_entersubstraction)
btsubstraction.bind("<Leave>",on_leavesubstraction)

btmultiplication.bind("<Enter>",on_entermultiplication)
btmultiplication.bind("<Leave>",on_leavemultiplication)

btdivision.bind("<Enter>",on_enterdivision)
btdivision.bind("<Leave>",on_leavedivision)

eny1.bind("<Enter>",on_enterentry)
eny1.bind("<Leave>",on_leaveentry)

win.mainloop()