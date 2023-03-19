class Persona: # se define una clase Persona
    # atributos
    nombre = None # atributo nombre inicializado a None
    edad = None # atributo edad inicializado a None

    # métodos
    def mostrar_datos(self): # define un método llamado mostrar_datos
        print(f'Nombre: {self.nombre}') # imprime el valor del atributo nombre
        print(f'Edad: {self.edad}') # imprime el valor del atributo edad