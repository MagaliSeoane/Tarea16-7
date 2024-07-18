#CLASE 16 de Julio, analizar el código y explicar que hace cada linea, luego reemplazarlo por otra condición
#WHILE
"""
n = 10
while n<10:
    if (n%2)==0:
        print(n,"Es un numero par")
    else:
        print(n,"es un numero impar")
    n+=1 """

"""El código lo que hace es en principio a la variable n se le asigna el valor 10
   Luego pregunta si n es menor que 10 entonces que ingrese al ciclo while en este caso nunca va a ocurrir 
   ya que como ya se le asigno como valor 10 entonces n nunca va a ser menor que 10.
   Si en caso de que este mal el código y lo que se quiso decir fue que mientras que n sea mayor que 10 que entre al ciclo while 
   lo que pregunta es si n es par que imprima el mensaje que dice que n es par y si no que imprima el mensaje donde n es impar. 
   Pero al incrementarse al final n en 1, lo que ocurre es que el ciclo while nunca termina porque con esa condición n siempre va a ser 
   mayor que 10."""

#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen que está en la carpeta assets del repositorio
inicio = input("¿ENTRAR? Escribir SI o NO: ").upper()
if inicio == "SI":
    print("Bienvenidos al sistema")
elif inicio == "NO":
    saludo = input("¿TE SALUDO? Escribir SI o NO: ").upper()
    if saludo == "SI":
        print("Hola, ¿Cómo estas?")
    elif saludo == "NO":
        salida = input("¿SALIR? Escribir SI o NO: ").upper()
        if salida == "SI":
            print("Saliendo del sistema")
else:
    print("No se reconoce el comando")
    