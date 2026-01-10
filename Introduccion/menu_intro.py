from AprendiendoPython import MenuAprendiendo
from EjerciciosBasicos import MenuEjerciciosBasicos
from EjerciciosCondicionales import MenuCondicionales


def menu_intro():
    
    aux_intro= True

    while aux_intro:
        print("Seleccione una opcion:")
        print("1. Aprendiendo Python")
        print("2. Ejercicios Basicos")
        print("3. Ejercicios Condicionales")  
        print("4. Salir")   
        

        opcion= input("Ingrese el numero de la opcion deseada: ")
        opcion= int (opcion)

        if opcion == 1:
            MenuAprendiendo()
        elif opcion == 2:
            MenuEjerciciosBasicos()
        elif opcion == 3:
            MenuCondicionales()
        elif opcion== 4:
            aux_intro= False
            
        else:
            print("Opcion no valida. Intente de nuevo.")
    



