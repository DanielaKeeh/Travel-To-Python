
def ejercicioRadioCirculo():

    pi= 3.1416
    pi= float(pi)

    radio=input("ingresa el radio de tu circulo: ")
    radio=float(radio)

    area= pi* radio ** 2

    print(f"el area de tu circulo es de {area} cms cuadrados.")

def ejercicioParImpar():

    num= input("ingresa un numero: ")
    num=int(num)

    if num % 2  == 0 :
        print(f"el numero {num} es par")
    else:
        print(f"el numero {num} es impar")

def condicionalSimple():

    edad= input("ingresa tu edad: ")
    edad= int (edad)

    if edad >= 18:
        print("eres mayor de edad.")
    else:
        print("eres menor de edad.")

    #------------------------------- 2

    num = input("ingresa un numero: ")
    num= int (num)

    if num >0:

        print ("positivo")

    elif num<0:
        print ("negativo")

    else:
        print("cero")


def ejercicioAreaTriangulo():  
    base = input ("ingresa la base del triangulo:")
    altura = input ("ingresa la altura del triangulo:")

    base= float(base)
    altura= float(altura)

    area= base* altura /2 

    print (f"El area del triangulo es de {area} cms cuadrados")


def MasOperaciones():
    num1= input("ingrese un numero: ")
    num2= input("ingrese otro numero: ")

    num1= int (num1)
    num2= int (num2)

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} % {num2} = {num1 % num2}")
    print(f"{num1} / {num2} = {num1 / num2}")



def MenuEjerciciosBasicos():
    
    auxEjerciciosBasicos= True

    while auxEjerciciosBasicos:
        print("Seleccione una opcion:")
        print("1. Ejercicio Radio Circulo")
        print("2. Ejercicio Par o Impar")
        print("3. Ejercicio Condicional Simple")     
        print("4. Ejercicio Area Triangulo")
        print("5. Mas Operaciones")
        print("6. Salir")

        opcion= input("Ingrese el numero de la opcion deseada: ")
        opcion= int (opcion)

        if opcion == 1:
            ejercicioRadioCirculo()
        elif opcion == 2:
            ejercicioParImpar()
        elif opcion == 3:
            condicionalSimple()
        elif opcion == 4:
            ejercicioAreaTriangulo()
        elif opcion == 5:
            MasOperaciones()
        elif opcion == 6:
            auxEjerciciosBasicos= False
            
        else:
            print("Opcion no valida. Intente de nuevo.")

