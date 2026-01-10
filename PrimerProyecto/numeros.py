def Numero_Par_Impar ():
    

    i=0 
    while i < 10:
        num= input("ingrese un numero:")
        num= int(num)
        i=i+1

        if num %2==0:
            print("el numero es par")
        else:
            print("el numero es impar")