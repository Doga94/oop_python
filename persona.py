class Persona: # se define una clase Persona
    # atributos
    #nombre = None # atributo nombre inicializado a None
    #edad = None # atributo edad inicializado a None

    #Constructor
    def __init__(self, nombre, edad):
        # Constructor que toma dos parámetros: "nombre" y "edad"
        # El primer parámetro siempre debe ser "self", que se refiere a la instancia actual de la clase.
        self.nombre = nombre
        # Establece el valor del atributo "nombre" de la instancia actual de la clase al valor del parámetro "nombre" que se pasó al constructor.
        self.edad = edad
        # Establece el valor del atributo "edad" de la instancia actual de la clase al valor del parámetro "edad" que se pasó al constructor.


    # métodos
    def mostrar_datos(self): # define un método llamado mostrar_datos
        print(f'Nombre: {self.nombre}') # imprime el valor del atributo nombre
        print(f'Edad: {self.edad}') # imprime el valor del atributo edad

    def __str__(self):
        # Método especial que se llama automáticamente cuando se utiliza la función print() con una instancia de la clase.
        # Devuelve una representación en cadena (string) de la instancia actual de la clase.
        # La cadena contiene el valor de los atributos "nombre" y "edad" de la instancia actual de la clase.
        # La sintaxis f-string de Python se utiliza para incluir los valores de los atributos dentro de la cadena.
        # El carácter de escape "\n" se utiliza para agregar un salto de línea entre los valores de los atributos.
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'