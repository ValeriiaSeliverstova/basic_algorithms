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

def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Базове число для хешування та модуль
    base = 256 
    modulus = 101  
    
    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                print("Substring found")
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    print("Substring not found")
    return -1



text1 = open_file('стаття 1.txt')
text2 = open_file('стаття 2.txt')

pattern = "Зв’язний список (linked list) – це структура даних, у якій кожен елемент має вказівник на наступний елемент."

polynomial_hash(pattern)

time_taken_rabin_karp_text1 = timeit.timeit(lambda: (rabin_karp_search(text1, pattern)), number=1)
print(f"Time taken for Rabin-Karp algorithm: {time_taken_rabin_karp_text1:.6f} seconds)")

print(f"-------------------------------------------------")

time_taken_rabin_karp_text2 = timeit.timeit(lambda: (rabin_karp_search(text2, pattern)), number=1)
print(f"Time taken for Rabin-Karp algorithm: {time_taken_rabin_karp_text2:.6f} seconds)")
