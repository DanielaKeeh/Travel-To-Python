def validar_contrasena():

    crea= input("crea una contraseña: ")
    crea= str(crea)

    intentos =0

    while intentos < 3:
        confirma= input("confirma la contraseña:")
        confirma= str(confirma)


        if confirma != crea:
            print("contraseña incorrecta.")
            intentos= intentos+1
        
        else:
            
            break 

    if  intentos== 3:
            print("intentos agotados.")
    else:
        print("contraseña correcta")
