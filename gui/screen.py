from tkinter import *
import syntax as sx

# import tkinter.scrolledtext as st

root = Tk()

# Basic Information
root.title("C-Analyzer")
root.geometry("1100x800")
eof = '\n'
tab = '\t'

input_code_height = 20
input_code_width = 100
input_output_font = "Consolas", 11
input_code = Text(root, height=input_code_height, width=input_code_width, font=input_output_font)
input_code.configure(relief="sunken", borderwidth=5)
input_code.grid(rowspan=3, columnspan=2, padx=20, pady=20)

lexico_output_height = 20
lexico_output_width = 50
lexico_output_font = "Consolas", 11
lexico_output = Text(root, height=lexico_output_height, width=lexico_output_width, font=lexico_output_font)
lexico_output.configure(relief="sunken", borderwidth=5)
lexico_output.grid(row=4, column=0, padx=20, pady=20)

syntactic_output_height = 20
syntactic_output_width = 50
syntactic_output_font = "Consolas", 11
syntactic_output = Text(root, height=syntactic_output_height, width=syntactic_output_width, font=syntactic_output_font)
syntactic_output.configure(relief="sunken", borderwidth=5)
syntactic_output.grid(row=4, column=1, padx=20, pady=20)


# <----- SCROLL TEXT ----->
# text_area = st.ScrolledText(root,
#                             width = 30, 
#                             height = 8, 
#                             font = ("Times New Roman",
#                                     15))
# text_area.place(x=50, y=450)


def lexico(code):
    code_to_analize = code.get("1.0", 'end-1c')
    print(code_to_analize)


def syntax(code):
    code_to_analize = code.get("1.0", 'end-1c')
    syntax_result = sx.syntax_analyzer(code_to_analize)
    syntax_result = prettier(syntax_result)
    syntactic_output.insert(INSERT, syntax_result)


def prettier(code):
    return extract_tree(code, 0)


def extract_tree(code, counter):
    var = ""
    code1 = code
    while len(code1) != 1:
        if not str(code1[0]).isupper():
            code1 = code1[1]
        else:
            var += tab * counter + code1[0] + eof
            counter += 1
            code1 = code1[1]
    return var


'''
    try:
        if len(code[1]) > 0:
            extract_tree(code[1], counter)
    except IndexError:
        return result
'''


def both(code):
    print(code)


button_lex = Button(root, text="Analyze lexicon", padx=40, pady=10, command=lambda: lexico(input_code))
button_lex.grid(row=0, column=2, padx=20, pady=20)

button_syntactic = Button(root, text="Analyze syntactic", padx=40, pady=10, command=lambda: syntax(input_code))
button_syntactic.grid(row=1, column=2, padx=20, pady=20)

button_both = Button(root, text="Analize both", padx=40, pady=10, command=lambda: both(input_code))
button_both.grid(row=2, column=2, padx=20, pady=20)

root.mainloop()
