from math import *
from tkinter import *
from tkinter import messagebox
wind = Tk()
label_text = "Очікування"  
x1 = 0 #корінь 1
x2 = 0 #корінь 2
a_ent = IntVar() #значення введене у entry_a
b_ent = IntVar() #значення введене у entry_b
c_ent = IntVar() #значення введене у entry_c

def solver(a_out,b_out,c_out): #Функція яка обчислює дискримінант
    a=int(a_out.get()) #значення введене у entry_a
    b=int(b_out.get()) #значення введене у entry_b
    c=int(c_out.get()) #значення введене у entry_c
    if (a*a-4*b*c<0):
        label_text = "Від'ємний дискримінант"
    elif (a*a-4*b*c==0):
        x1 = (-b/2*a)
        x2 = x1
        label_text = "Один корінь"
    elif (a*a-4*b*c>0):
        x1 = ((-b-sqrt(a*a-4*b*c))/2*a)
        x2 = ((-b+sqrt(a*a-4*b*c))/2*a)
        label_text = "Два корені"
    else:
        label_text = "Помилка"
    return(label_text)

solve_butn = Button(wind, text="Розв'язати",command = solver(a_ent,b_ent,c_ent))

labe_x1 = Label(wind, text = x1)
labe_x2 = Label(wind, text = x2)
labe1 = Label(wind, text = 'a')
labe2 = Label(wind, text = 'b')
labe3 = Label(wind, text = 'c')
labe_feedback = Label(wind, text = label_text) #Лейбл для відображення повідомленнь

entr_a = Entry(wind, textvariable = a_ent)
entr_b = Entry(wind, textvariable = b_ent)
entr_c = Entry(wind, textvariable = c_ent)

solve_butn.grid(row =3, column =1)

labe_x1.grid(row =4, column =0)
labe_x2.grid(row =4, column =1)
labe1.grid(row=0,column=0)
labe2.grid(row=1,column=0)
labe3.grid(row=2,column=0)
labe_feedback.grid(row=3,column=0)

entr_a.grid(row=0,column=1)
entr_b.grid(row=1,column=1)
entr_c.grid(row=2,column=1)




wind.mainloop()