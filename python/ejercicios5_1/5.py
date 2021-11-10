def ahorcado(palabra, acertadas ):
    guion="_"
    salida=""
    for x in palabra:
        if x in acertadas:
            salida += x
        else:
            salida += guion
    return salida


import random
lista = ["cerillas", "patrulla", "papel", "azor", "alerones", "conversar", "sollozo", "manzana"]
palabra = random.choice(lista)
if __name__=="__main__":
    acertadas = ""
    while True:
        try:
            letra = input("Introduce una letra: ")
            if palabra != ahorcado(palabra,letra):
                if (letra in palabra) :
                    acertadas+= letra
                print(ahorcado(palabra, acertadas))
            else:
                print("Has acertado la palabra.")
                break
        except ValueError:
            print ("Introduce una letra.")