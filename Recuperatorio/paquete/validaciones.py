def validar_numero(dato: str) -> bool:

    bandera = True
    indice = 0

    while bandera and indice < len(dato):
        
        if ord(dato[indice]) > 47 and ord(dato[indice]) < 58:
            indice += 1
        else:
            bandera = False

    return bandera