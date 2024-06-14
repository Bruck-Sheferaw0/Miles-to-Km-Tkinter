import tkinter

window = tkinter.Tk()
window.title("Miles to Km")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# label
label1 = tkinter.Label(text="is equal to", font=("Arial", 15))
label1.grid(column=1, row=2)
label1.config(padx=20, pady=1)
# text
text1 = tkinter.Entry(width=15)
text1.grid(column=2, row=1)

# label
label2 = tkinter.Label(text="Miles", font=("Arial", 15))
label2.grid(column=3, row=1)
label2.config(padx=20)

# answer label
ansLabel = tkinter.Label(text='0', font=("Arial", 15))
ansLabel.grid(column=2, row=2)
ansLabel.config(pady=20)
kmLabel = tkinter.Label(text="km", font=("Arial", 15))
kmLabel.grid(column=3, row=2)


# action button
def calculate():
    miles = int(text1.get())
    km = miles * 1.60934
    ansLabel.config(text=f"{round(km, 3)}")


button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

window.mainloop()
