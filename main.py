from tkinter import *


# Button

def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)
my_label.config(pady=50,padx=50)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Entry


input = Entry(width=10)
input.grid(column=3, row=4)
print(input.get())




button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="Click Me2", command=button_clicked)
button.grid(column=2, row=0)

# Always at the end
window.mainloop()
