"""
1) For each function calc presicesly its time complexity (number of steps done by the algo)

Note: to calc the complexity I'm using the RAM model, presented in CLRS's book
    + at the end of each line is a comment with the form: ci,ti
        -> ci: constant time to execute i line
        -> ti: number of times the line i is excecuted
"""

# A)


def ex1_algo1(n):
    cnt = 0
    # we include a conunter (cnt) to compare
    # this original algo with complexity caculated
    i = 0
    cnt += 1  # c1,1
    res = 10
    cnt += 1  # c2,1
    while i < n:
        cnt += 1  # c3,n (while loop)
        j = 0
        cnt += 1  # c4,n-1
        p = 0
        cnt += 1  # c5,n-1
        while j <= n:
            cnt += 1  # c6,(n-1)(n/2+2) (while loop)
            p = p + 2
            cnt += 1  # c7,(n-1)(n/2+1)
            j = j + 2
            cnt += 1  # c8,(n-1)(n/2+1)
        cnt += 1  # (while loop exit)
        i = i + 1
        cnt += 1  # c9,n-1
        res = res + 10 * p
        cnt += 1  # c10,n-1
    cnt += 1  # (while loop exit)
    return cnt


def ex1_algo1_comp(n):
    # any ci will be calculated as 1
    l1 = 1
    l2 = 1
    l3 = n + 1
    l4 = n
    l5 = n
    l6 = (n // 2 + 2) * n
    l7 = (n // 2 + 1) * n
    l8 = (n // 2 + 1) * n
    l9 = n
    l10 = n
    return l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10


# B)


def ex1_algo2(n):
    i = n  # c1,1
    res = 20  # c2,1
    while i >= 0:  # c3,n/2+2
        j = i  # c4,n/2+1
        s = 0  # c5,n/2+1
        while j < n:
            s = s + i  # c6,sum(tj-1)
            j = j + 1  # c6,sum(tj-1)
        i = i - 2
        res = res + s


def ex1_algo2_comp(n):
    l1 = 1
    l2 = 1
    l3 = (n / 2) + 2
    l4 = n / 2 + 1
    l5 = n / 2 + 1
    l6 = n * (n / 2 + 1) - (n * (n + 2)) / 4 + (n / 2 + 1)
    l7 = n * (n / 2 + 1) - (n * (n + 2)) / 4
    l8 = n * (n / 2 + 1) - (n * (n + 2)) / 4
    l9 = n / 2 + 1
    l10 = n / 2 + 1
    return l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10


# C

"""
Note:
En el código anterior como i depende de j vamos a escribir la linea temporalmente como
$\sum_{i=1}^{n}t_{i}$(linea 6) ahora debemos analizar como se comporta $i$ vs $j$ para
distintos valores de $n$ 

Como vemos en $i$ vs $j$ la formula que obtenemos sería $t_j=i+1$ por lo que si reemplazamos
en la sumatoria por lo tanto si reemplazamos $t_j$ en la sumatoria que teníamos tenemos que:
$\sum_{i=1}^{n}(i+1)$ solo queda transformar esta sumatoria a su forma cerrada 
$\sum_{i=1}^{n}(i+1) =  n(n+3)/2$ y sumarlo con los termos de los costos de las otras lineas
para obtener el polinomio total $T(n)$
"""


def ex1_algo3(n):
    cnt = 1  # c1,1
    s = 0
    cnt += 1  # c2,1
    i = 1
    while i <= n:
        cnt += 1  # c3,n+1
        t = 0
        cnt += 1  # c4,n
        j = 1
        cnt += 1  # c5,n
        while j <= i:
            cnt += 1  # c6,n(n+3)/2
            t += 1
            cnt += 1  # c7,n(n+1)/2
            j += 1
            cnt += 1  # c8,n(n+1)/2
        cnt += 1  # while loop exit
        s += t
        cnt += 1  # c9,n
        i += 1
        cnt += 1  # c10,n
    cnt += 1  # while loop exit
    return cnt


def ex1_algo3_comp(n):
    l1 = 1
    l2 = 1
    l3 = n + 1
    l4 = n
    l5 = n
    l6 = n * (n + 3) // 2
    l7 = n * (n + 1) // 2
    l8 = n * (n + 1) // 2
    l9 = n
    l10 = n
    return l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10


"""
2) Get the invariant of each loop
"""


def ex2_algo1(n):
    def inner_invariant(j):
        return 4 * (j - 1)  # =p

    def outer_invariant(i):
        return 10 + (i - 1) * 400  # = res

    i = 1
    res = 10
    while i <= n:
        j = 1
        p = 0
        while j <= 10:
            p = p + 4
            j = j + 1
            print(f" calculada: {inner_invariant(j)}, real: {p}")
        i = i + 1
        res = res + 10 * p
        print(f" calculada: {outer_invariant(i)}, real: {res}")


# Tests, driver code
if __name__ == "__main__":
    # ===== Ex 1.

    # list with different n's to test the complexity excercises
    lst = [2, 4, 10, 20, 24, 58, 92, 150, 200, 256, 512, 1024]

    print("Ex 1, algo 1")
    for n in lst:
        # Ex 1, algo 1 works perfect :D
        print(f"Original: {ex1_algo1(n)} ; complexity calculated {ex1_algo1_comp(n)}")
    print(10 * "=")
    print("Ex 1, algo 3")
    for n in lst:
        print(f"Original: {ex1_algo3(n)} ; complexity calculated {ex1_algo3_comp(n)}")
    print(10 * "=")

    # ==== Ex 2.
    ex2_algo1(10)
