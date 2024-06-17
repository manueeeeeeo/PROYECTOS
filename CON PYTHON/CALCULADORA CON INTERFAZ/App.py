from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

i = 0

# Entrada de texto
e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan=4, padx = 5, pady=5)

# Funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def operacion():
    ecua = e_texto.get()
    resultado = eval(ecua)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0


# Creamos los botones
bot_0 = Button(ventana, text="0", width=13, height=2, command=lambda: click_boton(0))
bot_1 = Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1))
bot_2 = Button(ventana, text="2", width=5, height=2, command=lambda: click_boton(2))
bot_3 = Button(ventana, text="3", width=5, height=2, command=lambda: click_boton(3))
bot_4 = Button(ventana, text="4", width=5, height=2, command=lambda: click_boton(4))
bot_5 = Button(ventana, text="5", width=5, height=2, command=lambda: click_boton(5))
bot_6 = Button(ventana, text="6", width=5, height=2, command=lambda: click_boton(6))
bot_7 = Button(ventana, text="7", width=5, height=2, command=lambda: click_boton(7))
bot_8 = Button(ventana, text="8", width=5, height=2, command=lambda: click_boton(8))
bot_9 = Button(ventana, text="9", width=5, height=2, command=lambda: click_boton(9))

bot_borrar = Button(ventana, text="AC", width=5, height=2, command=lambda: borrar())
bot_par1 = Button(ventana, text="(", width=5, height=2, command=lambda: click_boton("("))
bot_par2 = Button(ventana, text=")", width=5, height=2, command=lambda: click_boton(")"))
bot_punto = Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."))

bot_div = Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"))
bot_multi = Button(ventana, text="x", width=5, height=2, command=lambda: click_boton("*"))
bot_resta = Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"))
bot_suma = Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"))
bot_igual = Button(ventana, text="=", width=5, height=2, command=lambda: operacion())

# Posicionar los botones
bot_borrar.grid(row=1, column=0, padx=5, pady=5)
bot_par1.grid(row=1, column=1, padx=5, pady=5)
bot_par2.grid(row=1, column=2, padx=5, pady=5)
bot_div.grid(row=1, column=3, padx=5, pady=5)

bot_7.grid(row=2, column=0, padx=5, pady=5)
bot_8.grid(row=2, column=1, padx=5, pady=5)
bot_9.grid(row=2, column=2, padx=5, pady=5)
bot_multi.grid(row=2, column=3, padx=5, pady=5)

bot_4.grid(row=3, column=0, padx=5, pady=5)
bot_5.grid(row=3, column=1, padx=5, pady=5)
bot_6.grid(row=3, column=2, padx=5, pady=5)
bot_suma.grid(row=3, column=3, padx=5, pady=5)

bot_1.grid(row=4, column=0, padx=5, pady=5)
bot_2.grid(row=4, column=1, padx=5, pady=5)
bot_3.grid(row=4, column=2, padx=5, pady=5)
bot_resta.grid(row=4, column=3, padx=5, pady=5)

bot_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
bot_punto.grid(row=5, column=2, padx=5, pady=5)
bot_igual.grid(row=5, column=3, padx=5, pady=5)


ventana.mainloop()
