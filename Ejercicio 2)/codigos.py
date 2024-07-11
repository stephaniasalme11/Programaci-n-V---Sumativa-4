#Programa que genera códigos Qr personalizados. Por: Stephanía Salmerón. Para: Programación V-UBA
#https://www.python.org/

import qrcode #Importamos la librería qrcode para  utilizar las funcionalidades del QR.
def generar_qr(tamaño, color_qr, color_fondo): #definimos la función generar_qr() donde toma 3 parámetros
    #Dentro de la función creamos un objeto con la versión, el nivel de correción de errores y establece el tamaño y el borde del código.
    qr = qrcode.QRCode(version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_L, 
                   box_size=tamaño, 
                   border=2
                   )
    #Luego, agregamos el link al que queremos enlazar el código QR
    qr.add_data('https://www.python.org/')
    qr.make(fit=True) #Generamos la imagen del código y creamos la imagen final utilizando los colores prorporcionados.
    img = qr.make_image(fill_color=color_qr, back_color=color_fondo)
    return img #Retornamos la imagen 
#Solicitamos al usuario que ingrese el tamaño y colores del código QR
tama_qr = int(input("Ingrese el tamaño del QR en píxeles: "))
color_qr = input("Ingrese el color en inglés del QR:  ")
fondo_qr = input("Ingrese el color en inglés del fondo del QR:  ")
#Llamamos a la función generar_qr() y pasamos los valores ingresados por el ususario a la función y obtenemos la imagen del código QR 
qr_per = generar_qr(tama_qr, color_qr, fondo_qr)
#Guardamos la imagen en un archivo llamado "codigoQR.png"
name_archivo = "codigoQR.png"
qr_per.save(name_archivo)
#Imprimimos un mensaje de confirmación
print("Código QR listo")
