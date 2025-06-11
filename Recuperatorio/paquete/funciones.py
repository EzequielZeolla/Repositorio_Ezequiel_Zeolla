from paquete.validaciones import *

def inicializar_matriz(cant_filas: int,
                       cant_columnas: int,
                       valor: any = 0) -> list:
    
    '''
    Inicilializa una matriz

    Parametros:
    recibe una lista

    Retorna una lista
    '''
    
    matriz = []

    for _ in range(cant_filas):
        filas = [valor] * cant_columnas

        matriz += [filas]
    
    return matriz

def cargar_secuencialmente(matriz: list,
                           depositos: list[str],
                           insumos: list[str]) -> list:

    '''
    Carga un matriz de manera secuencialmente

    Parametros:
    Recibe una lista

    Retorna un lista
    '''

    for i in range(len(matriz)):
        for j in range (len(matriz[i])):
            validar = False

            while not validar:
                valor = input(f"Ingrese el stock para {depositos[i]} del insumo {insumos[j]}: ")

                if validar_numero(valor):
                    valor = int(valor)
                    validar = True
                    matriz[i][j] = valor
                else:
                    print("Ingresa un numero")
            
    
    return matriz

def cargar_distribuidamente(matriz: list) -> list:

    '''
    Carga matriz o modifica una matriz de manera distruibuida

    Parametros:
    Recibe una lista

    Retorna una lista
    '''

    seguir = "s"

    while seguir == "s":

        fila = int(input("Ingresa la fila que se encuentra el numero que deseas cambiar o modificar: "))
        columna = int(input("Ingrese la columna donde se encuentre el numero que deseas cargar o modificar: "))
        valor = int(input("Ingrese el valor: "))
        seguir = input("¿Deseas seguir cargando o modificando algun valor?")

        matriz[fila][columna] = valor
    
    return matriz

def mostrar_deposito(matriz: list,
                     deposito: list[str],
                     maximo: int):
    
    for i in range(len(matriz)):
        acumulador = 0
        for j in range(len(matriz[i])):

            acumulador += matriz[i][j]
        
        if acumulador > maximo:
            print(f"El deposito {deposito[i]} tiene {acumulador} insumos")

def mostrar_insumos(matriz: list,
                    insumos:list[str],
                    maximo: int):
    
    acumulador_insumo = [0] * len(insumos)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            acumulador_insumo[j] += matriz[i][j]
        
    for j in range(len(acumulador_insumo)):
        if acumulador_insumo[j] > maximo:
            print(f"El insumo {insumos[j]} cuenta con {acumulador_insumo[j]} insumos")

def identificar_deposito_mayor(matriz: list,
                               insumos: list[str],
                               depositos: list[str]):
    
    mayor_cantidades = [0] * len(insumos)
    deposito_mayor = [0] * len(insumos)

    for i in range(len(matriz)):
        for j in range (len(matriz[i])):

            if matriz[i][j] > mayor_cantidades[j]:
                mayor_cantidades[j] = matriz[i][j]
                deposito_mayor[j] = i
                
    for j in range(len(insumos)):
        print(f"El insumo {insumos[j]} tiene la mayor cantidad en el deposito de {depositos[deposito_mayor[j]]} con {mayor_cantidades[j]} unidades")
