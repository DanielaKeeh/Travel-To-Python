
def Verificador_De_Votacion(): 

    ciudadano= input("es usted ciudadano?(si 1/no 2): ") 
    ciudadano= int(ciudadano) 
    
    if ciudadano != 1 and ciudadano !=2: 
        print("respuesta no valida.") 

        return 
    
    edad= input("ingresa tu edad:") 
    edad= int (edad) 

    if edad >=18 and ciudadano== 1: 
        print("usted puede votar.") 
        
    else: print("usted no puede votar.")