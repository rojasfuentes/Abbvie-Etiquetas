import tkinter as tk
from tkinter import filedialog

#Botón aceptar
def aceptar():
    global pdf_path
    pdf_path = file_entry.get()
    if pdf_path:
        window.destroy()

#Botón cancelar
def cancelar():
    global pdf_path
    pdf_path = None
    window.destroy()

# UI
window = tk.Tk()
window.title('Seleccionar archivo PDF')


pdf_path = None

file_entry = tk.Entry(window)
file_entry.grid(row=0, column=0, padx=5, pady=5)

def browse_file():
    global pdf_path
    pdf_path = filedialog.askopenfilename(filetypes=(("Archivos PDF", "*.pdf"),))
    file_entry.delete(0, tk.END)
    file_entry.insert(0, pdf_path)

browse_button = tk.Button(window, text='Buscar', command=browse_file)
browse_button.grid(row=0, column=1, padx=5, pady=5)


aceptar_button = tk.Button(window, text='Aceptar', command=aceptar)
aceptar_button.grid(row=1, column=0, padx=5, pady=5)

cancelar_button = tk.Button(window, text='Cancelar', command=cancelar)
cancelar_button.grid(row=1, column=1, padx=5, pady=5)


window.mainloop()

#print("Ruta del archivo PDF seleccionado:", pdf_path)
