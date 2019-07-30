A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def lista_menor_10(lista):
    numero_do_usuario = int(input('Digite o número desejado:  '))
    lista_menor_10 = []
    for elemento in lista:
        if elemento < numero_do_usuario:
            lista_menor_10.append(elemento)
    print(lista_menor_10)



if __name__ == "__main__":
    lista_menor_10(A)