# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j):
    """Échange la place de deux éléments dans un tableau"""
    tab[i], tab[j] = tab[j], tab[i]
    return tab


# ---------------
# Tris classiques
# ---------------
def bubble(A):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""
    n=len(A)
    for i in range(n, 1, -1):
        for j in range(0, i-1):
            if A[j+1] < A[j]:
                swap(A, j+1, j)
    return A


def insertion(A):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    n = len(A)


    for i in range(1, n):
        x = A[i]
        j = i
        while j > 0 and A[j - 1] > x:
            A[j] = A[j - 1]
            j = j - 1
            A[j] = x
    return A


def selection(A):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    n = len(A)
    for i in range(0, n):
        min = i
        for j in range (i+1, n):
            if A[j] < A[min]:
                min = j
        if min != i:
            swap(A, i, min)
    return A


# --------------
# Tris récursifs
# --------------
def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""

    merge_sort_r(tab, 0, len(tab))

def merge_sort_r(tab, d, f):
    if d < f-1:
        m= int((d+f)/2)
        merge_sort_r(tab, d, m)
        merge_sort_r(tab, m, f)
        merge(tab, d, m, f)
    
def merge(tab, d, m, f):
    i = int(d)
    j = int(m)
    temp = [0] * int(len(tab))
    for k in range(d, f):
        if i < m and j < f:
            if tab[i] <= tab[j]:
                temp[k] = tab[i]
                i = i+1
            else:
                temp[k] = tab[j]
                j = j+1
        else:
            if i < m:
                temp[k] = tab[i]
                i = i+1
            else:
                temp[k] = tab[j]
                j = j+1
    for k in range(d, f):
        tab[k] = temp[k]


def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""
    tri_rapide_r(tab, 0, len(tab)-1)

def tri_rapide_r(tab, premier, dernier):
    if premier < dernier:
        pivot = partition(tab, premier, dernier)
        tri_rapide_r(tab, premier, pivot-1)
        tri_rapide_r(tab, pivot+1, dernier)
    
def partition(tab, premier, dernier):
    pivot = tab[premier]
    i = int(premier)
    j = int(dernier)
    while i <= j:
        if tab[i] <= pivot:
            i = i+1
        else:
            if tab[j] > pivot:
                j = j-1
            else:
                swap(tab, i, j)
        
    tab[premier], tab[j] = tab[j], tab[premier]
    return j
