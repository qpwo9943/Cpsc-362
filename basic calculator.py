# now only first index is the answer need to change
# play again menu
# image?
# in/correct ui
# division deciaml point 
# atleast second trial

from tkinter import *
from random import *
# from time import *
# import threading

win = Tk()
win.geometry("350x450")

Label(win,text = "ASMD",justify = CENTER,font = "Times 21").pack()
Label(win,text = "Learning Center",font = "Times 17").pack()

frame = Frame(win)

# getting x , y
def click():
    num1 = int(random()*10+1)
    num2 = int(random()*10+1)
    return num1,num2

def destroyMenu():
    btn_addition.destroy()
    btn_subtraction.destroy()
    btn_multiplication.destroy()
    btn_dvision.destroy()
    btn_exit.destroy()
# generating buttons for ans
def ansButton(anslist):
    bt1 = Button(frame,text= str(anslist[0]),padx = 35,pady = 35,command = lambda: checkAns(anslist[0]))
    bt2 = Button(frame,text= str(anslist[1]),padx = 35,pady = 35,command = lambda: checkAns(anslist[1]))
    bt3 = Button(frame,text= str(anslist[2]),padx = 35,pady = 35,command = lambda: checkAns(anslist[2]))
    bt4 = Button(frame,text= str(anslist[3]),padx = 35,pady = 35,command = lambda: checkAns(anslist[3]))
   
    bt1.grid(row=1,column=0)
    bt2.grid(row=1,column=1)
    bt3.grid(row=2,column=0)
    bt4.grid(row=2,column=1)
    
    def destroy():
        bt1.destroy()
        bt2.destroy()
        bt3.destroy()
        bt4.destroy()
#check the answer 
    def checkAns(ans):
        destroy()
        if ans == realAns:
            ansLabel = Label(frame,text="CORRECT!",font = "Time 21")
            ansLabel.grid(row=1,column=0)
        else:
            ansLabel = Label(frame,text="Wrong!",font = "Time 21")
            ansLabel.grid(row=1,column=0)
        

# store the followings into list
def storeAns(x,y):
    # print("inside storeAns")
    # print("arithmetic: " + arithmetic)
    anslist = []
    global realAns
    if arithmetic == "+":
        realAns = x+y
        anslist.append(realAns)
        for x in range(1,4):
            ans = int(random()*10)
            anslist.append(ans)
    elif arithmetic == "-":
        realAns = x-y
        anslist.append(realAns)
        for x in range(1,4):
            ans = int(random()*10)
            anslist.append(ans)
    elif arithmetic == "x":
        realAns = x*y
        anslist.append(realAns)
        for x in range(1,4):
            ans = int(random()*10)
            anslist.append(ans)
    elif arithmetic == "/":
        realAns = x/y
        anslist.append(realAns)
        for x in range(1,4):
            ans = int(random()*10)
            anslist.append(ans)
    return anslist

    




def addition():
    global arithmetic
    arithmetic = "+"
    destroyMenu()
    #2개의 번호생성 ex 9+5
    x,y = click()
    questionLabel = Label(frame,text="{0} + {1} = __".format(x,y),font = "Time 19")
    questionLabel.grid(row=0,column=0,columnspan=2)
    z = storeAns(x,y)
    ansButton(z)

def subtraction():
    global arithmetic
    arithmetic = "-"
    destroyMenu()
    #2개의 번호생성 ex 9+5
    x,y = click()
    questionLabel = Label(frame,text="{0} - {1} = __".format(x,y),font = "Time 19")
    questionLabel.grid(row=0,column=0,columnspan=2)
    z = storeAns(x,y)
    ansButton(z)

def multiplication():
    global arithmetic
    arithmetic = "x"
    destroyMenu()
    #2개의 번호생성 ex 9+5
    x,y = click()
    questionLabel = Label(frame,text="{0} x {1} = __".format(x,y),font = "Time 19")
    questionLabel.grid(row=0,column=0,columnspan=2)
    z = storeAns(x,y)
    ansButton(z)

def dvision():
    global arithmetic
    arithmetic = "/"
    destroyMenu()
    #2개의 번호생성 ex 9+5
    x,y = click()
    questionLabel = Label(frame,text="{0} / {1} = __".format(x,y),font = "Time 19")
    questionLabel.grid(row=0,column=0,columnspan=2)
    z = storeAns(x,y)
    ansButton(z)




#buttons
btn_addition = Button(frame,text="+", padx = 35, pady = 35, command = addition)
btn_subtraction = Button(frame,text="-", padx = 35, pady = 35,command = subtraction)
btn_multiplication = Button(frame,text="x", padx = 35, pady = 35,command = multiplication)
btn_dvision = Button(frame,text="/", padx = 35, pady = 35, command = dvision)
btn_exit = Button(frame,text = "Exit", padx = 35, pady = 35, command = win.quit)
btn_exit.grid(row=2,column=0,columnspan=2)

btn_addition.grid(row=0,column=0)
btn_subtraction.grid(row=0,column=1)
btn_multiplication.grid(row=1,column=0)
btn_dvision.grid(row=1,column=1)

frame.pack()


win.mainloop()


