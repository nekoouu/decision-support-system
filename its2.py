#In the name of GOD
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter 

global D
D = []
D.append(0)

global cost
cost =0

X = [0, 0.36, 0.33, 0.31, 0.3, 0.4, 0.27, 0.29, 0.16, 0.38, 0.40, 0.24, 0.27, 0.08]

root = Tk()
root.title("Parking Cost")
#root.configure(background='light green')
root.geometry('400x400')

def show_cost(cost):
    str_1 = "You should pay " + str(cost) + " Toman."
    tkinter.messagebox.showinfo("Message",str_1)




values_1=["=<0.5","0.5< <2",">=2"]
values_2=["7-14","14-24", "24-7"]
values_3=["Saturday to Wednesday","Thursday and Friday"]
values_4=["Normal Day","Public holiday"]
values_5=["Light","Normal","heavy"]
values_6=["Low","high"]
values_7=["=<12 meter",">12 meter"]
values_8=["Spring and Summer","Autumn and winter"]
values_9=["Inside the traffic plan","Outside the traffic plan"]
values_10=["Commercial","office","residential"]
values_11=["=<1/3",">1/3"]
values_12=["=<1 milliard",">1 milliard"]
values_13=["vulnerable","invulnerable"]


style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "light green", background= "white")


combo_1 = ttk.Combobox(root, values=values_1)
combo_1.set('Duration of parking')
combo_1.pack()

combo_2 = ttk.Combobox(root, values=values_2)
combo_2.set('Hour of using the parking')
combo_2.pack()

combo_3 = ttk.Combobox(root, values=values_3)
combo_3.set('Day of using the parking')
combo_3.pack()

combo_4 = ttk.Combobox(root, values=values_4)
combo_4.set('special time events')
combo_4.pack()

combo_5 = ttk.Combobox(root, values=values_5)
combo_5.set('Traffic conditions of the parking lot')
combo_5.pack()

combo_6 = ttk.Combobox(root, values=values_6)
combo_6.set('Regional value of the parking lot')
combo_6.pack()

combo_7 = ttk.Combobox(root, values=values_7)
combo_7.set('Passage width')
combo_7.pack()

combo_8 = ttk.Combobox(root, values=values_8)
combo_8.set('Season of using the parking')
combo_8.pack()

combo_9 = ttk.Combobox(root, values=values_9)
combo_9.set('Traffic plan')
combo_9.pack()

combo_10 = ttk.Combobox(root, values=values_10)
combo_10.set('Types of uses of surrounding properties')
combo_10.pack()

combo_11 = ttk.Combobox(root, values=values_11)
combo_11.set('Empty parking capacity')
combo_11.pack()

combo_12 = ttk.Combobox(root, values=values_12)
combo_12.set('The amount of parking fees')
combo_12.pack()

combo_13 = ttk.Combobox(root, values=values_13)
combo_13.set('User type')
combo_13.pack()

b = Button(root,text = "Calculate Cost")  
b.pack()

def option_selected_1(event):
    global D
    global cost
    selected_option_1 = combo_1.get()
    if selected_option_1 == values_1[0]: D.append(0)
    if selected_option_1 == values_1[1]: D.append(40)
    if selected_option_1 == values_1[2]: D.append(60)
    cost = cost + X[1]*((2*pow(D[1],2)/36) - 720000/3600 + 700)


def option_selected_2(event):
    global D
    global cost
    selected_option_2 = combo_2.get()
    if selected_option_2 == values_2[0]: D.append(40)
    if selected_option_2 == values_2[1]: D.append(60)
    if selected_option_2 == values_2[2]: D.append(0)
    cost = cost +X[2]*((200*D[2]/60) + 500) 

def option_selected_3(event):
    global D
    global cost
    selected_option_3 = combo_3.get()
    if selected_option_3 == values_3[0]: D.append(70)
    if selected_option_3 == values_3[1]: D.append(30)
    cost = cost + X[3]*((200*(D[3]-30)/40) + 500)

