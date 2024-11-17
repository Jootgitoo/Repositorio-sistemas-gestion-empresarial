from os import listdir, mkdir, remove, rmdir
from os.path import exists, isdir
import shutil

ruta = "./RECETAS"

def leerOpcionMenu(opcion):
    if opcion == 1:
        preguntarCategoria()
    elif opcion == 2:
        crearReceta()
    elif opcion == 3:
        crearCategoria()
    elif opcion == 4:
        eliminarReceta()
    elif opcion == 5:
        eliminarCategoria()
    elif opcion == 6:
        print("Hasta otra")
        exit()
    else:
        print("Opción no válida, seleccione una opción que aparezca en el menú.")
        leerOpcionMenu(int(input("Elija una opción válida: ")))

def crearReceta():
    categorias = listdir(ruta)
    for i in range(len(categorias)):
        print(str(i + 1) + ". " + categorias[i])
    opcion = int(input("¿A cuál categoría pertenece la receta que quieres crear?: "))
    receta = input("¿Cuál es el nombre de la receta?: ")
    rutaNueva = ruta + "/" + categorias[opcion - 1] + "/" + receta + ".txt"


    if not exists(rutaNueva):
        #w mejor que x, asi sobreescribe el archivo si ya existe
        with open(rutaNueva, "w") as f:
            contenido = input("Escribe la receta:\n")
            f.write(contenido)
        print("Receta creada corectamente")
    else:
        print("La receta ya existe")

def preguntarCategoria():
    categorias = listdir(ruta)
    for i in range(len(categorias)):
        print(str(i + 1) + ". " + categorias[i])
    opcion = int(input("¿A cuál categoría pertenece la receta que quieres leer?: "))
    rutaNueva = ruta + "/" + categorias[opcion - 1]
    preguntarReceta(rutaNueva)

def preguntarReceta(ruta):
    recetas = listdir(ruta)
    for i in range(len(recetas)):
        print(str(i + 1) + ". " + recetas[i])
    opcion = int(input("¿Cuál receta deseas abrir?: "))
    ruta = ruta + "/" + recetas[opcion - 1]
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
    print("=================================")
    print(contenido)
    print("=================================")

def crearCategoria():
    nombre = input("Introduce el nombre de la nueva categoría: ")
    rutaNueva = ruta + "/" + nombre
    if not exists(rutaNueva):
        mkdir(rutaNueva)
        print("Categoría creada correctamente")
    else:
        print("La categoría ya existe")

def eliminarReceta():
    categorias = listdir(ruta)

    for i in range(len(categorias)):
        print(str(i + 1) + ". " + categorias[i])
    opcion = int(input("¿De cuál categoría es la receta que quieres eliminar?: "))
    rutaCategoria = ruta + "/" + categorias[opcion - 1]
    recetas = listdir(rutaCategoria)

    for i in range(len(recetas)):
        print(str(i + 1) + ". " + recetas[i])
    opcionReceta = int(input("¿Cuál receta deseas eliminar?: "))
    rutaReceta = rutaCategoria + "/" + recetas[opcionReceta - 1]
    remove(rutaReceta)
    print("Receta eliminada correctamente.")

def eliminarCategoria():
    categorias = listdir(ruta)
    for i in range(len(categorias)):
        print(str(i + 1) + ". " + categorias[i])
    opcion = int(input("¿Cuál categoría deseas eliminar?: "))
    rutaCategoria = ruta + "/" + categorias[opcion - 1]
    if isdir(rutaCategoria):
        # Lo de abajo se supone que borra de manera recursiva el contenido y luego la categoria
        shutil.rmtree(rutaCategoria)
        print("Categoría y su contenido eliminados correctamente.")
    else:
        print("La categoría no existe.")

# Inicialización del programa
print("------------------------------------------------------------------------------------")
print("      ***** Bienvenido a tu libro de recetas digital *****")
print("------------------------------------------------------------------------------------")
print("Si quieres consultar las recetas sin encender este asistente, puedes hacerlo")
print("consultando la ruta " + ruta + " de tu equipo, dentro de este proyecto")
print("------------------------------------------------------------------------------------")

if not exists(ruta):
    mkdir(ruta)

while True:
    print("\n1. Leer receta\n2. Crear receta\n3. Crear categoría\n4. Eliminar receta\n5. Eliminar categoría\n6. Salir\n")
    leerOpcionMenu(int(input("Elija una de las opciones que aparecen arriba: ")))

