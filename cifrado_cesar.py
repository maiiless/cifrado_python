def cifrar_texto(texto, posicion):
    texto_final = ""
    for letra in texto:
        if letra.isupper():
            codigo_letra = ord(letra)
            posicion_inicial = codigo_letra - ord("A")
            posicion_final = (posicion_inicial + posicion) % 26
            letra_final = posicion_final + ord("A")
            letra_final = chr(letra_final)
            texto_final = texto_final + letra_final
        else:
            texto_final += letra

    return texto_final

def descifrar_texto(cifrado,posicion):
    texto_final = ""
    for letra in cifrado:
        if letra.isupper():
            codigo_letra = ord(letra)
            posicion_inicial = codigo_letra - ord("A")
            posicion_final = (posicion_inicial - posicion) % 26
            letra_final = posicion_final + ord("A")
            letra_final = chr(letra_final)
            texto_final = texto_final + letra_final
        else:
            texto_final += letra
            
    return texto_final

def run():
    seleccion = input(print("""
    Cifrado Cesar:
    Seleccione una opción:
    1. Cifrar un texto
    2. Descifrar un texto    
    """))

    if seleccion == "1":
        posicion = int(input("N° desplazamiento: "))
        texto_plano = input("Texto a cifrar: ")
        resultado = cifrar_texto(texto_plano, posicion)
        print("Texto cifrado: "+ resultado)

    elif seleccion == "2":
        posicion = int(input("N° desplazamiento: "))
        texto_cifrado = input("Texto a descifrar: ")
        resultado = descifrar_texto(texto_cifrado, posicion)
        print("Texto descifrado: "+ resultado)

    else:
        print("Seleccione una opción válida")
if __name__ == '__main__':
    run()