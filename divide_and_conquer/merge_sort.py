def merge_sort(lst):
    #caso base: el subarray es solo de un elemento, o es vacio
    if len(lst)<=1:
        return lst
    #caso recursivo
    else:
        #Dividir
        mid = len(lst)//2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])

        #Combinar
        return merge(left,right)

def merge(left,right):
    """
    Combinar los subarreglos que ya se encuentran ordenados

    Args:
        left: subarray izquierdo
        right: subarray derecho
    """

    result = []
    i=0 #indice para el subarray de la izquierda
    j=0 #indice para el sub array de la derecha
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    #Si aún quedan elementos en el subarray de la izquierda
    while i < len(left):
        result.append(left[i])
        i+=1

    #Si aún quedan elementos en el subarray de la izquierda
    while j < len(right):
        result.append(right[j])
        j+=1

    #regresa la lista ya combinada y ordenada
    return result


if "__main__" == __name__:
    arr = [12, 11, 13, 5, 6]
    print(arr)
    print(merge_sort(arr))