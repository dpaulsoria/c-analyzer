from tkinter import *

root = Tk()

# Basic Information
root.title("C-Analyzer")
root.geometry("900x600")

code1 = Text(root, height=10, width=30)
code1.configure(relief="sunken", borderwidth=5)
code1.grid(row=0, column=0)

code2 = Text(root, height=10, width=30)
code2.configure(relief="sunken", borderwidth=5)
code2.grid(row=0, column=2)


def lexico(code):
    print(code)


button = Button(root, text="Lexic", padx=40, pady=30, command=lambda: lexico(code1))
button.grid(row=0, column=1)

root.mainloop()
