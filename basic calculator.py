#have to download image for the example

from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
from random import *

# from time import *
# import threading

win = Tk()
#win.geometry("350x750")
win.geometry("390x846")
bg = Image.open("Start_Screen_BG.png")
resized = bg.resize((390, 846), Image.ANTIALIAS)
bgImage = ImageTk.PhotoImage(resized)
Label(win, image = bgImage).place(relwidth = 1, relheight = 1)
Label(win, text="ASMD", justify=CENTER, font="Times 21").pack()
Label(win, text="Learning Center", font="Times 17").pack()

frame = Frame(win)



def answer_add():
	answer = num_1 + num_2
	if int(answerex.get()) == answer:
		display = "Correct! " + str(num_1) + " + " + str(num_2) + " = " + str(answer)
	else:
		display = "Wrong! " + str(num_1) + " + " + str(num_2) + " = " + str(answer) + " Not " + answerex.get()

	answer_message.config(text=display)
	answerex.delete(0, 'end')

def answer_sub():
	answer = num_1 - num_2
	if int(answerex.get()) == answer:
		display = "Correct! " + str(num_1) + " - " + str(num_2) + " = " + str(answer)
	else:
		display = "Wrong! " + str(num_1) + " - " + str(num_2) + " = " + str(answer) + " Not " + answerex.get()

	answer_message.config(text=display)
	answerex.delete(0, 'end')

def answer_mul():
	answer = num_1 * num_2
	if int(answerex.get()) == answer:
		display = "Correct! " + str(num_1) + " x " + str(num_2) + " = " + str(answer)
	else:
		display = "Wrong! " + str(num_1) + " x " + str(num_2) + " = " + str(answer) + " Not " + answerex.get()

	answer_message.config(text=display)
	answerex.delete(0, 'end')






# getting x , y
def click():
    num1 = int(random() * 10 + 1)
    num2 = int(random() * 10 + 1)
    return num1, num2


def destroyMenu():
    btn_addition.destroy()
    btn_subtraction.destroy()
    btn_multiplication.destroy()
    btn_dvision.destroy()
    btn_exit.destroy()




# generating buttons for ans
def ansButton(x,y,anslist,questionLabel):
    bt1 = Button(frame, text=str(anslist[0]), padx=35, pady=35, command=lambda: checkAns(anslist[0]))
    bt2 = Button(frame, text=str(anslist[1]), padx=35, pady=35, command=lambda: checkAns(anslist[1]))
    bt3 = Button(frame, text=str(anslist[2]), padx=35, pady=35, command=lambda: checkAns(anslist[2]))
    bt4 = Button(frame, text=str(anslist[3]), padx=35, pady=35, command=lambda: checkAns(anslist[3]))


    bt1.grid(row=1, column=0)
    bt2.grid(row=1, column=1)
    bt3.grid(row=2, column=0)
    bt4.grid(row=2, column=1)




    def destroy():
        bt1.destroy()
        bt2.destroy()
        bt3.destroy()
        bt4.destroy()

    # check the answer
    def checkAns(ans):
        destroy()
        questionLabel.config(text="{0} + {1} = {2}".format(x,y,realAns))
        if ans == realAns:
            ansLabel = Label(frame, text="CORRECT!", font="Time 21")
            ansLabel2 = Label(frame, text=realAns, font="Time 21")
            ansLabel2.grid(row=2, column=0)
            ansLabel.grid(row=1, column=0)
            btn_continue = Button(frame, text="Continue",font="Time 15", padx=35, pady=35, command= lambda: continue_learning())
            btn_exit = Button(frame, text="Exit",font="Time 15", padx=35, pady=35, command=win.quit)
            btn_exit.grid(row=5, column=0 )
            btn_continue.grid(row=4, column=0)

            def continue_learning():
                ansLabel.destroy()
                ansLabel2.destroy()
                btn_continue.destroy()
                questionLabel.destroy()
                if arithmetic == "+":
                    addition()
                elif arithmetic == "-":
                    subtraction()
                elif arithmetic == "x":
                    multiplication()
                elif arithmetic == "/":
                    dvision()



        else:
            questionLabel.config(text="{0} + {1} = {2}".format(x,y,realAns))
            ansLabel = Label(frame, text="Wrong!", font="Time 21")
            ansLabel.grid(row=1, column=0)
            btn_continue = Button(frame, text="Continue", font="Time 15", padx=35, pady=35,
                                  command=lambda: continue_l())
            btn_continue.grid(row=4, column=0)

            def continue_l():
                ansLabel.destroy()
                questionLabel.destroy()
                btn_continue.destroy()
                if arithmetic == "+":
                    addition()
                elif arithmetic == "-":
                    subtraction()
                elif arithmetic == "x":
                    multiplication()
                elif arithmetic == "/":
                    dvision()

