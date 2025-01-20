def OrdenarLista(lista):
    lista.sort()
    lista.reverse()

    with open("ListaOrdenada.txt", "w") as file:
        for i in lista:
            file.write(str(i)+"\n")
OrdenarLista([90328490,34124,3475,3,4654,123,5,424,])
def NumeroPar(fichero):
    import os

    if os.path.isfile(fichero):
        with open(fichero,"r") as file:
            numeros = file.readlines()

            with open("ListaPares","w") as file:
                for numero in numeros:
                    if (int(numero)) %2 ==0:
                        file.write(numero)
    else:
        print("El fichero con nombre: "+ fichero +"no existe")
OrdenarLista([90328490,34124,3475,3,4654,123,5,424,])
NumeroPar("Listardenada.txt")

