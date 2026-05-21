class Videojuego:

    def __init__(self, titulo, plataforma, anioLanzamiento, precio):

        self.__titulo = titulo
        self.__plataforma = plataforma
        self.__anioLanzamiento = anioLanzamiento
        self.__precio = precio

    # GETTERS
    def getTitulo(self):
        return self.__titulo

    def getPlataforma(self):
        return self.__plataforma

    def getAnioLanzamiento(self):
        return self.__anioLanzamiento

    def getPrecio(self):
        return self.__precio

    # SETTERS
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setPlataforma(self, plataforma):
        self.__plataforma = plataforma

    def setAnioLanzamiento(self, anio):
        self.__anioLanzamiento = anio

    def setPrecio(self, precio):
        self.__precio = precio

    # MOSTRAR INFORMACION
    def mostrarInformacion(self):

        print("Titulo:", self.__titulo)
        print("Plataforma:", self.__plataforma)
        print("Año:", self.__anioLanzamiento)
        print("Precio:", self.__precio)

        print("----------------------")