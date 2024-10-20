import timeit
from pathlib import Path

def open_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='windows-1251') as f:  # Спроба відкрити файл в іншому кодуванні
            text = f.read()
    return text

def compute_lps(pattern):
    """
    Функція для пошуку алгоритмом Кнута-Морріса-Пратта

    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            print(f"Pattern found at index {i - j}")
            return i - j 
    print("Pattern not found")
    return -1  # якщо підрядок не знайдено



text1 = open_file('стаття 1.txt')
text2 = open_file('стаття 2.txt')

pattern = "Зв’язний список (linked list) – це структура даних, у якій кожен елемент має вказівник на наступний елемент."

time_taken_kmp_text1 = timeit.timeit(lambda: (kmp_search(text1, pattern)), number=1)
print(f"Time taken for Knuth-Morris-Pratt algorithm: {time_taken_kmp_text1:.6f} seconds)")

print(f"-------------------------------------------------")

time_taken_kmp_text2 = timeit.timeit(lambda: (kmp_search(text2, pattern)), number=1)
print(f"Time taken for Knuth-Morris-Pratt algorithm: {time_taken_kmp_text2:.6f} seconds)")
