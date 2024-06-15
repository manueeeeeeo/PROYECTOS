import qrcode

#Ponemos lo que queremos que se vea al crear el QR
data = 'Esto es una prueba para un QR'
#Pedimos el nombre del archivo que generamos
nombre = input("Digame el nombre del QR: ")
#Procedemos a guardar la imagen
img = qrcode.make(data)
img.save('DIRECCIÓN_DE_DONDE_QUIRES_GUARDARLO/'+nombre)
