import os

class Empleado:
  
    def __init__(self):
        error = False
        while not error:
          try:
            self.nombreEmpleado = str(input("INGRESE EL NOMBRE DEL EMPLEADO: ").capitalize())
            self.sueldo = float(input("SUELDO DEL EMPLEADO: $ "))
            error = True
          except ValueError:
            os.system("clear")
            print("Introduce un monto de sueldo valido.")

    def Imprimir(self):
        print("NOMBRE EMPLEADO: ", self.nombreEmpleado)
        print("SUELDO EMPLEADO: $ ", self.sueldo)

    def Impuestos(self):
      if self.sueldo > 3000:
        print("El empleado " + self.nombreEmpleado + " tiene un sueldo mayor a $ 3000.00, por lo tanto debe pagar impuesto.")
      else:
        print("El empleado " + self.nombreEmpleado + " tiene un sueldo menor a $ 3000.00, por lo tanto NO debe pagar impuesto.")
  
    
salir = False
opcion = 0
while not salir:
  print()
  print("1-CARGAR EMPLEADO")
  print("2-IMPRIMIR DATOS")
  print("3-VERIFICAR IMPUESTO")
  print("4-SALIR")
  try:
    opcion = int(input("POR FAVOR, INGRESE UNA OPCION: -> "))
    if opcion == 1:
      os.system("clear")
      empleado = Empleado()
    elif opcion == 2:  
      os.system("clear")
      empleado.Imprimir()
    elif opcion == 3: 
      os.system("clear")
      empleado.Impuestos()
    elif opcion == 4:
      os.system("clear")
      print("FIN DEL PROGRAMA")
      salir = True
    else:
      os.system("clear")
      print("OPCION INCORRECTA!:")
  except ValueError:
    os.system("clear")
    print("INGRESE UNA OPCION VALIDA!")

