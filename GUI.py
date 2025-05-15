# Se importa la libreria para hacer interfaces
import tkinter as tk

# Creamos la ventana principal del programa
ventana = tk.Tk()
# Se le da un nombre a la ventana
ventana.title("Calculadora")

# Se le da un tamaño fijo a la ventana
ventana.geometry("400x400")
ventana.resizable(0, 0)
ventana.minsize(400, 400)
ventana.maxsize(400, 400)
# Se le da un color de fondo a la ventana
ventana.config(bg="#8ffffa")
# Tambien pueden usar el nombre del color, aqui hay un enlace a 
# Una página con los nombres de los colores https://www.plus2net.com/python/tkinter-colors.php

# Se crea un frame para la calculadora
#todos los elementos, el primer parametro, tiene que ser el padre
frameInicio = tk.Frame(ventana)
frameJ1uego = tk.Frame(ventana)
frameJ2uego = tk.Frame(ventana)
frameJ3uego = tk.Frame(ventana)


frameInicio.grid(row=0, column=0, padx=10, pady=10)
frameInicio.config(bg="red")
frameInicio.config(width=400, height=400)

#se crea un label(etiqueta de texto) para el titulo de la app
labelTitulo = tk.Label(frameInicio, text="Calculadora", bg="red", font=("Arial", 20))
labelTitulo.grid(row=0, column=0, padx=10, pady=10)




#el main loop es el bucle principal de la aplicacion
ventana.mainloop()