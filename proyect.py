from tkinter import *

window = Tk()
window.title("Miles converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


input = Entry(width=10)
input.grid(column=1, row=0)
print(input.get())

def button_clicked():
    my_label3["text"] = int(input.get()) * 1.60934

my_label = Label(text=" Miles", font=("Arial", 16))
my_label.grid(column=2, row=0)

my_label2 = Label(text="Is equal to", font=("Arial", 16))
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0", font=("Arial", 16))
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km", font=("Arial", 16))
my_label4.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)





# Always at the end
window.mainloop()
