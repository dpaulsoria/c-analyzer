import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

import analyzers.syntax as sx
import analyzers.lexicon as lx


# -------------------------
# Config UI
# -------------------------
APP_TITLE = "C-Analyzer"
DEFAULT_GEOMETRY = "1100x780"
MONO_FONT = ("Consolas", 11)
UI_FONT = ("Segoe UI", 10)
EOF = "\n"


def main():
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(DEFAULT_GEOMETRY)
    root.minsize(980, 680)

    style = ttk.Style(root)
    # Tema cross-platform (en Windows se ve bien; en Linux/mac también)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    style.configure("TLabel", font=UI_FONT)
    style.configure("TButton", font=UI_FONT, padding=(10, 6))
    style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
    style.configure("Status.TLabel", font=("Segoe UI", 9))

    # Grid principal
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    status_var = tk.StringVar(value="Listo.")

    # -------------------------
    # Toolbar
    # -------------------------
    toolbar = ttk.Frame(root, padding=(10, 8))
    toolbar.grid(row=0, column=0, sticky="ew")
    toolbar.columnconfigure(10, weight=1)

    ttk.Label(toolbar, text="C-Analyzer", style="Header.TLabel").grid(row=0, column=0, padx=(0, 12))

    # Botones principales
    btn_open = ttk.Button(toolbar, text="Abrir .c/.h", command=lambda: open_file(input_text, status_var))
    btn_open.grid(row=0, column=1, padx=4)

    btn_lex = ttk.Button(toolbar, text="Analizar Léxico", command=lambda: analyze_lexicon(input_text, lexicon_text, status_var))
    btn_lex.grid(row=0, column=2, padx=4)

    btn_syn = ttk.Button(toolbar, text="Analizar Sintaxis", command=lambda: analyze_syntax(input_text, syntax_text, status_var))
    btn_syn.grid(row=0, column=3, padx=4)

    btn_both = ttk.Button(toolbar, text="Analizar Ambos", command=lambda: analyze_both(input_text, lexicon_text, syntax_text, status_var))
    btn_both.grid(row=0, column=4, padx=4)

    btn_clear = ttk.Button(toolbar, text="Limpiar", command=lambda: clear_all(input_text, lexicon_text, syntax_text, status_var))
    btn_clear.grid(row=0, column=5, padx=4)

    # Toggle wrap (ajuste de línea)
    wrap_var = tk.BooleanVar(value=False)
    wrap_chk = ttk.Checkbutton(
        toolbar,
        text="Ajustar líneas",
        variable=wrap_var,
        command=lambda: toggle_wrap(wrap_var, input_text, lexicon_text, syntax_text),
    )
    wrap_chk.grid(row=0, column=6, padx=(14, 0))

    # Spacer
    ttk.Label(toolbar, text="").grid(row=0, column=10, sticky="ew")

    # Hint atajos
    ttk.Label(toolbar, text="Atajos: Ctrl+O Abrir | F5 Ambos | F6 Léxico | F7 Sintaxis | Ctrl+L Limpiar").grid(
        row=0, column=11, sticky="e"
    )

    # -------------------------
    # Paned layout (vertical)
    # -------------------------
    main_pane = ttk.Panedwindow(root, orient="vertical")
    main_pane.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 8))

    # --- Input Frame
    input_frame = ttk.Frame(main_pane, padding=(8, 8))
    input_frame.columnconfigure(0, weight=1)
    input_frame.rowconfigure(1, weight=1)

    ttk.Label(input_frame, text="INPUT (Código C)").grid(row=0, column=0, sticky="w", pady=(0, 6))

    input_text = ScrolledText(input_frame, font=MONO_FONT, height=12, undo=True, wrap="none")
    input_text.grid(row=1, column=0, sticky="nsew")

    # --- Output Frame (horizontal split)
    output_frame = ttk.Frame(main_pane, padding=(8, 8))
    output_frame.columnconfigure(0, weight=1)
    output_frame.rowconfigure(1, weight=1)

    ttk.Label(output_frame, text="OUTPUT").grid(row=0, column=0, sticky="w", pady=(0, 6))

    out_pane = ttk.Panedwindow(output_frame, orient="horizontal")
    out_pane.grid(row=1, column=0, sticky="nsew")
    output_frame.rowconfigure(1, weight=1)

    # Lexicon output
    lex_frame = ttk.Frame(out_pane, padding=(6, 6))
    lex_frame.columnconfigure(0, weight=1)
    lex_frame.rowconfigure(1, weight=1)
    ttk.Label(lex_frame, text="LÉXICO").grid(row=0, column=0, sticky="w", pady=(0, 6))
    lexicon_text = ScrolledText(lex_frame, font=MONO_FONT, wrap="none")
    lexicon_text.grid(row=1, column=0, sticky="nsew")
    set_readonly(lexicon_text, True)

    # Syntax output
    syn_frame = ttk.Frame(out_pane, padding=(6, 6))
    syn_frame.columnconfigure(0, weight=1)
    syn_frame.rowconfigure(1, weight=1)
    ttk.Label(syn_frame, text="SINTAXIS").grid(row=0, column=0, sticky="w", pady=(0, 6))
    syntax_text = ScrolledText(syn_frame, font=MONO_FONT, wrap="none")
    syntax_text.grid(row=1, column=0, sticky="nsew")
    syntax_text.tag_configure("error", foreground="#b00020")  # rojo
    syntax_text.tag_configure("ok", foreground="#1b5e20")     # verde oscuro
    set_readonly(syntax_text, True)

    out_pane.add(lex_frame, weight=1)
    out_pane.add(syn_frame, weight=1)

    # Añadir panes al principal
    main_pane.add(input_frame, weight=1)
    main_pane.add(output_frame, weight=2)

    # -------------------------
    # Status bar
    # -------------------------
    status = ttk.Frame(root, padding=(10, 6))
    status.grid(row=2, column=0, sticky="ew")
    status.columnconfigure(0, weight=1)
    ttk.Label(status, textvariable=status_var, style="Status.TLabel").grid(row=0, column=0, sticky="w")

    # -------------------------
    # Hotkeys
    # -------------------------
    root.bind("<Control-o>", lambda _e: open_file(input_text, status_var))
    root.bind("<F5>", lambda _e: analyze_both(input_text, lexicon_text, syntax_text, status_var))
    root.bind("<F6>", lambda _e: analyze_lexicon(input_text, lexicon_text, status_var))
    root.bind("<F7>", lambda _e: analyze_syntax(input_text, syntax_text, status_var))
    root.bind("<Control-l>", lambda _e: clear_all(input_text, lexicon_text, syntax_text, status_var))

    root.mainloop()


