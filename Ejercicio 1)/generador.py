#Programa que genera contraseñas automáticas. Por: Stephanía Salmerón. Para: Programación V-UBA
import random #Importamos la biblioteca random de Pyhton, la cual genera números y caracteres aleatorios.

caracter = '!"#$%&/()*+-./0123456789?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' #Creamos la variable caracter donde se guardará una cadena de caracteres que incluyen letras mayúsculas, minúsculas, números y símbolos.

contraseña = '' #se creará una variable llamada contraseña donde se guradará la contraseña generada 

lengthContra = int(input('Indique el largo de la contraseña: ')) #Craemos otra variable llamada lengthContra que almacenará el largo de la contraseña. Por otro lado, se utiliza la función input() para solicitar al usuario que ingrese el largo de la misma conviertiendolo así en un número entero mediante la función int().

for _ in range(lengthContra): #El bucle for lo utilizamos para repetir la cantidad de veces indicada por la variable lengthContra 
    contraseña += random.choice(caracter)#Dentro de este bucle utilizamos la función random.choice() para seleccionar un caracter aleatorio de la variable caracter.

print(contraseña) #Finalemnte mostramos por terminal la contraseña generada.
