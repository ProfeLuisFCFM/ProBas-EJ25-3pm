import tkinter as tk
from tkinter import filedialog, scrolledtext, Menu
import subprocess

def new_file():
    text_area.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))

def close_app():
    root.quit()

def execute_code():
    code = text_area.get("1.0", tk.END)
    process = subprocess.Popen("python", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(code)
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, stdout + stderr)
    output_area.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Python Notepad")
root.geometry("800x600")

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nuevo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Cerrar", command=close_app)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

run_menu = Menu(menu_bar, tearoff=0)
run_menu.add_command(label="Ejecutar", command=execute_code)
menu_bar.add_cascade(label="Ejecutar", menu=run_menu)

root.config(menu=menu_bar)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 12))
text_area.pack(expand=True, fill=tk.BOTH)

output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 12), height=10, state=tk.DISABLED, bg="black", fg="white")
output_area.pack(fill=tk.X)

root.mainloop()
