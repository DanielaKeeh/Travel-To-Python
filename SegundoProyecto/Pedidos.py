from DataBase import DataBase
tienda = DataBase()

def Pedidos ():
    
    postre= input("que producto dese comprar?.")
    orden = int (input ("cuantos productos desea comprar?:"))

    if postre in tienda ['productos']:
        restantes= tienda ['productos'][postre]['Cantidad']- orden
        if restantes <0 :
            print ("No hay suficientes postres en stock...")
        else: 
            precio = tienda ['productos'][postre]['Precio']* orden
            print (f'total a pagar:{precio}')
            tienda ['productos'][postre]['Cantidad']= restantes
            print(f'Cantidad de postres restantes:{restantes}')
    else:
        print("el producto no existe en la tienda :C")