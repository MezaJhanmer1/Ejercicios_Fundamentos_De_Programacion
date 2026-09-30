def eliminar_repeticion(lista, eliminar_nro, cual_eliminar):     #lista, numero a eliminar, num exacto de repeticion a eliminar 
    lista_limpia = []
    contador_apariciones = 0            # Cuenta cuántas veces vemos el número
    
    for numero in lista:                #para la var numero en lista
        if numero == eliminar_nro:      
            contador_apariciones += 1   #si encontró y es igual, sumamos al contador
            
            if contador_apariciones == cual_eliminar:   # Si el contador es la repetición que queremos borrar, le damos al print
                print(f"Eliminando la aparición #{cual_eliminar} del número {eliminar_nro}")  #muestra el valor actual de las variables
                continue                                # Salta al sigte. numero del ciclo sin guardarlo
                
        lista_limpia.append(numero)     # Los num q no saltaron el continue, se guardan        
    return lista_limpia                 #retorna la lista limpia con los numeros ya borrados

notas = [85, 42, 93, 42, 67, 28, 42, 75, 42]        # Lista con 4 números 42 iguales (en los índices 1, 3, 6 y 8)
numero_rep = 42                                     #llamamos al numero repetido
resultado = eliminar_repeticion(notas, numero_rep, cual_eliminar=2)  #borra la concurrencia 2 del num repetido

print(f"\nLista original: {notas}")
print(f"Lista final:    {resultado}")









#1. Cuando el contador llega al número que elegiste (contador_apariciones == cual_eliminar), ejecuta el print.
#2. Justo después, encuentra el continue. su única misión es funcionar como un "salto". Le dice a Python: "Olvida lo que queda por 
# hacer abajo con este número actual (que es guardarlo) y pasa directo a leer el siguiente número de la lista".
#3. De esa manera, al no llegar a la línea del .append(), ese número específico nunca se guarda en la nueva lista, logrando que quede "borrado".
#4. Y como bien mencionas, el ciclo sigue leyendo y procesando los números restantes de forma normal.






