import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig, ax = plt.subplots() #Damos a entender que vamos a dibujar un grafico
ax.plot(squares, linewidth=3) #Dibujamos los valores

#Establecemos el título del gráfico y las etiquetas de los ejes
ax.set_title("SQUARE NUMBERS", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#Establecemos el tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(labelsize=14)

plt.show() #MMostramos el gráfico
