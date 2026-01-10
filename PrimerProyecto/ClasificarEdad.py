def clasificar_Edad():  
        
        edad= input("ingresa una edad: ")
        edad=int(edad)

        if edad >=65:
                print("usted es un adulto mayor.")
        elif edad >=30:
                print("usted es un adulto.")
        elif edad >=18:
                print("usted es un joven.")
        elif edad >=13:
                print("usted es un adolescente.")
        else:
                print("usted es un niño.")