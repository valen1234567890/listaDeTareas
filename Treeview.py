import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from tkinter import messagebox

# Esta es la función que agrega una tarea
def agregar():
    today = datetime.today()
    fecha = f"{today.day}/{today.month}/{today.year}"
    tarea = texto.get()

    # Confirmación antes de agregar la tarea
    confirmar = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas agregar la tarea?")
    
    if confirmar:
        treeview.insert("", tk.END, text=tarea, values=(fecha, False))
        texto.delete(0, tk.END)

# Esta es la función que marca una tarea como completada
def completar():
    tareaCompletada = treeview.selection()
    if tareaCompletada:
        treeview.item(tareaCompletada, values=(treeview.item(tareaCompletada)['values'][0], True))

# Esta es la función que elimina una tarea seleccionada
def borrar():
    confirmar = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas borrar?")
    if confirmar:
        BorrarTarea = treeview.selection()
        if BorrarTarea:
            treeview.delete(BorrarTarea)

# Esta función salir cierra la ventana
def salir():
    confirmar = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas salir?")
    if confirmar:
        main_window.quit()

# Estas variables crean la ventana
main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")

treeview = ttk.Treeview(columns=("size", "lastmod"))
treeview.heading("#0", text="Descripción")
treeview.heading("size", text="Fecha")
treeview.heading("lastmod", text="Completado")
treeview.pack()

# Esta variable hace una etiqueta
etiqueta = tk.Label(main_window, text="Agregar tarea: ")
etiqueta.pack()

texto = tk.Entry(main_window)
texto.pack()

# Botones "Agregar", "Completar", "Borrar" y "Salir"
btn_agregar = tk.Button(main_window, bg="lightgreen", text="Agregar", command=agregar, width=20)
completar_btn = tk.Button(main_window, bg="violet", text="Completar", command=completar, width=20)
borrar_btn = tk.Button(main_window, bg="lightblue", text="Borrar", command=borrar, width=20)
salir_btn = tk.Button(main_window, bg="red", text="Salir", command=salir, width=20)

# side=tk.LEFT hace que los botones se coloquen a la izquierda
btn_agregar.pack(side=tk.LEFT)
completar_btn.pack(side=tk.LEFT)
borrar_btn.pack(side=tk.LEFT)
salir_btn.pack(side=tk.LEFT)

main_window.mainloop()
