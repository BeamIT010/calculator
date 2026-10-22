from tkinter import *

tk = Tk()
tk.title("เครื่องคิดเลขBeam")

conton = ""
display = StringVar(value="")

def btn(number):
    global conton
    conton = conton + str(number)
    display.set(conton)

ent = Entry(tk, width=20, font=("Arial", 24), justify=RIGHT, textvariable=display)
ent.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="n")
btn7 = Button(tk, text="7", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "7"))
btn7.grid(row=1, column=0, sticky="n", padx=2, pady=2)
btn8 = Button(tk, text="8", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "8"))
btn8.grid(row=1, column=1, sticky="n", padx=2, pady=2)
btn9 = Button(tk, text="9", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "9"))
btn9.grid(row=1, column=2, sticky="n", padx=2, pady=2)
btnclear = Button(tk, text="c", font=("Arial", 24),bg="orange", padx=10,pady=10,command=lambda: display.set(""))
btnclear.grid(row=1, column=3, sticky="n", padx=2, pady=2)
#แถวที่ 2
btn4 = Button(tk, text="4", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "4"))
btn4.grid(row=2, column=0, sticky="n", padx=2, pady=2) 
btn5 = Button(tk, text="5", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "5"))
btn5.grid(row=2, column=1, sticky="n", padx=2, pady=2)
btn6 = Button(tk, text="6", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "6"))
btn6.grid(row=2, column=2, sticky="n", padx=2, pady=2)
btndelete = Button(tk, text="<-", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(display.get()[:-1]))
btndelete.grid(row=2, column=3, sticky="n", padx=2, pady=2)
#แถวที่ 3
btn1 = Button(tk, text="1", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "1"))
btn1.grid(row=3, column=0, sticky="n", padx=2, pady=2)
btn2 = Button(tk, text="2", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "2"))
btn2.grid(row=3, column=1, sticky="n", padx=2, pady=2)
btn3 = Button(tk, text="3", font=("Arial", 24), padx    =10, pady=10,command=lambda: display.set(display.get() + "3"))
btn3.grid(row=3, column=2, sticky="n", padx=2, pady=2)
btnplus = Button(tk, text="+", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(display.get() + "+"))
btnplus.grid(row=3, column=3, sticky="n", padx=2, pady=2)
#แถวที่ 4
btn0 = Button(tk, text="0", font=("Arial", 24), padx=10, pady=10,command=lambda: display.set(display.get() + "0"))
btn0.grid(row=4, column=0, sticky="n", padx=2, pady=2)
btnDot = Button(tk, text=".", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(display.get() + "."))
btnDot.grid(row=4, column=1, sticky="n", padx=2, pady=2)
btnEqual = Button(tk, text="=", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(eval(display.get())))
btnEqual.grid(row=4, column=2, sticky="n", padx=2, pady=2)
btnminus = Button(tk, text="-", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(display.get() + "-"))
btnminus.grid(row=4, column=3, sticky="n", padx=2, pady=2)
#แถวที่ 5
btnmultiply = Button(tk, text="*", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(display.get() + "*"))
btnmultiply.grid(row=5, column=0, sticky="n", padx=2, pady=2)
btndivide = Button(tk, text="/", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(display.get() + "/"))
btndivide.grid(row=5, column=1, sticky="n", padx=2, pady=2)
btnbracket1 = Button(tk, text="(", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(display.get() + "("))
btnbracket1.grid(row=5, column=2, sticky="n", padx=2, pady=2)
btnbracket2 = Button(tk, text=")", font=("Arial", 24),bg="orange", padx=10, pady=10,command=lambda: display.set(display.get() + ")"))
btnbracket2.grid(row=5, column=3, sticky="n", padx=2, pady=2)
tk.mainloop()