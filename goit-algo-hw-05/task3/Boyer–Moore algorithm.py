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

def build_shift_table(pattern):
    """Create a shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)
    # For each character in the pattern, set the shift equal to the length of the pattern
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # If the character is not in the table, the shift will be equal to the length of the pattern
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    # Create a shift table for the pattern
    shift_table = build_shift_table(pattern)
    i = 0  # Initialize the starting index for the main text

    # Traverse the main text, comparing with the pattern
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Start from the end of the pattern

        # Compare characters from the end of the pattern to its beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Move towards the beginning of the pattern

        # If the entire pattern matches, return its position in the text
        if j < 0:
            print(f"Pattern found at index {i}")
            return i  # Pattern found

        # Shift the index i based on the shift table
        # This allows "jumping" over non-matching parts of the text
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # If the pattern is not found, return -1
    print("Pattern not found")
    return -1


text1 = open_file('стаття 1.txt')
text2 = open_file('стаття 2.txt')

pattern = "Зв’язний список (linked list) – це структура даних, у якій кожен елемент має вказівник на наступний елемент."
build_shift_table(pattern)

time_taken_boyer_moore_text1 = timeit.timeit(lambda: (boyer_moore_search(text1, pattern)), number=1)
print(f"Time taken for Boyer-Moore algorithm: {time_taken_boyer_moore_text1:.6f} seconds)")

print(f"-------------------------------------------------")

time_taken_boyer_moore_text2 = timeit.timeit(lambda: (boyer_moore_search(text2, pattern)), number=1)
print(f"Time taken for Boyer-Moore algorithm: {time_taken_boyer_moore_text2:.6f} seconds)")


