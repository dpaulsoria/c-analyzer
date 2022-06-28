import tkinter
from tkinter import Tk

from lexical import validator as lexer

from syntactic import parser
import functions as fnc

root = Tk()
root.title("C Analyzer")
root.geometry("900x568")


test_file = "tests/keylogger.c"


def analyze(dato, result):
    lexer.input(dato)
    while True:
        tok = lexer.token()
        if not tok:
            break
        line = str(tok) + "\n"
        result.insert(tkinter.INSERT, line)
        print(tok)


def lexical_analyzer(result):
    result.delete("1.0", 'end-1c')
    archivo = open(test_file, "r")
    for line in archivo:
        if len(line) == 0:
            break
        print(">>>" + line)
        analyze(line, result)


def syntactic_analyzer(r1):
    r1.delete("1.0", 'end-1c')
    file = open(test_file, "r")
    for i in file:
        if i != "\n":
            if i[:3] == "for" or i[:5] == "while" or i[:2] == "if":
                newl = i
                for line in file:
                    newl += " " + line
                    if line[:3] == "end":
                        break
                i = newl

            result = parser.parse(i)
            if result is not None:
                result_linea = str(result) + "\n"
                r1.insert(tkinter.INSERT, result_linea)
            else:
                result_linea = "Error de sintaxis \n"
                r1.insert(tkinter.INSERT, result_linea)


def lexico(code):
    if fnc.verify_code(code):
        lexical_analyzer(result_text_area)


def sintactico(code):
    if fnc.verify_code(code):
        syntactic_analyzer(result_text_area)


code1 = tkinter.Text(root, height=10, width=30, )
code1.configure(relief="sunken", borderwidth=5)
code1.place(x=50, y=50, width=300, height=200)

lexic_button = tkinter.Button(root, text="Lexico", padx=40, pady=30,
                              command=lambda: lexico(code1))

lexic_button.place(x=300, y=300, width=100, height=75)

sintactic_button = tkinter.Button(root, text="Sintáctico", padx=40, pady=30,
                                  command=lambda: sintactico(code1))

sintactic_button.place(x=470, y=300, width=100, height=75)

result_text_area = tkinter.Text(root, height=10, width=30)
result_text_area.configure(relief="sunken", borderwidth=5)
result_text_area.place(x=470, y=50, width=350, height=195)

root.mainloop()
