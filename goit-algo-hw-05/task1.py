class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][i]
                    return True
        return False

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.insert("plum", 40)
H.insert("kiwi", 50)
H.insert("grape", 60)
H.insert("peach", 70)
H.insert("pear", 80)
H.insert("cherry", 90)
H.insert("strawberry", 100)

print(H.get("grape"))   # Виведе: 60
print(H.get("kiwi"))  # Виведе: 50
print(H.get("plum"))  # Виведе: 40

H.delete("apple")
H.delete("orange")
H.delete("banana")
print(H.get("apple"))   # Виведе: None
print(H.get("orange"))  # Виведе: None
print(H.get("banana"))  # Виведе: None



