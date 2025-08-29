from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text = "I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    print("I got clicked")
    my_label.config(text="The button got clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()


input_field = Entry(width=10)
input_field.pack()
input_field








window.mainloop()