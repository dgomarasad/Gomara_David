import os
def OrdenarLista():
    n=int(input('Introduce un numero entero: '))
    if 1 <= n <= 10:
        with open (f"ListaOrdenada.txt","w") as file :
            file.write(n)
            print(n())
    else:
        print(f"El numero no existe")
resultado = OrdenarLista