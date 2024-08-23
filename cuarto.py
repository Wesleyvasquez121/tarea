class Articulo:
   def __init__(self, categoria, especificacion, precio_compra):
       self.categoria = categoria  # Cuaderno o Lápiz
       self.especificacion = especificacion  # 50 hojas, 100 hojas, grafito, colores
       self.precio_compra = precio_compra
       self.marca = self.definir_marca()
       self.precio_venta = self.calcular_precio_venta()
   def definir_marca(self):
       if self.categoria == "cuaderno":
           return "HOJITAS"
       elif self.categoria == "lapiz":
           return "RAYAS"
       else:
           return "Desconocida"
   def calcular_precio_venta(self):
       return self.precio_compra * 1.30
   def mostrar_informacion(self):
       detalles = [
           f"Categoría: {self.categoria.capitalize()}",
           f"Especificación: {self.especificacion}",
           f"Marca: {self.marca}",
           f"Precio de compra: ${self.precio_compra:.2f}",
           f"Precio de venta: ${self.precio_venta:.2f}"
       ]
       return detalles

class Papeleria:
   def __init__(self):
       self.articulos = []  # Lista para almacenar los artículos
   def registrar_articulo(self):
       categoria = input("Ingrese la categoría del artículo (cuaderno/lapiz): ").lower()
       if categoria == "cuaderno":
           especificacion = input("Ingrese la cantidad de hojas (50/100): ")
           if especificacion not in ["50", "100"]:
               print("Cantidad de hojas no válida. Debe ser 50 o 100.")
               return
       elif categoria == "lapiz":
           especificacion = input("Ingrese el tipo de lápiz (grafito/colores): ").lower()
           if especificacion not in ["grafito", "colores"]:
               print("Tipo de lápiz no válido. Debe ser grafito o colores.")
               return
       else:
           print("Categoría de artículo no válida.")
           return
       precio_compra = float(input("Ingrese el precio de compra del artículo: "))
       articulo = Articulo(categoria, especificacion, precio_compra)
       self.articulos.append(articulo)
       print(f"\nEl artículo {categoria} ha sido registrado con éxito.\n")
   def mostrar_articulos(self):
       if not self.articulos:
           print("No hay artículos registrados.\n")
       else:
           print("Artículos registrados:\n")
           for articulo in self.articulos:
               for detalle in articulo.mostrar_informacion():
                   print(detalle)
               print("")  # Espacio entre artículos

# Ejemplo de uso
papeleria = Papeleria()
while True:
   print("1. Registrar un artículo")
   print("2. Mostrar todos los artículos")
   print("3. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       papeleria.registrar_articulo()
   elif opcion == "2":
       papeleria.mostrar_articulos()
   elif opcion == "3":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")
