import pickle

class Inventario:

    def __init__(self):

        self.__videojuegos = []

    # AGREGAR VIDEOJUEGO
    def agregarVideojuego(self, juego):

        self.__videojuegos.append(juego)

    # LISTAR INVENTARIO
    def listarInventario(self):

        for juego in self.__videojuegos:

            juego.mostrarInformacion()

    # BUSCAR POR PLATAFORMA
    def buscarPorPlataforma(self, plataforma):

        for juego in self.__videojuegos:

            if juego.getPlataforma() == plataforma:

                juego.mostrarInformacion()

    # GUARDAR DATOS
    def guardarDatos(self, nombreArchivo):

        archivo = open(nombreArchivo, "wb")

        pickle.dump(self.__videojuegos, archivo)

        archivo.close()

        print("Datos guardados correctamente")

    # CARGAR DATOS
    def cargarDatos(self, nombreArchivo):

        archivo = open(nombreArchivo, "rb")

        self.__videojuegos = pickle.load(archivo)

        archivo.close()

        print("Datos cargados correctamente")