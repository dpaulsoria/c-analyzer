import tkinter as tk
import analyzers.syntax as sx

# import tkinter.scrolledtext as st

root = tk.Tk()

# Basic Information
root.title("C-Analyzer")
root.geometry("1000x650")
eof = '\n'
tab = '\t'

# Label(root, text = "INPUT").place(x = 20, y = 5)
# Label(root, text = "INPUT").place(x = 20, y = 5)
# Label(root, text = "INPUT").place(x = 20, y = 5)
input_code_height = 15
input_code_width = 85
input_output_font = "Consolas", 11
input_scroll = tk.Scrollbar(root)
input_scroll.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=tk.N + tk.S + tk.E)
input_code = tk.Text(root, height=input_code_height, width=input_code_width, font=input_output_font, yscrollcommand=input_scroll.set)
input_code.configure(relief="ridge", borderwidth=5)
input_code.grid(row=0, column=0, rowspan=2, columnspan=2, padx=10, pady=10)
input_scroll.config(command=input_code.yview)

lexicon_output_height = 15
lexicon_output_width = 40
lexicon_output_font = "Consolas", 11
lexicon_scroll = tk.Scrollbar(root)
lexicon_scroll.grid(row=2, column=0, rowspan=2, columnspan=1, sticky=tk.N + tk.S + tk.E)
lexicon_output = tk.Text(root, height=lexicon_output_height, width=lexicon_output_width, font=lexicon_output_font, yscrollcommand=lexicon_scroll.set)
lexicon_output.configure(relief="ridge", borderwidth=5)
lexicon_output.grid(row=2, column=0, rowspan=2, columnspan=1, padx=20, pady=20)
lexicon_scroll.config(command=input_code.yview)

syntax_output_height = 15
syntax_output_width = 40
syntax_output_font = "Consolas", 11
syntax_scroll = tk.Scrollbar(root)
syntax_scroll.grid(row=2, column=1, rowspan=2, columnspan=1, sticky=tk.N + tk.S + tk.E)
syntax_output = tk.Text(root, height=syntax_output_height, width=syntax_output_width, font=syntax_output_font, yscrollcommand=syntax_scroll.set)
syntax_output.configure(relief="ridge", borderwidth=5)
syntax_output.grid(row=2, column=1, rowspan=2, columnspan=1, padx=20, pady=20)
input_scroll.config(command=input_code.yview)
syntax_scroll.config(command=input_code.yview)


# <----- SCROLL TEXT ----->
# text_area = st.ScrolledText(root,
#                             width = 30, 
#                             height = 8, 
#                             font = ("Times New Roman",
#                                     15))
# text_area.place(x=50, y=450)


def lexicon(code):
    code_to_analize = code.get("1.0", 'end-1c')
    print(code_to_analize)


def syntax(code):
    code_to_analize = code.get("1.0", 'end-1c')
    syntax_result = sx.syntax_analyzer(code_to_analize)
    syntax_result = prettier(syntax_result)
    syntax_output.insert(INSERT, syntax_result)


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


button_lex = tk.Button(root, text="Analyze Lexicon", padx=40, pady=10, command=lambda: lexicon(input_code))
button_lex.grid(row=1, column=2, rowspan=1, padx=20, pady=20)

button_syntax = tk.Button(root, text="Analyze Syntax", padx=40, pady=10, command=lambda: syntax(input_code))
button_syntax.grid(row=1, column=2, rowspan=2, padx=20, pady=20)

button_both = tk.Button(root, text="Analize both", padx=40, pady=10, command=lambda: both(input_code))
button_both.grid(row=1, column=2, rowspan=3, padx=20, pady=20)

root.mainloop()
