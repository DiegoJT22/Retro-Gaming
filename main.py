from inventario import *
from videojuego import *


# CREAR INVENTARIO
inventario = Inventario()


# INGRESAR 3 VIDEOJUEGOS POR TECLADO
for i in range(3):

    print("Ingrese los datos del videojuego", i + 1)

    titulo = input("Titulo: ")

    plataforma = input("Plataforma: ")

    anio = int(input("Año de lanzamiento: "))

    precio = float(input("Precio: "))

    # CREAR OBJETO
    juego = Videojuego(titulo, plataforma, anio, precio)

    # AGREGAR AL INVENTARIO
    inventario.agregarVideojuego(juego)

    print("-------------------------")


# MOSTRAR INVENTARIO ORIGINAL
print("INVENTARIO ORIGINAL")

inventario.listarInventario()


# GUARDAR DATOS
inventario.guardarDatos("inventario.dat")


# SIMULAR REINICIO
inventarioNuevo = Inventario()


# CARGAR DATOS
inventarioNuevo.cargarDatos("inventario.dat")


# MOSTRAR INVENTARIO CARGADO
print("INVENTARIO CARGADO")

inventarioNuevo.listarInventario()