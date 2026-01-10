

def conociendo_python():

    ##experimentando la sintaxis básica de python

    print("hola mundo")

    nombre = "Daniela"
    print ("hola," + nombre)

    Edad = 20
    print (f"{nombre} tiene {Edad} años")

    Estatura = input ("cual es tu estatura:")

    print (f"la estatura de {nombre} es de {Estatura} centimetros")

    Nombre = input("ingresa tu nombre:")
    print(f"hola, {Nombre} bienvenido")

    edad = input("ingresa tu edad:")
    edad = int (edad)
    print (f"tu tendras {edad +1} el proximo año")

    x=10
    y=5
    suma = x+y
    print(f"la suma de {x} y {y} es igual a {suma}")

    area_cuadrado = x**2
    print (f"el area de un cuadrado con lado {x} es {area_cuadrado}")

def ejercicio_1():

    Nombre = input("ingresa tu nombre:")
    Edad = input("ingresa tu edad:")
    Edad= str(Edad)

    Producto= Nombre + Edad 

    print (f"el producto de {Nombre} y {Edad} es {Producto}")

def ejercicio_2():

    GradosCelsius = input("ingresa los grados celsius:")
    GradosCelcius = float(GradosCelsius)

    Farenheit = (1.8 * GradosCelcius) + 32

    print (f"Los {GradosCelcius} grados celisius son {Farenheit} en farenheit.") 

def EjercicioInputs():

    Nombre = input ("ingresa tu nombre:") 
    Edad = input ("ingresa tu edad:")

    print (f"tu nombre es {Nombre} y tu edad es {Edad}")

def TiposDeDatos():

    numero = 10
    print(f"la variable llamada numero es de tipo {type(numero)} y tiene valor {numero}")

    flotante = 10.00 
    print(f"la variable llamada flotante es de tipo {type(flotante)} y tiene valor de {flotante}")

    cadenita = "q rollo plebeeeeees"
    print(f"la variable llamada cadenita es de tipo {type(cadenita)} y tiene valor de {cadenita}")

    Daniela = True
    print(f"la variable llamada Daniela es de tipo {type(Daniela)} y tiene valor de {Daniela}")

    Cadena = input("ingresa una cadena de texto:")
    Cadena = str(Cadena)

    Numerito =input("ingresa un numero:")
    Numerito =  int(Numerito)

    print(f"""la variable llamada Cadena es de tipo {type(Cadena)} 
        y tiene como valor {Cadena}, Asi mismo la variable 
        llamada numerito es de tipo {type(Numerito)} y 
        tiene como valor {Numerito}""")
    

def operadores_aritmeticos():

    a= 7
    b= 3

    resultado = a+b 

    #OPERADORES ARIMETICOS

    print(f"{a}+ {b} = {a+b}")

    print(f"{a}- {b} = {a-b}")

    print(f"{a}/{b} = {a/b}")

    print(f"{a}// {b} = {a//b}")

    print(f"{a} *{b} = {a*b}")

    print(f"{a} ** {b} = {a**b}")

    print(f"{a} % {b} = {a%b}")


def operadores_compuestos():

    x=10
    
    x= input("ingrese saldo a su cuenta:")
    x= int (x)

    print(f"valor inicial de su saldo {x}")

    x+= 100
    print(f"deposito de 100 pesos... Saldo en su cuenta {x}")

    x-=300
    print(f"Transferencia de 300... Saldo en su cuenta: {x}")

    x*=200
    print(f"Deposito de a cuenta bancaria: {x}")


    y=20
    print(f"valor inicial de {y}")

    y+= 5
    print(f"despues de x+ =5: {y}")

    y-=3
    print(f"despues de x-=3: {y}")

    y*=2
    print(f"despues de x*=2: {y}")

    y /=4
    print(f"después de x/=4: {y}")

def conversion_de_tipos():

    numero= input("ingresa un numero: ")
    numero= int (numero)

    print(f"el dato ingresado es de tipo {type(numero)} y su valor es {numero}")

    cadena = str (numero)

    print(f"el dato ingresado ha cambiado a tipo {type(cadena)} y su valor es {cadena}")

    print("----------------------------------------------------")

    numero = input("ingresa un numero:")
    numero = int (numero)

    cuadrado = float (numero)
    cuadrado = numero ** 2


    print (f"el cuadrado de {numero} es {cuadrado}")

def concatenacion_e_indexacion():

    #concatenación
    nombre= input("ingresa tu nombre:")
    saludo = "  Hola, "

    repeticion= saludo + nombre 
    print(repeticion *3 )


    #indexación 
    palabra = input("ingresa una palabra:")
    palabra= str (palabra)

    print(palabra [0])
    print(palabra [1])
    print(palabra [2])

    print(palabra[0:4])
    print(palabra[7:])

def MenuAprendiendo():
    
    auxAprendiendo= True

    while auxAprendiendo:
        print("Seleccione una opcion:")
        print("1. Conociendo Python")
        print("2. Ejercicio 1")
        print("3. Ejercicio 2")     
        print("4. Ejercicio Inputs")
        print("5. Tipos De Datos")
        print("6. Operadores Aritmeticos")
        print("7. Operadores Compuestos")
        print("8. Conversion De Tipos")
        print("9. Concatenacion e Indexacion")
        print("10. Salir")

        opcion= input("Ingrese el numero de la opcion deseada: ")
        opcion= int (opcion)

        if opcion == 1:
            conociendo_python()
        elif opcion == 2:
            ejercicio_1()
        elif opcion == 3:
            ejercicio_2()
        elif opcion == 4:
            EjercicioInputs()
        elif opcion == 5:
            TiposDeDatos()
        elif opcion == 6:
            operadores_aritmeticos()
        elif opcion== 7:
            operadores_compuestos()
        elif opcion== 8:
            conversion_de_tipos()
        elif opcion== 9:
            concatenacion_e_indexacion()
        elif opcion== 10:
            auxAprendiendo= False
            
        else:
            print("Opcion no valida. Intente de nuevo.")

