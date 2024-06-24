import random

"""
Example: 
To find the max element and min element element in a given array.

Time Complexity:
Is given by the recurrence
a=2, b=2, C(n) = O(1), D(n) = O(1). Then T(n)=2T(n/2)+O(1)

Space Complexity:
"""


def dac_minimax_elm(lst: list[int]) -> tuple[int, int]:
    # if lst is empty
    if not lst:
        return None
    else:
        return dac_minimax_elm_aux(0, len(lst) - 1, lst)


# recursive func
def dac_minimax_elm_aux(i: int, l: int, lst: list[int]) -> (int, int):
    """
    Args:
        i: index of the start of the sub-array
        l: index of the end of the sub-array
    """

    # base case: if the list has only one element,
    # both l and i indexes are has the same value
    # para n==1
    if i == l:
        return (lst[i], lst[i])
    # para n==2
    elif 0 == l - i:
        return (lst[i], lst[l]) if lst[i] < lst[i] else (lst[i], lst[l])
    # Si el subarreglo tiene más de dos elementos,
    # la función se divide en dos mitades y se llama a
    # sí misma recursivamente para encontrar el elemento|
    # máximo de cada mitad. Luego, la función devuelve el
    # máximo de los dos elementos máximos.
    else:
        # divide in halfs the array
        mid = (i + l) // 2
        lmin, lmax = dac_minimax_elm_aux(i, mid, lst)
        rmin, rmax = dac_minimax_elm_aux(mid + 1, l, lst)

        max = lmax if lmax > rmax else rmax
        min = lmin if lmin < rmin else rmin
        return (min, max)


# tests
if __name__ == "__main__":

    def randlist():
        randomlist = []
        for _ in range(0, 20):
            i = random.randint(-100, 100)
            randomlist.append(i)
        return randomlist

    # arr=[70, 250, 50, 80, 140, 12, 14 ]
    # arr=[1,4,1,44,52,3,11,32,555,100,1231,1,0,-1,-5,7]
    n = 0
    while n <= 5:
        lst = randlist()
        print("Lista:")
        print(lst)
        print("Resultados")
        print(dac_minimax_elm(lst))
        n += 1
