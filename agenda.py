#Agenda de teléfonos almacenada en forma de diccionario
agenda = {'Alba': '635958412','Alberto':'665987723','Albertina':'626845721','Carlos':'658986598','Pepe':'658986599','Pepito':'658986510','Pep':'658986511','Pepon':'658986512','Alvarez':'631223344','Alex':'658986569'}

#Escoger función a utilizar
def main():
    print('Opciones:\n1: Introducir datos\n2: Buscar contacto\n3: Buscar personas')
    opcion = input('Introduzca opción: ')
    num = int(opcion)
    if num==1:
        introDatos()
    elif num==2:
        buscarContacto()
    elif num==3:
        buscarPersona()
    else:
        print(f'La opción {num} no existe')

#Añadir personas a la agenda
def introDatos():
    nombre = input('Nombre: ')
    telefono = input('Teléfono: ')
    if nombre not in agenda: 
        agenda[nombre]=telefono
        print(f'El contacto {nombre} se ha añadido correctamente')
    else: 
        print(f'El contacto {nombre} ya existe en la agenda')


#Buscar el teléfono de cualquier persona en la agenda
def buscarContacto():
    buscar = input('Nombre a buscar: ')
    if buscar in agenda:
        print(f'El teléfono de {buscar} es {agenda.get(buscar)}')
    else: 
        print(f'El contacto {buscar} no existe en la agenda')

#Buscar todas las personas que empiecen con el texto introducido
def buscarPersona():
    texto = input('texto a buscar: ')
    print('Los siguientes contactos coinciden con el texto introducido: ')
    for nombre, telefono in agenda.items():
        if nombre.startswith(texto):
            print(f'{nombre} --> {telefono}')
       
main()