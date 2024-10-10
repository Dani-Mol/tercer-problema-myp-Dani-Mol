def saltos (arr):
    indice = 0
    while indice < len(arr): 
        # Cuando el indice se salga del rango o si no es posible avanzar mas termina el ciclo.
        salto = arr[indice]
        if salto == 0: 
        # Falso para no quedar atrapado en el mismo lugar (por no poder avanzar)
            return False
        indice += salto
        
    return indice >= len(arr) 
    # Retorna True si el indice es mayor o igual y False si la condicion while no se cumple



        
        


    
