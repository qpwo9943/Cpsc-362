# try:
#     print("Division Calculator")
#     nums = []
#     nums.append(int(input("Enter the first integer: ")))
#     nums.append(int(input("Enter the second integer: ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
# except ValueError:
#     print("Invalid input!")
# except ZeroDivisionError as error:
#     print(error)vv
# except Exception as error: 
#     print(error)

from tkinter import *

win = Tk()
win.title("Simple Calculator!")

# win.geometry("1000x500")
e = Entry(win, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):
    # e.delete(0,END)
    current = e.get()
    e.delete(0,END)

    e.insert(0, current + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    f_num = e.get()
    global first_number
    global arithmetic
    arithmetic = "+"
    first_number = int(f_num)
    e.delete(0,END)


def button_subtraction():
    f_num = e.get()
    global first_number
    global arithmetic
    arithmetic = "-"
    first_number = int(f_num)
    e.delete(0,END)

def button_multiplication():
    f_num = e.get()
    global first_number
    global arithmetic
    arithmetic = "x"
    first_number = int(f_num)
    e.delete(0,END)


def button_equal():
    s_num = e.get()
    e.delete(0,END)
    ans_promt = "{0} {1} {2} = ".format(first_number,arithmetic,s_num)
    # ans = first_number + int(s_num)
    # e.insert(0,ans_promt + str(ans))
    #  + " + " + s_num + " = " + (first_number + int(s_num)))
    # e.insert(0,first_number + int(s_num))

    if arithmetic == "+":
        ans = first_number + int(s_num)
        e.insert(0,ans_promt + str(ans))
    elif arithmetic == "-":
        ans = first_number - int(s_num)
        e.insert(0,ans_promt + str(ans))
    elif arithmetic == "x":
        ans = first_number * int(s_num)
        e.insert(0,ans_promt + str(ans))
    else:
        e.insert(0,"Invalid")
    

button_1 = Button(win, text = "1", padx = 35, pady = 21, command = lambda: button_click(1))
button_2 = Button(win, text = "2", padx = 35, pady = 21, command = lambda: button_click(2))
button_3 = Button(win, text = "3", padx = 35, pady = 21, command = lambda: button_click(3))
button_4 = Button(win, text = "4", padx = 35, pady = 21, command = lambda: button_click(4))
button_5 = Button(win, text = "5", padx = 35, pady = 21, command = lambda: button_click(5))
button_6 = Button(win, text = "6", padx = 35, pady = 21, command = lambda: button_click(6))
button_7 = Button(win, text = "7", padx = 35, pady = 21, command = lambda: button_click(7))
button_8 = Button(win, text = "8", padx = 35, pady = 21, command = lambda: button_click(8))
button_9 = Button(win, text = "9", padx = 35, pady = 21, command = lambda: button_click(9))
button_0 = Button(win, text = "0", padx = 35, pady = 21, command = lambda: button_click(0))


button_add = Button(win, text = "+", padx = 45, pady = 21, command = button_add)
button_subtraction = Button(win, text = "-", padx = 45, pady = 21, command = button_subtraction)
button_multiplication = Button(win, text = "x", padx = 45, pady = 21, command = button_multiplication)
# button_backspace = Button(win, text = "<--", padx = 35, pady = 21, command = button_multiplication)

button_equal = Button(win, text = "=", padx = 77, pady = 21, command = button_equal)
button_clear = Button(win, text = "Clear", padx = 35, pady = 21, command = button_clear)



button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row = 3, column = 3)

button_clear.grid(row = 4, column = 3,columnspan = 2)

# button_backspace.grid(row=3, column=3,columnspan = 2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiplication.grid(row=2, column=3,columnspan = 3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_subtraction.grid(row=1, column=3,columnspan = 3)

button_0.grid(row=4, column=0)
# button_add.grid(row = 5, column = 0)
button_equal.grid(row = 4, column = 1,columnspan = 2)



win.mainloop()
