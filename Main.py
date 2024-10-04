Tareas = [
    ("[1]","Estudiar para el examen","Revisar capitulos 1 a 5","En progreso"),
    ("[2]","Hacer ejercicio","Ir al gimnasio por 1 hora","completa"),
    ("[3]","Llamar al medico","Solicitar una cita para chequeo","Pendientre"),
    ("[4]","Enviar el informe","Eviar el informe a mi jefe por correo","En Progreso")
]

pendientes = []

print("-"*20)
print("[1]Agregar Tarea")
print("[2]Eliminar Tarea")
print("[3]Actualizar Estado")
print("[4]Mostrar Tarea")
print("[5]Fliltrar Tarea")
print("[6]Guardar Tarea")
print("[7]Cargar Tarea")
print("[0]Salir Tarea")
print("-"*20)
opcion = int(input("[?]Inserte una opcion:"))

if opcion == 1:
    agregar = input("Nueva tarea:")
    pendientes.append(agregar)
    print("Nueva tarea agregada")

if opcion == 2:
    eliminar = int(input("Que desea eliminar:"))

    if eliminar == 1:
        print(Tareas[1])
        print("Eliminado")
    
    if eliminar == 2:
        print(Tareas[2])
        print("Eliminado")

    if eliminar == 3:
        print(Tareas[3])
        print("Eliminado")

    if eliminar == 4:
        print(Tareas[4])
        print("Eliminado")

if opcion == 3:
    print("Estamos programando")

if opcion == 4:
    print("Mostrando")
    print(pendientes)

if opcion == 5:
    print("Estamos programando")

if opcion == 6:
    print("Estamos programando")

if opcion == 7:
    print("Estamos programando")

if opcion == 0:
    print("Esperamos tu regreso")