def option_selected_4(event):
    global D
    global cost
    selected_option_4 = combo_4.get()
    if selected_option_4 == values_4[0]: D.append(70)
    if selected_option_4 == values_4[1]: D.append(30) 
    cost = cost + X[4]*((200*(D[4]-30)/40) + 500)

def option_selected_5(event):
    global D
    global cost
    selected_option_5 = combo_5.get()
    if selected_option_5 == values_5[0]: D.append(20)
    if selected_option_5 == values_5[1]: D.append(30)
    if selected_option_5 == values_5[2]: D.append(50)
    cost = cost + X[5]*((200*(D[5]-20)/30) + 500)

def option_selected_6(event):
    global D
    global cost
    selected_option_6 = combo_6.get()
    if selected_option_6 == values_6[0]: D.append(40)
    if selected_option_6 == values_6[1]: D.append(60) 
    cost = cost + X[6]*((200*(D[6]-40)/20) + 500)

def option_selected_7(event):
    global D
    global cost
    selected_option_7 = combo_7.get()
    if selected_option_7 == values_7[0]: D.append(60)
    if selected_option_7 == values_7[1]: D.append(40) 
    cost = cost + X[7]*((200*(D[7]-40)/20) + 500)

def option_selected_8(event):
    global D
    global cost
    selected_option_8 = combo_8.get()
    if selected_option_8 == values_8[0]: D.append(40)
    if selected_option_8 == values_8[1]: D.append(60)
    cost = cost + X[8]*((200*(D[8]-40)/20) + 500)

def option_selected_9(event):
    global D
    global cost
    selected_option_9 = combo_9.get()
    if selected_option_9 == values_9[0]: D.append(70)
    if selected_option_9 == values_9[1]: D.append(30)
    cost = cost + X[9]*((200*(D[9]-30)/40) + 500)

def option_selected_10(event):
    global D
    global cost
    selected_option_10 = combo_10.get()
    if selected_option_10 == values_10[0]: D.append(50)
    if selected_option_10 == values_10[1]: D.append(30)
    if selected_option_10 == values_10[2]: D.append(20)
    cost = cost + X[10]*((200*(D[10]-20)/30) + 500)

def option_selected_11(event):
    global D
    global cost
    selected_option_11 = combo_11.get()
    if selected_option_11 == values_11[0]: D.append(60)
    if selected_option_11 == values_11[1]: D.append(40) 
    cost = cost + X[11]*((200*(D[11]-40)/20) + 500)

def option_selected_12(event):
    global D
    global cost
    selected_option_12 = combo_12.get()
    if selected_option_12 == values_12[0]: D.append(11.5)
    if selected_option_12 == values_12[1]: D.append(10) 
    cost = cost + X[12]*((200*(D[12]-10)/0.5) + 500)

def option_selected_13(event):
    global D
    global cost
    selected_option_13 = combo_13.get()
    if selected_option_13 == values_13[0]: D.append(20)
    if selected_option_13 == values_13[1]: D.append(80) 
    cost = cost + X[13]*((200*(D[13]-20)/60) + 500)
    b['command'] = show_cost(cost)

    




print(cost)


print("P")



combo_1.bind("<<ComboboxSelected>>", option_selected_1)
combo_2.bind("<<ComboboxSelected>>", option_selected_2)
combo_3.bind("<<ComboboxSelected>>", option_selected_2)
combo_4.bind("<<ComboboxSelected>>", option_selected_2)
combo_5.bind("<<ComboboxSelected>>", option_selected_2)
combo_6.bind("<<ComboboxSelected>>", option_selected_2)
combo_7.bind("<<ComboboxSelected>>", option_selected_2)
combo_8.bind("<<ComboboxSelected>>", option_selected_2)
combo_9.bind("<<ComboboxSelected>>", option_selected_2)
combo_10.bind("<<ComboboxSelected>>", option_selected_2)
combo_11.bind("<<ComboboxSelected>>", option_selected_2)
combo_12.bind("<<ComboboxSelected>>", option_selected_2)
combo_13.bind("<<ComboboxSelected>>", option_selected_13)



root.mainloop()



