"""
1. recorrer la lista de izq a der
2. compara cada item (current) con los de su izquierda
3. mientras que current sea menor a los de su izquierda, corre aquellos valores
    mayores un item a la derecha, para cuando los que queden en la izquierda no sean
    mayores que current
4. en el espacio que queda "libre" se inserta el item current
"""

def insertion_sort(lst):
    print(lst)
    n=len(lst)-1
    i=1
    while i<=n:
        current=lst[i]
        j=i-1 #indice del elemento anterior a current

        while j>=0 and current<lst[j]:
            #then swap
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=current
        i+=1
    print(lst)
    return lst

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
