from paquete.funciones import *

depositos = ["Rosario", "Cordoba", "Salta", "Bahia Blanca"]
insumos = ["Arduinno UNO", "Sensor de temperatura", "Cable USB", "Display LCD", "Protoboard"]



matriz_stock = []

menu = True

while menu:

    print("")
    print("1-Cargar secuencialmente los insumos")
    print("2-Mostrar los depositos con stock superior a 5000 unidades")
    print("3-Mostar los insumos con stock superior a 3000 unidades")
    print("4-Deposito con mayor candad de unidades")
    print("5-Registrar ventas de insumos")
    print("6-Informe de ventas por deposito")
    print("")



    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            matriz_stock = inicializar_matriz (len(depositos),
                                                len(insumos))
            
            matriz_stock = cargar_secuencialmente(matriz_stock)

            for fila in matriz_stock:
                print(fila)
        
        case 2:
            if not matriz_stock:
                print("Primero tienes que cargar los stock")
            else:
                for i in range(len(matriz_stock)):
                    for j in range(len(matriz_stock[i])):
                        if matriz_stock[i][j] > 5000:
                            print(f"Los depositos de {depositos[i]} tienen un stock de {matriz_stock[i][j]}")
                        else:
                            print("Ningun deposito supero las 5000 unidades")

        case 3:
            if not matriz_stock:
                print("Primero tienes que cargar los insumos")
            else:
                for i in range(len(matriz_stock)):
                    for j in range(len(matriz_stock[i])):
                        if matriz_stock [i][j] > 3000:
                            print(f"Los insumos de {matriz_stock[j]} son {matriz_stock[i][j]}")
                        else:
                            print("Ningun insumo superar las 3000 unidades")

        case 4:
            if not matriz_stock:
                print("Debes ingresar los insumos")
            else:
                for i in range(len(matriz_stock)):
                    cant_mayor = matriz_stock[i][0]

                    for j in range (len(matriz_stock[i])):
                        if matriz_stock > cant_mayor:
                            cant_mayor = matriz_stock[i][j]

                            print(f"El deposito de {depositos[i]} tiene mayor cantidad de unidades por insumos")
        
        case 5:
            print("No llegue")
        
        case 6:
                print("No llegue")

        case 9:
            menu = False
            print("Saliendo del programa...")
