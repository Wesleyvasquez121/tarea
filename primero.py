class Estudiante:
   def __init__(self, nombre, id_estudiante, edad, curso, promedio):
       self.nombre = nombre
       self.id_estudiante = id_estudiante
       self.edad = edad
       self.curso = curso
       self.promedio = promedio
   def actualizar_promedio(self, nuevo_promedio):
       self.promedio = nuevo_promedio
   def mostrar_info(self):
       return (f"Nombre: {self.nombre}\n"
               f"ID: {self.id_estudiante}\n"
               f"Edad: {self.edad}\n"
               f"Curso: {self.curso}\n"
               f"Promedio: {self.promedio:.2f}")

class Escuela:
   def __init__(self):
       self.estudiantes = []
   def agregar_estudiante(self):
       nombre = input("Ingrese el nombre del estudiante: ")
       id_estudiante = input("Ingrese el ID del estudiante: ")
       edad = int(input("Ingrese la edad del estudiante: "))
       curso = input("Ingrese el curso del estudiante: ")
       promedio = float(input("Ingrese el promedio del estudiante: "))
       estudiante = Estudiante(nombre, id_estudiante, edad, curso, promedio)
       self.estudiantes.append(estudiante)
       print(f"\nEl estudiante '{nombre}' ha sido agregado con éxito.\n")
   def actualizar_promedio(self):
       id_estudiante = input("Ingrese el ID del estudiante para actualizar el promedio: ")
       nuevo_promedio = float(input("Ingrese el nuevo promedio: "))
       for estudiante in self.estudiantes:
           if estudiante.id_estudiante == id_estudiante:
               estudiante.actualizar_promedio(nuevo_promedio)
               print(f"\nEl promedio del estudiante '{estudiante.nombre}' ha sido actualizado.\n")
               return
       print("Estudiante no encontrado.\n")
   def mostrar_estudiantes(self):
       if not self.estudiantes:
           print("No hay estudiantes registrados.\n")
       else:
           print("Lista de estudiantes:\n")
           for estudiante in self.estudiantes:
               print(estudiante.mostrar_info())
               print("")  # Espacio entre estudiantes

# Ejemplo de uso
escuela = Escuela()
while True:
   print("1. Agregar un estudiante")
   print("2. Actualizar promedio")
   print("3. Mostrar estudiantes")
   print("4. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       escuela.agregar_estudiante()
   elif opcion == "2":
       escuela.actualizar_promedio()
   elif opcion == "3":
       escuela.mostrar_estudiantes()
   elif opcion == "4":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")
