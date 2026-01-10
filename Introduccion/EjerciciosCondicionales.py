import random

def num_1():

    numero= 10 

    if numero >=-5 and numero <=5:
        print("rango chico")
    elif numero >=6 and numero <=20:
        print("Rango mediano")
    else:
        print("fuera de rango")

def num_2():

    numero= 10 

    if numero >=-5 and numero <=5:
        print("rango chico")
    elif numero <=6 and numero <=20:
        print("Rango mediano")
    else:
        print("fuera de rango")

def num_3():
    edad= 65

    if edad >= 18 and edad <=64:
        print ("adulto") 

    elif edad <18:
        print ("menor de edad")

    else:
        print ("adulto mayor")

def num_4():
    temp= 30

    if temp >= 11 and temp <=25:
            print ("templado")
    elif temp <= 10:
            print("frio")
    else: 
            print("calor")


def num_5():

    numero_secreto = random.randint(1, 100)

    intentos = 0
    adivinado = False

    while not adivinado and intentos <5:
        intentos += 1
        usuario = int(input("Adivina el número secreto (1-100): "))

        if usuario == numero_secreto:
            print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
            adivinado = True
        elif intentos==5:
            print("intentos agotados. El número secreto era:", numero_secreto)
        elif usuario < numero_secreto:
            print("El número secreto es mayor.")
        elif usuario > numero_secreto:
            print("El número secreto es menor.")
        else:
            print("Entrada no válida. Por favor, ingresa un número entre 1 y 100.")



def MenuCondicionales():
    
    auxCondicionales= True

    while auxCondicionales:
        print("Seleccione una opcion:")
        print("1.Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")     
        print("4. Ejercicio 4")
        print("5.  Ejercicio 5")
        print("6. Salir")

        opcion= input("Ingrese el numero de la opcion deseada: ")
        opcion= int (opcion)

        if opcion == 1:
            num_1()
        elif opcion == 2:
            num_2()
        elif opcion == 3:
            num_3()
        elif opcion == 4:
            num_4()
        elif opcion == 5:
            num_5()
        elif opcion== 6:
            auxCondicionales= False
            
        else:
            print("Opcion no valida. Intente de nuevo.")

