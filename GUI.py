from tkinter import *
from tkinter import  ttk
import Functions
#Create the form
form = Tk(className='user input')
form.geometry("500x600")
#create labels
feature_string1 = StringVar()
feature_string1.set("Select feature 1:")
features_label1 = Label(form, textvariable = feature_string1)
features_label1.place(x = 30, y = 30)

feature_string2 = StringVar()
feature_string2.set("Select feature 2:")
features_label2 = Label(form, textvariable = feature_string2)
features_label2.place(x = 30, y = 80)

class_string1 = StringVar()
class_string1.set("Select class 1:")
class_label1 = Label(form, textvariable = class_string1)
class_label1.place(x = 30, y = 130)

class_string2 = StringVar()
class_string2.set("Select class 2:")
class_label2 = Label(form, textvariable = class_string2)
class_label2.place(x = 30, y = 180)

eta_string = StringVar()
eta_string.set("Enter learning rate(eta):")
eta_label = Label(form, textvariable = eta_string)
eta_label.place(x = 30, y = 230)

m_string = StringVar()
m_string.set("Enter number of epochs(m):")
m_label = Label(form, textvariable = m_string)
m_label.place(x = 30, y = 280)

mse_string = StringVar()
mse_string.set("Enter MSE Threshold:")
mse_label = Label(form, textvariable = mse_string)
mse_label.place(x = 30, y = 330)

#create combo boxes
f1_combo = ttk.Combobox(form, values = ["X1", "X2", "X3", "X4"])
f1_combo.current(0)
f1_combo.place(x = 250, y = 30)

f2_combo = ttk.Combobox(form, values = ["X1", "X2", "X3", "X4"])
f2_combo.current(0)
f2_combo.place(x = 250, y = 80)

c1_combo = ttk.Combobox(form, values = ["C1", "C2", "C3"])
c1_combo.current(0)
c1_combo.place(x = 250, y = 130)

c2_combo = ttk.Combobox(form, values = ["C1", "C2", "C3"])
c2_combo.current(0)
c2_combo.place(x = 250, y = 180)
#create textboxes
eta_str = StringVar(form, value='0.0')
eta_entry = ttk.Entry(form, textvariable = eta_str)
eta_entry.place(x = 250, y = 230)

m_str = StringVar(form, value= '1')
m_entry = ttk.Entry(form, textvariable = m_str)
m_entry.place(x = 250, y = 280)

mse_str = StringVar(form, value= '0.01')
mse_entry = ttk.Entry(form, textvariable = mse_str)
mse_entry.place(x = 250, y = 330)

#create checkbox
b_string = StringVar()
b_string.set("Add bias")
check_var = IntVar()
b_check = ttk.Checkbutton(form, textvariable = b_string, variable = check_var)
b_check.place(x = 30, y = 380)
#global_data_variables
f1 = 'X1'
f2 = 'X2'
c1 = 'C1'
c2 = 'C2'
eta = 0.0
m = 1
b = 0
mse = 0.01
#save after complete input
def save():
    global f1
    global f2
    global c1
    global c2
    global eta
    global m
    global b
    global mse
    f1 = f1_combo.get()
    f2 = f2_combo.get()
    c1 = c1_combo.get()
    c2 = c2_combo.get()
    eta = float(eta_entry.get())
    m = int(m_entry.get())
    b = int(check_var.get())
    mse = float(mse_entry.get())
    print(f1, f2, c1, c2, eta, m, b, mse)
#save button
save_b = Button(form, text = 'Save', command = save)
save_b.place(x = 30, y = 430)
#train button
train_b = Button(form, text = 'Train', command = lambda : Functions.train(c1, c2, f1, f2, m, eta, b, mse))
train_b.place(x = 230, y = 430)
#testing button
test_b = Button(form, text = 'Test', command = lambda : Functions.test(c1, c2, f1, f2, b))
test_b.place(x = 30, y = 480)
#display button
display_b = Button(form, text = 'Dispaly plot', command = lambda : Functions.display_plot(c1, c2, f1, f2))
display_b.place(x = 230, y = 480)
form.mainloop()

