from Introduccion.menu_intro import menu_intro
from PrimerProyecto.menupp import menu_pp
from SegundoProyecto.menusp import menu_sp


def main():
    
    aux= True

    while aux:
        print("Seleccione una opcion:")
        print("1. Introduccion")
        print("2. Primer Proyecto (pequeños ejercicios)")
        print("3. Segundo Proyecto")
        print("5. Salir")

        opcion= input("Ingrese el numero de la opcion deseada: ")
        opcion= int (opcion)

        if opcion == 1:
            menu_intro()
        elif opcion == 2:
            menu_pp()
        elif opcion == 3:
            menu_sp()
        elif opcion == 5:
            aux= False
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__== "__main__":
    main()

    