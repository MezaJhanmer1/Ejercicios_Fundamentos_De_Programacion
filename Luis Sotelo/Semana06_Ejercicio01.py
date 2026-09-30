#Lista de Notas, ordenar con bubble soart , selection soart y encontrar la nota max, min y prom

def bubble_sort(lista):
    n = len(lista) # n = total de elementos
    for i in range(n): 			 # i = pasada actual (0 a n-1)
        intercambiado = False 		 # detectar lista ya ordenada
        for j in range(0, n-i-1): 	 # j recorre hasta el último no colocado
            if lista[j] > lista[j+1]:	 
					 # Si sí, se intercambian
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True	 # hubo al menos 1 cambio
        if not intercambiado:		 # si no hubo cambios → lista ordenada
            break 			 # salir antes

datos = [85, 42, 93, 67, 28, 75]
bubble_sort(datos)
print(f'Ordenamiento por Burbuja: {datos}')

def selection_sort(lista):
    n = len(lista) 				# cantidadde elementos
    for i in range(n -1): 			# i= inicio sublista sin ordenar
    						
        idx_min= i				# guarda índice del mínimo actual
        for j in range(i+ 1, n): 		# buscarmínimoenelresto
            if lista[j] > lista[idx_min]:       
                idx_min= j		 	# actualizo el índice del mínimo

        if idx_min!= i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i] # swap

datos = [85, 42, 93, 67, 28, 75]
selection_sort(datos)
print(f'Ordenamiento por Seleccion: {datos}')

def mostrar_notas(lista):
    nota_min = min(lista)
    nota_max = max(lista)
    prom = sum(lista) / len(lista)
    
    print(f"Nota mínima: {nota_min}")
    print(f"Nota máxima: {nota_max}")
    print(f"Promedio de notas: {prom:.2f}")

mostrar_notas(datos)