diccionario = {}
while True: 
    seleccion = int(input('Eliga una de las siguientes opciones:\n'
                          ' 1- Añadir un alumno\n'
                          ' 2- Mostrar número aprobados\n'
                          ' 3- Mostrar todo el alumnado\n'))
    if seleccion == 1:
        alumno = input('Nombre del alumno: ')
        aprobado = bool(int(input('Indica 0 si ha '
                                  'suspendido 1 si ha abrobado: \n')))
        diccionario[alumno] = aprobado

    elif seleccion == 2:
        aprobados = 0
        for aprobado in diccionario.values():
            if aprobado:
                aprobados += 1
        print('El  número de aprobados es: ' + str(aprobados)+'\n')
    elif seleccion == 3:
        print(diccionario.keys())
    else:
        print('Ha marcado una opción inexistente\n')