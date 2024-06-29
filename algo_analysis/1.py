"""
1) For each function calc presicesly its computational complexity
"""

# A)


def ex1_algo1(n):
    i = 0
    res = 10
    while i < n:  # n+1
        j = 0
        p = 0
        while j <= n:  # 0 62 => 61
            p = p + 2
            j = j + 2
            i = i + 1  # l9
            res = res + 10 * p


def ex1_algo1_comp(n):
    l1 = 1
    l2 = 1
    l3 = n + 1
    l4 = n
    l5 = n
    l6 = (n / 2 + 2) * n
    l7 = (n / 2 + 1) * n
    l8 = (n / 2 + 1) * n
    l9 = n
    l10 = n
    return l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10


# B)


def ex1_algo2(n):
    i = n
    cnt = 1
    res = 20
    cnt += 1
    cnt += 1  # declaracion falsa cabecera del while
    while i >= 0:
        cnt += 1  # cabecera del while
        j = i
        cnt += 1
        s = 0
        cnt += 1
        cnt += 1  # declaracion falsa cabecera del while
        while j < n:
            cnt += 1  # cabecera del while
            s = s + i
            cnt += 1
            j = j + 1
            cnt += 1
        i = i - 2
        cnt += 1
        res = res + s
        cnt += 1
    return cnt


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
# -> suppose len(mat) = len(mat2) = n
def ex1_algo3(n):
    cnt = 0
    i = 1
    cnt += 1
    while i <= n:
        cnt += 1  # start while
        j = 1
        cnt += 1
        while j <= n:
            cnt += 1  # start inner while
            # 5-line
            cnt += 1
            j = j + 1
            cnt += 1
        cnt += 1  # end inner while
        i += 1
    cnt += 1  # end outer while
    return cnt


"""
2) Get the invariant of each loop
"""


def programa3(n):
    i = 1
    res = 10
    while i <= n:
        j = 1
        p = 0
        while j <= 10:
            p = p + 4
            j = j + 1
        # print(f" calculada: {invariante_interna(j)}, real: {p}")
        i = i + 1
        res = res + 10 * p
    print(f" calculada: {invariante_externa(i)}, real: {res}")


def invariante_interna(j):
    return 4 * (j - 1)  # =p


def invariante_externa(i):
    return 10 + (i - 1) * 400


programa3(100)

if __name__ == "__main__":
    """
    def proof(func1,func2):
    lst=[2,4,10,20,24,58,92,150,200,256,512,1024]
    for i in lst:
        print(func1(i),func2(i))
    """
    # proof(programa2,comp_p2)
