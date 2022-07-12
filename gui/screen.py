from tkinter import *
# import tkinter.scrolledtext as st

root = Tk()


# Basic Information
root.title("C-Analyzer")
root.geometry("1200x900")


input_code_width = 20
input_code_height = 20
input_code = Text(root, height=input_code_height, width=input_code_width)
input_code.configure(relief="sunken", borderwidth=5)
input_code.grid(row=2, column=0, padx=20, pady=20)


lexico_output_height = 20
lexico_output_width = 20
lexico_output = Text(root, height=lexico_output_height, width=lexico_output_width)
lexico_output.configure(relief="sunken", borderwidth=2)
lexico_output.grid(row=4, column=0, padx=20, pady=20)


syntactic_output_height = 20
syntactic_output_width = 20
syntactic_output = Text(root, height=syntactic_output_height, width=syntactic_output_width)
syntactic_output.configure(relief="sunken", borderwidth=2)
syntactic_output.grid(row=4, column=1, padx=20, pady=20)


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
button_lex.grid(row=0, column=1, padx=20, pady=20)

button_syntactic = Button(root, text="Analyze syntactic", padx=40, pady=10, command=lambda: lexico(input_code))
button_syntactic.grid(row=1, column=1, padx=20, pady=20)

button_both = Button(root, text="Analize both", padx=40, pady=10, command=lambda: lexico(input_code))
button_both.grid(row=2, column=1, padx=20, pady=20)

root.mainloop()
