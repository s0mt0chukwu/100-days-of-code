from tkinter import *


def button_clicked():
    print("clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("my first GUI program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

#label
my_label = Label(window, text="i'm a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)


#Button

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="new button", command=button_clicked)
new_button.grid(row=0, column=2)

#Entry
input = Entry(width=10)
input.grid(row=2, column=3)







window.mainloop()