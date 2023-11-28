"""
Diseñe un algoritmo bajo la estrategia divide y venceras para encontrar la moda de un vector. La
moda de un vector es el elemento que mas se repite, si existe mas de una moda, el algoritmo retornar´a
todos los elementos que son moda. Ejemplo
(1,2,2,3,4) La moda es 2
(1,2,2,3,3,5) La moda es 2 y 3
"""

def dac_mode(lst):
    dictionary = {}
    if not lst:
        return None
    else:
        return dac_mode_aux(0,len(lst)-1,lst,dictionary)
    
def dac_mode_aux(i,l,lst,dictionary):
    #caso base: combinar
    if i==l:
        if lst[i] in dictionary:
            dictionary[lst[i]] += 1
        else:
            dictionary[lst[i]] = 1
    #sino dividir
    else:
        mid=(i+l)//2
        dac_mode_aux(i,mid,lst) #mitad izquierda
        dac_mode_aux(i,mid+1,lst) #mitad derecha

    """
    public static void main(String[] args) {
    int[] repetitive = { 5, 12, 5, 17, 12, 12, 5, 39 };
    System.out.println(countOccurences(repetitive));
}

public static Map<Integer, Integer> countOccurences(int[] arr) {
    if (arr.length == 1) {
        Map<Integer, Integer> result = new HashMap<>();
        result.put(arr[0], 1);
        return result;
    } else {

        int to = arr.length / 2;
        Arrays.copyOfRange(arr, 0, to);

        Map<Integer, Integer> left = countOccurences(Arrays.copyOfRange(arr, 0, to));
        Map<Integer, Integer> right = countOccurences(Arrays.copyOfRange(arr, to, arr.length));
        return merge(left, right);
    }
}

static Map<Integer, Integer> merge(Map<Integer, Integer> left, Map<Integer, Integer> right) {
    right.forEach((number, count) -> {
        left.compute(number, (num, c) -> c == null ? count : c + count);
    });
    return left;
}
    """