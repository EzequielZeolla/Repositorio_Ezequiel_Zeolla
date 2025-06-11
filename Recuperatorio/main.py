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
            
            matriz_stock = cargar_secuencialmente(matriz_stock,depositos, insumos)

            for fila in matriz_stock:
                print(fila)
        
        case 2:
            if not matriz_stock:
                print("Primero tienes que cargar los stock")
            else:
                mostrar_deposito(matriz_stock, depositos, 5000)

        case 3:
            if not matriz_stock:
                print("Primero tienes que cargar los insumos")
            else:
                mostrar_insumos(matriz_stock, insumos, 3000)
                

        case 4:
            if not matriz_stock:
                print("Debes ingresar los insumos")
            else:
                identificar_deposito_mayor(matriz_stock, insumos, depositos)
            
        
        case 5:
            print("No llegue")
        
        case 6:
                print("No llegue")

        case _:
            menu = False
            print("Saliendo del programa...")
