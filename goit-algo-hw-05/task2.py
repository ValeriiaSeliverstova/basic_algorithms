def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None
 
    while low <= high:
        iterations += 1  # лічильник ітерацій
        mid = (high + low) // 2

        #якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        #якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]  #оновлюємо верхню межу (найменший більший елемент)

        # x присутній на позиції
        else:
            upper_bound = arr[mid]  #якщо знайдено елемент, він є верхньою межею
            return (iterations, upper_bound)

    #якщо елемент не знайдено, повертаємо кількість ітерацій і найменший елемент, більший або рівний x
    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]
    
    return (iterations, upper_bound)

# Приклад використання:
arr = [1.2, 2.5, 3.8, 4.1, 5.6, 7.3, 8.9, 10.0]
x = 5.9
result = binary_search(arr, x)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")