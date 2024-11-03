"""
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

import timeit

def open_file (filename):
    with open(filename, 'r') as f:
        numbers = list(map(int, f.read().split()))
    return numbers

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Method to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Method to display the linked list as a list for easy viewing
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

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



numbers = open_file('digits.txt')

linked_list = LinkedList()
for number in numbers:
    linked_list.append(number)

print("Original linked list:", linked_list.to_list())

print(f"-------------------------------------------------")
print(f"-------------------------------------------------")
print(f"-------------------------------------------------")

linked_list.reverse()
print("Reversed linked list:", linked_list.to_list())

print(f"-------------------------------------------------")
print(f"-------------------------------------------------")
print(f"-------------------------------------------------")

time_taken_merge = timeit.timeit(lambda: sort_merge(numbers), number=1)
print(f"Merge sort (time taken: {time_taken_merge:.6f} seconds): {sort_merge(numbers)}")
print(f"-------------------------------------------------")