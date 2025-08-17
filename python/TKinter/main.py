import tkinter

tk=tkinter.Tk()

tk_label=tkinter.Label(text=f'label ')
tk.title('first program with tk')
tk.minsize(500,200)

def event():
    print('clicked')
    tk_label.config(text=input_val.get())

button=tkinter.Button(text='click me!',command=event)
button.pack()

input_val=tkinter.Entry()
input_val.pack()



tk_label.pack()




tk.mainloop()