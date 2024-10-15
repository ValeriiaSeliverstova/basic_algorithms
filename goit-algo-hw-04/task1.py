import timeit

def open_file (filename):
    with open(filename, 'r') as f:
        numbers = list(map(int, f.read().split()))
    return numbers

def sort_merge(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(sort_merge(left_half), sort_merge(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def sort_insertion(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst



def sort_tim(lst):
    return sorted(lst)
    

numbers = open_file('digits.txt')


time_taken_merge = timeit.timeit(lambda: sort_merge(numbers), number=1)
print(f"Merge sort (time taken: {time_taken_merge:.6f} seconds): {sort_merge(numbers)}")
print(f"-------------------------------------------------")

time_taken_insertion = timeit.timeit(lambda: sort_insertion(numbers), number=1)
print(f"Insertion sort (time taken: {time_taken_insertion:.6f} seconds): {sort_insertion(numbers)}")
print(f"-------------------------------------------------")

time_taken_tim = timeit.timeit(lambda: sort_tim(numbers), number=1)
print(f"Tim sort (time taken: {time_taken_tim:.6f} seconds): {sort_tim(numbers)}")


"""
У результатах вимірювання часу виконання трьох різних алгоритмів сортування отримано наступні дані:

Сортування злиттям: 0.000129 секунд
Сортування вставками: 0.000149 секунд
Timsort (вбудований алгоритм у Python): 0.000002 секунд
Ці результати показують, що алгоритм Timsort значно перевершує обидва інші алгоритми за швидкістю. Поєднання сортування злиттям і сортування вставками робить Timsort дуже ефективним для реальних сценаріїв.
"""

