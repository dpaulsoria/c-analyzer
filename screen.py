import re
import tkinter as tk
import analyzers.syntax as sx
import analyzers.lexicon as lx

# import tkinter.scrolledtext as st

root = tk.Tk()

# Basic Information
root.title("C-Analyzer")
root.geometry("950x700")
eof = '\n'
tab = '   '

tk.Label(root, text="INPUT").grid(row=0, columnspan=3)
input_code_height = 15
input_code_width = 85
input_output_font = "Consolas", 11
input_scroll = tk.Scrollbar(root)
input_scroll.grid(row=1, column=0, rowspan=6, columnspan=3, sticky=tk.N + tk.S + tk.E)
input_code = tk.Text(root, height=input_code_height, width=input_code_width, font=input_output_font,
                     yscrollcommand=input_scroll.set)
input_code.configure(relief="ridge", borderwidth=5)
input_code.grid(row=1, column=0, rowspan=6, columnspan=3, padx=20, pady=10)
input_scroll.config(command=input_code.yview)

tk.Label(root, text="LEXICON ANALYZER").grid(row=7, column=0, columnspan=2)
lexicon_output_height = 15
lexicon_output_width = 50
lexicon_output_font = "Consolas", 11
lexicon_scroll = tk.Scrollbar(root)
lexicon_scroll.grid(row=8, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E)
lexicon_output = tk.Text(root, height=lexicon_output_height, width=lexicon_output_width, font=lexicon_output_font,
                         yscrollcommand=lexicon_scroll.set)
lexicon_output.configure(relief="ridge", borderwidth=5)
lexicon_output.grid(row=8, column=0, columnspan=2, padx=0, pady=10)
lexicon_scroll.config(command=lexicon_output.yview)

tk.Label(root, text="SYNTAX ANALYZER").grid(row=7, column=2, columnspan=2)
syntax_output_height = 15
syntax_output_width = 50
syntax_output_font = "Consolas", 11
syntax_scroll = tk.Scrollbar(root)
syntax_scroll.grid(row=8, column=2, columnspan=2, sticky=tk.N + tk.S + tk.E)
syntax_output = tk.Text(root, height=syntax_output_height, width=syntax_output_width, font=syntax_output_font,
                        yscrollcommand=syntax_scroll.set)
syntax_output.configure(relief="ridge", borderwidth=5)
syntax_output.grid(row=8, column=2, columnspan=2, padx=0, pady=10)
syntax_scroll.config(command=syntax_output.yview)


def lexicon(code):
    lexicon_output.delete('1.0', tk.END)
    code_to_analize = code.get("1.0", 'end-1c')
    lexicon_result = lx.lexicon_analyzer(code_to_analize)
    for result in lexicon_result:
        lexicon_output.insert(tk.INSERT, result)
    # print(code_to_analize)


def skipping_condition(text):
    end_of_structure = text == "}"
    if_structure = text == "} else {" or text == "}else{" or text.__contains__("else if")
    switch_structure = text == "default:" or text.__contains__("case")
    return end_of_structure or if_structure or switch_structure


def syntax(code):
    syntax_output.delete('1.0', tk.END)
    code_to_analize = code.get("1.0", 'end-1c')
    lines = code_to_analize.strip().split(eof)
    print(lines)

    for line in lines:
        k = line.replace("\t", "")
        if skipping_condition(k):
            continue
        if line != "\n":
            if line.startswith("for") or line.startswith("switch") or line.startswith("if"):
                index = lines.index(line) + 1
                print("Start analyzing a CONTROL STRUCTURE")
                attach = line
                while True:
                    attach += " " + lines[index]
                    index += 1
                    if index == len(lines):
                        line = attach
                        break
            print_syntax_result(line)


def print_syntax_result(code):
    syntax_result = sx.syntax_analyzer(code)
    if syntax_result is not None:
        syntax_result = prettier(syntax_result)
        syntax_result = str(syntax_result) + "\n"
        syntax_output.insert(tk.INSERT, syntax_result)
    else:
        syntax_result = "Error de sintaxis \n"
        syntax_output.insert(tk.INSERT, syntax_result)


def prettier(code):
    var = ""
    code1 = code
    counter = 0
    while len(code1) != 1:
        if not str(code1[0]).isupper():
            code1 = code1[1]
        else:
            var += tab * counter + ">>" + code1[0] + eof
            counter += 1
            code1 = code1[1]
    return var


def both(code):
    lexicon(code)
    syntax(code)


def clear():
    input_code.delete('1.0', tk.END)
    lexicon_output.delete('1.0', tk.END)
    syntax_output.delete('1.0', tk.END)


button_lex = tk.Button(root, text="Analyze Lexicon", padx=40, pady=10, command=lambda: lexicon(input_code))
button_lex.grid(row=1, column=3, padx=20, pady=20)

button_syntax = tk.Button(root, text="Analyze Syntax", padx=40, pady=10, command=lambda: syntax(input_code))
button_syntax.grid(row=2, column=3, padx=20, pady=20)

button_both = tk.Button(root, text="Analize both", padx=40, pady=10, command=lambda: both(input_code))
button_both.grid(row=3, column=3, padx=20, pady=20)

button_clear = tk.Button(root, text="Clear", padx=40, pady=10, command=lambda: clear())
button_clear.grid(row=4, column=3, padx=20, pady=20)

root.mainloop()
