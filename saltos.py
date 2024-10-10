def saltos (arr):
    indice = 0
    while indice < len(arr):
        salto = arr[indice]
        if salto == 0:
            return False
        indice += salto
        
    return indice >= len(arr) 



        
        


    
