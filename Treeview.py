#ElValenYElLucas🇦 🇷 🇬 🇪 🇳 🇹 🇮 🇳 🇦
import tkinter
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox  # Importa el módulo messagebox

# Esta es la función que agrega una tarea
def agregar():
    today = datetime.today()
    fecha = f"{today.day}/{today.month}/{today.year}"
    treeview.insert("", tk.END, text=texto.get(), values=(fecha, False))
    texto.delete(0, tk.END)

# Esta es la función que elimina una tarea seleccionada
def borrar():
    confirmar = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas borrar?")
    if confirmar:
        selected_item = treeview.selection()
        if selected_item:
            treeview.delete(selected_item)




# Esta función salir cierra la ventana
def salir():
    confirmar = messagebox.askyesno("Confirmación", "¿Estás seguro  de que deseas salir?")
    if confirmar: main_window.quit()

# Estas variables crean la ventana
main_window = tk.Tk()
etiqueta = tk.Label(main_window, text="Agregar tarea: ")
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview(columns=("size", "lastmod"))
treeview.heading("#0", text="Descripcion")
treeview.heading("size", text="Fecha")
treeview.heading("lastmod", text="Completado")
etiqueta.pack() 

texto = tk.Entry(main_window)
texto.pack()

# Esto crea los botones que aparecen en la ventana

btn_guardar = tkinter.Button(main_window, bg="green", text="Agregar", command=agregar)
borrar_btn = tkinter.Button(main_window, bg="blue", text="Borrar", command=borrar)
salir_btn = tkinter.Button(main_window, bg="red", text="Salir", command=salir)
btn_guardar.pack(side=tk.LEFT, fill="y")
borrar_btn.pack(side=tk.LEFT, fill="y")
salir_btn.pack(side=tk.LEFT, fill="y")
treeview.pack()
main_window.mainloop()

