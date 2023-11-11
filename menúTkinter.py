import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import*
import manipulaArticulos

#módulos del sistema

#funciones para las opciones del menú
def abrir():
    messagebox.showinfo("Abrir", "Abrir archivo")

def guardar():
    messagebox.showinfo("Guardar", "Guardar archivo")

def salir():
    ventana.quit()

def articulos():
    manipulaArticulos.muestra()

#crea la ventana principal

ventana = tk.Tk()
ventana.resizable(1,1)
ventana.geometry("1200x900")
ventana.config(bg="#e5f2f4")
ventana.title("HardWolf.Store")

#define imagen del logo de la ferretería
logo = tk.PhotoImage(file="lobo.png") 
etiqueta_logo = tk.Label(ventana, image=logo)
etiqueta_logo.place(x=350, y=100)  # coordenadas de la imagen


#definir la fuente para el menú
fuente_menu = tkFont.Font(family="Arisl",size=14)
#crea un objeto menú
menu = tk.Menu(ventana, font=fuente_menu)
ventana.config(menu=menu)

#crea un menú Archivo y añadir opciones
menu_catalogos = tk.Menu(menu)
menu.add_cascade(label="Catálogos", menu=menu_catalogos)
menu_catalogos.add_command(label="Artículos", command=articulos)
menu_catalogos.add_command(label="Proveedores", command=guardar)
menu_catalogos.add_command(label="Clientes", command=guardar)

menu_movimientos = tk.Menu(menu)
menu.add_cascade(label="Movimientos", menu=menu_movimientos)
menu_movimientos.add_cascade(label="Entrada a Almacén",command=abrir)
menu_movimientos.add_cascade(label="Traspaso a piso de venta",command=guardar)
menu_movimientos.add_cascade(label="Venta",command=guardar)

ventana.mainloop()