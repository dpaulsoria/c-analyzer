def verify_code(code):
    texto = code.get("1.0", 'end-1c')

    if texto == "":
        return False
    else:
        save_file(texto)
        return True


def save_file(txt):
    file = open("out/keylogger_output.c", "w")
    line = ""
    for character in txt:
        line += character
    file.write(line)
    file.close()
