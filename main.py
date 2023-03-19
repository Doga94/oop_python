from persona import Persona # importa la clase Persona desde el archivo personas.py

persona1 = Persona('David', 29) # crea una instancia de la clase Persona llamada persona1
#persona1.nombre = 'David' # establece el atributo nombre de persona1 a 'David'
#persona1.edad = 29 # establece el atributo edad de persona1 a 29

#persona2 = Persona() # crea una instancia de la clase Persona llamada persona2
#persona2.nombre = 'Orlando' # establece el atributo nombre de persona2 a 'Orlando'
#persona2.edad = 25 # establece el atributo edad de persona2 a 25

#persona2.mostrar_datos() # llama al método mostrar_datos de persona2 para imprimir sus atributos
print('='*25) # imprime una línea separadora
persona1.mostrar_datos() # llama al método mostrar_datos de persona1 para imprimir sus atributos

##Cambiar el nombre de forma sencilla
persona1.nombre = 'Orlando'
persona1.mostrar_datos()

print(persona1)