# store the followings into list
def storeAns(x, y):
    # print("inside storeAns")
    # print("arithmetic: " + arithmetic)
    anslist = []
    ans_inList = False
    global realAns

    if arithmetic == "+":
        realAns = x + y
        for index in range(4):
            ans = int(random() * 10)
            anslist.append(ans)
            if anslist[index] == realAns:
                ans_inList = True
                print("answer already in the list")
            print(anslist[index])

        print("correct answer ", realAns)
        i = randint(0, 3)
        print(" index = ", i)

        if ans_inList == False:
            anslist[i] = realAns
        print(anslist[i])
    elif arithmetic == "-":
        realAns = x - y
        for index in range(4):
            ans = int(random() * 10)
            anslist.append(ans)
            if anslist[index] == realAns:
                ans_inList = True
                print("answer already in the list")
            print(anslist[index])

        print("correct answer " , realAns )
        i = randint(0, 3)
        print(" index = ",i )

        if ans_inList == False:
            anslist[i] = realAns
        print(anslist[i])
    elif arithmetic == "x":
        realAns = x * y
        for index in range(4):
            ans = int(random() * 10)
            anslist.append(ans)
            if anslist[index] == realAns:
                ans_inList = True
                print("answer already in the list")
            print(anslist[index])

        print("correct answer " , realAns )
        i = randint(0, 3)
        print(" index = ",i )

        if ans_inList == False:
            anslist[i] = realAns
        print(anslist[i])
    elif arithmetic == "/":
        realAns = x / y
        for index in range(4):
            ans = int(random() * 10)
            anslist.append(ans)
            if anslist[index] == realAns:
                ans_inList = True
                print("answer already in the list")
            print(anslist[index])

        print("correct answer " , realAns )
        i = randint(0, 3)
        print(" index = ",i )

        if ans_inList == False:
            anslist[i] = realAns
        print(anslist[i])
    return anslist




def addition():
    hideframes()
    frame.pack()
    global arithmetic
    arithmetic = "+"
    destroyMenu()
    # 2개의 번호생성 ex 9+5
    x, y = click()
    questionLabel = Label(frame, text="{0} + {1} = __".format(x, y), font="Time 19")
    questionLabel.grid(row=0, column=0, columnspan=2)
    z = storeAns(x, y)
    ansButton(x,y,z,questionLabel)


def subtraction():
    hideframes()
    frame.pack()
    global arithmetic
    arithmetic = "-"
    destroyMenu()
    # 2개의 번호생성 ex 9+5
    x, y = click()
    questionLabel = Label(frame, text="{0} - {1} = __".format(x, y), font="Time 19")
    questionLabel.grid(row=0, column=0, columnspan=2)
    z = storeAns(x, y)
    ansButton(x,y,z,questionLabel)


def multiplication():
    hideframes()
    frame.pack()
    global arithmetic
    arithmetic = "x"
    destroyMenu()
    # 2개의 번호생성 ex 9+5
    x, y = click()
    questionLabel = Label(frame, text="{0} x {1} = __".format(x, y), font="Time 19")
    questionLabel.grid(row=0, column=0, columnspan=2)
    z = storeAns(x, y)
    ansButton(x,y,z,questionLabel)


def dvision():
    hideframes()
    frame.pack()

    global arithmetic
    arithmetic = "/"
    destroyMenu()
    # 2개의 번호생성 ex 9+5
    x, y = click()
    questionLabel = Label(frame, text="{0} / {1} = __".format(x, y), font="Time 19")
    questionLabel.grid(row=0, column=0, columnspan=2)
    z = storeAns(x, y)
    ansButton(x,y,z,questionLabel)


def gen_num():
    global num_1
    global num_2
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    print(num_1)
    print(num_2)

    return  num_1,num_2

def main():
    hideframes()
    frame.pack()

    btn_addition = Button(frame, text="+", padx=35, pady=35, command=addition)
    btn_subtraction = Button(frame, text="-", padx=35, pady=35, command=subtraction)
    btn_multiplication = Button(frame, text="x", padx=35, pady=35, command=multiplication)
    btn_dvision = Button(frame, text="/", padx=35, pady=35, command=dvision)
    btn_exit = Button(frame, text="Exit", padx=35, pady=35, command=win.quit)
    btn_exit.grid(row=2, column=0, columnspan=2)

    btn_addition.grid(row=0, column=0)
    btn_subtraction.grid(row=0, column=1)
    btn_multiplication.grid(row=1, column=0)
    btn_dvision.grid(row=1, column=1)


def ansEx(a):
    global answerex
    answerex = Entry(frame2, font=("Times", 18))
    answerex.pack(pady=50)

    if a == "+":
        answerex_button = Button(frame2, text="Answer", command=answer_add)
        answerex_button.pack()

    elif a == "-":
        answerex_button = Button(frame2, text="Answer", command=answer_sub)
        answerex_button.pack()

    elif a == "x":
        answerex_button = Button(frame2, text="Answer", command=answer_mul)
        answerex_button.pack()

    global answer_message
    answer_message = Label(frame2, text="", font=("Times", 18))
    answer_message.pack(pady=40)

    mainBtn = Button(frame2,text="main",command= main)
    mainBtn.pack()


