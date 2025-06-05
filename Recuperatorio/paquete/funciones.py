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

def cargar_secuencialmente(matriz: list) -> list:

    '''
    Carga un matriz de manera secuencialmente

    Parametros:
    Recibe una lista

    Retorna un lista
    '''

    for i in range(len(matriz)):
        for j in range (len(matriz[i])):

            matriz[i][j] = int(input(f"Ingrese el stock para {i} del insumo {j}: "))
    
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


def ordenar_por_burbujeo (lista: list) -> list:

    if type(lista) != list:
        print("El parametro que reciba debe ser una lista")

    n = len(lista)

    for i in range(n):

        intercambio = False

        for j in range (0, n - 1):
            if lista[j] > lista[j + 1]:
                intercambio = True
                menor = lista[j + 1]

                lista[j + 1] = lista[j]
                lista[j] = menor

                print(f"Se intercambio el {menor} por {lista[j + 1]}")
        
        if intercambio == False:
            break
        
    return lista