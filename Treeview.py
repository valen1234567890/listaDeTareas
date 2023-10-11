#ElValenYElLucas🇦 🇷 🇬 🇪 🇳 🇹 🇮 🇳 🇦
import tkinter
import tkinter as tk
from datetime import datetime
from tkinter import ttk
#Esta es la funciòn que agrega una tarea
def agregar():
        today = datetime.today()
        fecha = f"{today.day}/{today.month}/{today.year}"
        treeview.insert("", tk.END, text= texto.get(), values=(fecha, False))
        texto.delete(0, tk.END)
        
  #esta es la funciòn que elimina una tarea seleccionada   
def borrar():
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item)  

#esta funcion salir cierra la ventana                 
def salir():
    main_window.quit()

#estas variables crean la ventana
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

#esto crea los botones que aparecen en la ventana

btn_guardar = tkinter.Button(main_window, bg= "green", text="Agregar", command = agregar)
borrar_btn = tkinter.Button(main_window, bg=  "blue", text="Borrar", command = borrar)
salir_btn = tkinter.Button(main_window, bg=  "red", text="salir", command = salir)
btn_guardar.pack()
borrar_btn.pack()
salir_btn.pack()   
treeview.pack()
main_window.mainloop()   