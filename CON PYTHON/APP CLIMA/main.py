import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from weather_api import fetch_weather

# Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación de Clima")
root.geometry("400x500")
root.configure(background='#f0f0f0')

# Crear un estilo ttk para configurar el color de fondo
style = ttk.Style()
style.configure('Top.TFrame', background='#f0f0f0')

# Función para obtener y mostrar el clima
def get_weather():
    city = city_entry.get()
    if city:
        data = fetch_weather(city)
        if data:
            display_weather(data)
        else:
            messagebox.showerror("Error", "No se pudo obtener la información del clima.")
    else:
        messagebox.showerror("Error", "Por favor, ingresa una ciudad.")

# Función para mostrar la información del clima
def display_weather(data):
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    weather = data['weather'][0]['description']

    # Actualizar el área de texto con la información del clima
    weather_info.delete('1.0', tk.END)
    weather_info.insert(tk.END, f"Ciudad: {city}, {country}\n")
    weather_info.insert(tk.END, f"Temperatura: {temp}°C\n")
    weather_info.insert(tk.END, f"Condición: {weather.capitalize()}\n")

    # Mostrar el ícono del clima correspondiente
    icon_name = get_icon(weather.lower())
    icon_path = f"iconos/{icon_name}"
    icon_image = Image.open(icon_path)
    icon_image = icon_image.resize((100, 100), Image.LANCZOS)
    icon_photo = ImageTk.PhotoImage(icon_image)
    weather_icon_label.config(image=icon_photo)
    weather_icon_label.image = icon_photo

# Función para obtener el ícono del clima
def get_icon(weather_description):
    # Diccionario de íconos
    weather_icons = {
        'cielo claro': 'sunny.png',
        'algo de nubes': 'partly_cloud.png',
        'nubes dispersas': 'partly_cloud.png',
        'nubes rotas': 'cloudy.png',
        'nubes': 'cloudy.png',
        'lluvia ligera': 'rainy.png',
        'lluvia moderada': 'rainy.png',
        'lluvia intensa': 'rainy.png',
        'tormenta': 'stormy.png',
        'nevada ligera': 'snowy.png',
        'nieve': 'snowy.png',
        'nieve intensa': 'snowy.png',
        'neblina': 'cloudy.png',
        'lluvia': 'rainy.png'
    }
    # Obtener el ícono basado en la descripción del clima
    return weather_icons.get(weather_description, 'cloudy.png')

# Frame superior para la entrada de ciudad y botón
frame_top = ttk.Frame(root, style='Top.TFrame', padding=(20, 10))
frame_top.pack(fill=tk.BOTH)

# Etiqueta y entrada para la ciudad
ttk.Label(frame_top, text="Ciudad:", font=("Helvetica", 14)).pack(side=tk.LEFT)
city_entry = ttk.Entry(frame_top, width=30, font=("Helvetica", 14))
city_entry.pack(side=tk.LEFT, padx=10)

# Botón para obtener el clima (ahora se coloca directamente en root)
ttk.Button(root, text="Obtener Clima", command=get_weather).pack(pady=10)

# Frame para mostrar la información del clima
frame_weather = ttk.Frame(root, padding=(20, 10), style='Top.TFrame')
frame_weather.pack(fill=tk.BOTH, expand=True)

# Área de texto para mostrar la información del clima
weather_info = tk.Text(frame_weather, height=8, font=("Helvetica", 12), wrap=tk.WORD)
weather_info.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Etiqueta para mostrar el ícono del clima
weather_icon_label = tk.Label(frame_weather)
weather_icon_label.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
