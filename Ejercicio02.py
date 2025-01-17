def CrearLista():
    open("Lista.txt","a").close()

def NombreAlumno():
    nombre=input("Dime el nombre del alumno:")
    nota=input("Dime la nota del alumo:")
    try:
        with open("Lista.txt") as f:
            for linea in f:
                Alumno=linea.strip()
    except FileNotFoundError:
        print("El alumno no está")

def AgregarAlumno():
    nombre=input("Dime nombre del alumno:")
    with open ("Lista.txt") as f:
        f.write(f"{nombre}\n")

def Aprobados():
    nota = input("Introduce tu nota:")
    with open ("Lista.txt","a") as f:
        f.write(f"{nota}\n")
def Alumnos():
    with open("Lista.txt","a") as f:
        print("Alumnos")
def menu():
    while True:
        print("\n1. Añadir Alumno\n2.Numero aprobados\n3.Mostrar alumnos")
        opcion=input("Elija una opcion")
        if opcion== "1": AgregarAlumno
        if opcion== "2": Aprobados
        if opcion == "3": Alumnos