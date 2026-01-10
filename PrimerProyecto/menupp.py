from numeros import Numero_Par_Impar
from PrimerProyecto.ValidarContrasena import validar_contrasena
from ClasificarEdad import clasificar_Edad
from VerificadorVotacion import Verificador_De_Votacion

def menu_pp():
    
    auxPP= True

    while auxPP:
        print("Seleccione una opcion:")
        print("1. Validar Contraseña")
        print("2. Clasificar Edad")
        print("3. Verificador De Votacion")
        print("4. Numero Par o Impar")
        print("5. Salir")

        opcion= input("Ingrese el numero de la opcion deseada: ")
        opcion= int (opcion)

        if opcion == 1:
            validar_contrasena()
        elif opcion == 2:
            clasificar_Edad()
        elif opcion == 3:
            Verificador_De_Votacion()
        elif opcion == 4:
            Numero_Par_Impar()
        elif opcion == 5:
            auxPP= False
        else:
            print("Opcion no valida. Intente de nuevo.")