# -------------------------
# Helpers UI
# -------------------------
def set_readonly(widget: tk.Text, readonly: bool):
    widget.configure(state=("disabled" if readonly else "normal"))


def toggle_wrap(wrap_var: tk.BooleanVar, *widgets: tk.Text):
    mode = "word" if wrap_var.get() else "none"
    for w in widgets:
        # ScrolledText es Text normal
        was_disabled = str(w.cget("state")) == "disabled"
        if was_disabled:
            w.configure(state="normal")
        w.configure(wrap=mode)
        if was_disabled:
            w.configure(state="disabled")


def open_file(input_text: tk.Text, status_var: tk.StringVar):
    path = filedialog.askopenfilename(
        title="Abrir archivo C",
        filetypes=[("C / Header", "*.c *.h"), ("Todos", "*.*")],
    )
    if not path:
        return
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        input_text.delete("1.0", "end")
        input_text.insert("1.0", content)
        status_var.set(f"Abrí: {path}")
    except Exception as e:
        messagebox.showerror("Error", f"No pude abrir el archivo.\n\n{e}")
        status_var.set("Error al abrir archivo.")


# -------------------------
# Lógica (reusa tus analyzers)
# -------------------------
def analyze_lexicon(input_text: tk.Text, lexicon_output: tk.Text, status_var: tk.StringVar):
    code = input_text.get("1.0", "end-1c")
    set_readonly(lexicon_output, False)
    lexicon_output.delete("1.0", "end")

    try:
        results = lx.lexicon_analyzer(code)
        lexicon_output.insert("1.0", "".join(results))
        status_var.set("Análisis léxico completado.")
    except Exception as e:
        lexicon_output.insert("1.0", f"Error en análisis léxico:\n{e}\n")
        status_var.set("Error en análisis léxico.")
    finally:
        set_readonly(lexicon_output, True)


