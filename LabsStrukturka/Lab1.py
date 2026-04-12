import time
import tracemalloc
import random


# 1 Проверка наличия элемента в массиве
def proverka_elementa(arr, target):
    for element in arr:
        if element == target:
            return True
    return False


# 2 Поиск второго максимального элемента
def poisk_vtorogo_max_element(arr):
    if len(arr) < 2:
        return None

    max1 = arr[0]
    max2 = arr[0]

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max2


# 3 Бинарный поиск
def binary_poisk(arr, target):
    sorted_arr = sorted(arr)
    left = 0
    right = len(sorted_arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_arr[mid] == target:
            return True
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# 4 Построение таблицы умножения
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

# Доп Сортировка выбором
def Selection_sort(massiv):
    massiv = massiv.copy()
    n = len(massiv)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if massiv[j] < massiv[min_index]:
                min_index = j
        massiv[i], massiv[min_index] = massiv[min_index], massiv[i]
    return massiv

# Функция для измерения времени
def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


# Функция для измерения времени и памяти
def measure_time_memory(func, *args):
    tracemalloc.start()
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end - start, peak / 1024


# Генерация случайного массива
def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 1000))
    return arr


sizes = [100, 1000, 10000]

print("1 Проверка наличия элемента")
for size in sizes:
    test_arr = generate_array(size)
    time_taken, memory_kb = measure_time_memory(proverka_elementa, test_arr, -1)
    print(f"Размер {size}: {time_taken:.8f} сек, память: {memory_kb:.2f} КБ")


print("\n2 Поиск второго максимального элемента")
for size in sizes:
    test_arr = generate_array(size)
    time_taken, memory_kb = measure_time_memory(poisk_vtorogo_max_element, test_arr)
    print(f"Размер {size}: {time_taken:.8f} сек, память: {memory_kb:.2f} КБ")


print("\n3 Бинарный поиск")

for size in sizes:
    test_arr = generate_array(size)
    time_taken, memory_kb = measure_time_memory(binary_poisk, test_arr, test_arr[0])
    print(f"Размер {size}: {time_taken:.8f} сек, память: {memory_kb:.2f} КБ")

print("\n4 таблица умножения")
table_sizes = [10, 50, 100]
for size in table_sizes:
    time_taken, memory_kb = measure_time_memory(multiplication_table, size)
    print(f"Размер {size}×{size}: {time_taken:.8f} сек, память: {memory_kb:.2f} КБ")


print("\n5. Сортировка выбором")
for size in sizes:
    test_massiv = generate_array(size)
    execution_time, memory_kb = measure_time_memory(Selection_sort, test_massiv)
    print(f"Размер {size}: {execution_time:.8f} сек, память: {memory_kb:.2f} КБ")