def add():
    destroyMenu()
    hideframes()
    frame2.pack()

    add_label = Label(frame2, text="Addition", font=("Times", 18)).pack()
    Label(frame2,text = "(count the apples)", font=("Times", 13)).pack()

    pic_frame = Frame(frame2, width=400, height=300)
    pic_frame.pack()

    a,b = gen_num()
    global add_image1
    global add_image2


    add1 = Label(pic_frame)
    add2 = Label(pic_frame)
    sign = Label(pic_frame,text ="+",font=("Times", 28))

    add1.grid(row=0,column=0)
    sign.grid(row=0,column=1)
    add2.grid(row=0,column=2)

    #image path
    pic1 = str(a) + ".jpg"
    pic2 = str(b) + ".jpg"
    add_image1 = ImageTk.PhotoImage(Image.open(pic1))
    add_image2 = ImageTk.PhotoImage(Image.open(pic2))

    add1.config(image=add_image1)
    add2.config(image=add_image2)
    arithmetic = "+"
    ansEx(arithmetic)




def sub():
    destroyMenu()
    hideframes()
    frame2.pack()

    add_label = Label(frame2, text="Subtraction", font=("Times", 18)).pack()
    Label(frame2,text = "(count the apples)", font=("Times", 13)).pack()
    pic_frame = Frame(frame2, width=400, height=300)
    pic_frame.pack()

    a,b = gen_num()
    global add_image1
    global add_image2


    sub1 = Label(pic_frame)
    sub2 = Label(pic_frame)
    sign = Label(pic_frame,text ="-",font=("Times", 28))

    sub1.grid(row=0,column=0)
    sign.grid(row=0,column=1)
    sub2.grid(row=0,column=2)

    pic1 = str(a) + ".jpg"
    pic2 = str(b) + ".jpg"
    add_image1 = ImageTk.PhotoImage(Image.open(pic1))
    add_image2 = ImageTk.PhotoImage(Image.open(pic2))

    sub1.config(image=add_image1)
    sub2.config(image=add_image2)

    arithmetic = "-"
    ansEx(arithmetic)

def mul():
    destroyMenu()
    hideframes()
    frame2.pack()

    add_label = Label(frame2, text="multiplication", font=("Times", 18)).pack()
    Label(frame2,text = "(count the apples on the first image times the second image)", font=("Times", 13)).pack()

    pic_frame = Frame(frame2, width=400, height=300)
    pic_frame.pack()

    a, b = gen_num()
    global add_image1
    global add_image2

    mul1 = Label(pic_frame)
    mul2 = Label(pic_frame)
    sign = Label(pic_frame, text="x", font=("Times", 28))

    mul1.grid(row=0, column=0)
    sign.grid(row=0, column=1)
    mul2.grid(row=0, column=2)

    pic1 = str(a) + ".jpg"
    pic2 = str(b) + ".jpg"
    add_image1 = ImageTk.PhotoImage(Image.open(pic1))
    add_image2 = ImageTk.PhotoImage(Image.open(pic2))

    mul1.config(image=add_image1)
    mul2.config(image=add_image2)

    arithmetic = "x"
    ansEx(arithmetic)



def hideframes():
    # Loop thru and destroy all children in previous frames
    for widget in frame.winfo_children():
        widget.destroy()

    for widget in frame2.winfo_children():
        widget.destroy()
    frame.pack_forget()
    frame2.pack_forget()

# buttons

btn_addition = Button(frame, text="+", padx=35, pady=35, command=addition)
btn_subtraction = Button(frame, text="-", padx=35, pady=35, command=subtraction)
btn_multiplication = Button(frame, text="x", padx=35, pady=35, command=multiplication)
btn_dvision = Button(frame, text="/", padx=35, pady=35, command=dvision)
btn_exit = Button(frame, text="Exit", padx=35, pady=35, command=win.quit)
btn_exit.grid(row=2, column=0, columnspan=2)

btn_addition.grid(row=0, column=0)
btn_subtraction.grid(row=0, column=1)
btn_multiplication.grid(row=1, column=0)
btn_dvision.grid(row=1, column=1)




my_menu = Menu(win)
win.config(menu=my_menu)

ASMD_menu = Menu(my_menu)
my_menu.add_cascade(label="ASMD", menu=ASMD_menu)
ASMD_menu.add_command(label="Addition", command=addition)
ASMD_menu.add_command(label="Substraction", command=subtraction)
ASMD_menu.add_command(label="Mulitplication", command=multiplication)
ASMD_menu.add_command(label="Dvision", command=dvision)

example_menu = Menu(my_menu)
my_menu.add_cascade(label="Example", menu=example_menu)
example_menu.add_command(label="Addition", command=add)
example_menu.add_command(label="Substraction", command=sub)
example_menu.add_command(label="Mulitplication", command=mul)


frame2 = Frame(win, width=100, height=100)


frame.pack()

win.mainloop()
