
def validar_contraseña(veces,letra,contraseña):
    contador = 0
    letra = letra.replace(":","")
    for x in contraseña:
        if letra==x:
            contador+=1
    lista_split = veces.split("-")
    if int(lista_split[0])<= contador <=int(lista_split[1]):
        return True
    return False


def validar_contraseña_2(posiciones,letra,contraseña):
    letra = letra.replace(":", "")
    posiciones = posiciones.replace("-","")
    for x in posiciones:
        if not contraseña[int(x)-1]==letra:
            return False
    return True