from tkinter import *
# import tkinter.scrolledtext as st

root = Tk()


# Basic Information
root.title("C-Analyzer")
root.geometry("1200x900")



input_code = Text(root, height=30, width=100)
input_code.configure(relief="sunken", borderwidth=5)
input_code.grid(row=0, column=0 , padx=20, pady=20)

lexico_output = Text(root, height=30, width=50)
lexico_output.configure(relief="sunken", borderwidth=2)
lexico_output.place(x=50, y=450)

syntactic_output = Text(root, height=30, width=50)
syntactic_output.configure(relief="sunken", borderwidth=2)
syntactic_output.place(x=600, y=450)


# <----- SCROLL TEXT ----->
# text_area = st.ScrolledText(root,
#                             width = 30, 
#                             height = 8, 
#                             font = ("Times New Roman",
#                                     15))
# text_area.place(x=50, y=450)


def lexico(code):
    print(code)


button_lex = Button(root, text="Analyze lexicon", padx=40, pady=10, command=lambda: lexico(input_code))
button_lex.place(x=800, y=100)

button_syntactic= Button(root, text="Analyze syntactic", padx=40, pady=10, command=lambda: lexico(input_code))
button_syntactic.place(x=800, y=200)

button_both = Button(root, text="Analize both", padx=40, pady=10, command=lambda: lexico(input_code))
button_both.place(x=800, y=300)

root.mainloop()
