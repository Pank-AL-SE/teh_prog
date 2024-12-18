def find_min_element(arr): #3, 17, 6, 26, 16
    min_value = float('inf')
    min_index = -1

    for i in range(len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i

    return min_value, min_index
def bubble_sort(arr): #1, 13, 6, 31, 26
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def binary_search(arr, target): #3, 18, 9, 34, 28
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
def find_min_element_2d(arr): #4, 18, 8, 43, 27
    min_value = float('inf')
    min_row, min_col = -1, -1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < min_value:
                min_value = arr[i][j]
                min_row, min_col = i, j

    return min_value, min_row, min_col
def reverse_array(arr): #1, 5, 2, 6, 3
    arr.reverse()
def left_rotate(arr, d): #2, 9, 4, 14, 13
    n = len(arr)
    d = d % n
    arr[:] = arr[d:] + arr[:d]
def replace_value(arr, old_value, new_value): #3, 12, 5, 16, 12
    for i in range(len(arr)):
        if arr[i] == old_value:
            arr[i] = new_value
import math

def find_some(nD, n1, n2, N1, N2):
    S = 11

    n = n1 + n2
    N = N1 + N2

    ngal = n1 * math.log2(n1) + n2 * math.log2(n2)
    vD = (2 + nD) * math.log2(2 + nD)
    v = N * math.log2(n)
    L = vD / v
    lgal = (2 / n1) * (n2 / N2)
    I = (2 / n1) * (2 / N2) * (N1 + N2) * math.log2(n1 + n2)
    tgal1 = (v * v) / (S * vD)
    tgal2 = (n1 * N2 * (n1 * math.log(n1) * n2 * math.log2(n2)) * math.log2(n)) / (2 * S * n2)
    tgal3 = (n1 * N2 * N * math.log2(n)) / (2 * S * n2)
    pusto1 = lgal * lgal * v
    pusto2 = (vD * vD) / v

    print(f"nD: {nD}")
    print(f"n1: {n1}")
    print(f"n2: {n2}")
    print(f"n: {n}")
    print(f"N1: {N1}")
    print(f"N2: {N2}")
    print(f"N: {N}")
    print(f"ngal: {round(ngal, 7)}")
    print(f"vD: {round(vD, 7)}")
    print(f"v: {round(v, 7)}")
    print(f"L: {round(L, 7)}")
    print(f"lgal: {round(lgal, 7)}")
    print(f"I: {round(I, 7)}")
    print(f"tgal1: {round(tgal1, 7)}")
    print(f"tgal2: {round(tgal2, 7)}")
    print(f"tgal3: {round(tgal3, 7)}")
    print(f"pusto1: {round(pusto1, 7)}")
    print(f"pusto2: {round(pusto2, 7)}")
find_some(3, 17, 6, 26, 16) #наименьший элемент + индекс
find_some(1, 13, 6, 31, 26) #сортировка пузырьком
find_some(3, 18, 9, 34, 28) #бинарный поиск
find_some(4, 18, 8, 43, 27) #минимальынй элемент матрицы
find_some(1, 5, 2, 6, 3) #развернуть массив
find_some(2, 9, 4, 14, 13) #лефт ротате
find_some(3, 12, 5, 16, 12) #заменить значение в массиве

###
#Для 13ой лабы
###

# find_some(10, 26,35,215,112) #python
# print("\n--------------------------------\n")
# find_some(11, 33, 34, 291, 101) #c++