def skipping_condition(text: str) -> bool:
    end_of_structure = text == "}"
    if_structure = text in ("} else {", "}else{") or ("else if" in text)
    switch_structure = text == "default:" or ("case" in text)
    return end_of_structure or if_structure or switch_structure or (len(text) == 0)


def analyze_syntax(input_text: tk.Text, syntax_output: tk.Text, status_var: tk.StringVar):
    code = input_text.get("1.0", "end-1c")
    lines = code.strip().split(EOF)

    set_readonly(syntax_output, False)
    syntax_output.delete("1.0", "end")

    ok_count = 0
    err_count = 0

    try:
        for i, line in enumerate(lines):
            # Limpia //comentarios, tabs y espacios
            k = re.sub(r"//.*$", "", line).replace("\t", "").strip()

            if skipping_condition(k) or not k:
                continue

            # Skipear cosas no soportadas por tu gramática actual
            if k.startswith(("typedef", "static")):
                continue

            # “Une” bloques para estructuras y declaraciones multi-línea (mejor que lines.index)
            if k.startswith(("for", "switch", "if", "int", "double", "short", "long", "float")):
                attach = k
                j = i + 1
                while j < len(lines):
                    nxt = re.sub(r"//.*$", "", lines[j]).strip()
                    if nxt:
                        attach += " " + nxt
                    j += 1
                k = attach

            # Parse
            result = sx.syntax_analyzer(k)
            if result is not None:
                pretty = prettier(result)
                syntax_output.insert("end", pretty + "\n", ("ok",))
                ok_count += 1
            else:
                syntax_output.insert("end", f"Error de sintaxis en >{k}<\n", ("error",))
                err_count += 1

        status_var.set(f"Análisis sintáctico: OK={ok_count} | Errores={err_count}")
    except Exception as e:
        syntax_output.insert("end", f"\nExcepción en análisis sintáctico:\n{e}\n", ("error",))
        status_var.set("Error en análisis sintáctico.")
    finally:
        set_readonly(syntax_output, True)


def analyze_both(input_text: tk.Text, lexicon_output: tk.Text, syntax_output: tk.Text, status_var: tk.StringVar):
    analyze_lexicon(input_text, lexicon_output, status_var)
    analyze_syntax(input_text, syntax_output, status_var)


def clear_all(input_text: tk.Text, lexicon_output: tk.Text, syntax_output: tk.Text, status_var: tk.StringVar):
    input_text.delete("1.0", "end")
    set_readonly(lexicon_output, False)
    lexicon_output.delete("1.0", "end")
    set_readonly(lexicon_output, True)

    set_readonly(syntax_output, False)
    syntax_output.delete("1.0", "end")
    set_readonly(syntax_output, True)

    status_var.set("Limpio. Listo para analizar.")


def prettier(tree):
    tab = "   "
    eof = "\n"
    var = ""
    code1 = tree
    counter = 0
    while len(code1) != 1:
        if not str(code1[0]).isupper():
            code1 = code1[1]
        else:
            var += tab * counter + ">>" + code1[0] + eof
            counter += 1
            code1 = code1[1]
    return var


if __name__ == "__main__":
    main()
