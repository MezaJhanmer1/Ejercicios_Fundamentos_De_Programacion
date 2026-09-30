#comenzamoos colacando el iniciador para la tabla
pila=[]
#definimos una funcion para el inicio de una pagina
def pag (url):
 pila.append(url)
 print("Visitando:",url)
 print("Historial : ",pila)

#/funcion para retroceder
def retrodecer():
 if len(pila)>1:
  pagina=pila.pop()
  #notificacion de la direccion de la pag
  print("Retrocediendo : " ,pagina)
  print("Regreso a :", pila[-1])
  print("HISTORIAL:",pila)
 else:
  print("No hay pagina que volver")
#creamos un def para mostra la pagina actual
def pagina_actual():
 if len(pila)>0:
  print("Pagina actual:",pila[-1])
 else:
  print("No hay paginas visitadas")
#programa principal

while True:
  #definimos el menu de opciones
  print("\nMenu de opciones:")
  print("1. Visitar una pagina")
  print("2. Retroceder a la pagina anterior")
  print("3. Mostrar pagina actual")
  print("4. Salir")

# solicitamos al usuario que ingrese una opcion
  opcion = input("Ingrese una opcion (1-4): ")
  if opcion == "1":
    url = input("Ingrese la URL de la pagina: ")
    pag(url)
  elif opcion == "2":
       retrodecer()
  elif opcion == "3":
        pagina_actual()
  elif opcion == "4":
        print("Saliendo del programa...")
        break
  else:
        print("Opcion invalida. Por favor, ingrese una opcion valida (1-4).") 
    