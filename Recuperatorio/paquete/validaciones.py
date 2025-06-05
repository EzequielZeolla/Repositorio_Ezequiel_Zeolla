def validar_numero(dato: str) -> bool:

    bandera = True
    indice = 0

    while bandera and indice < len(dato):
        
        if ord(dato[indice]) > 47 and ord(dato[indice]) < 58:
            indice += 1
        else:
            bandera = False

    return bandera

def validar_letra(dato: str) -> bool:

    bandera = True
    indice = 0

    while bandera and indice < len(dato):
        if (97 <= ord(dato[indice]) <= 122) or (65 <= ord(dato[indice]) <= 90):
            indice += 1
        else:
            bandera = False