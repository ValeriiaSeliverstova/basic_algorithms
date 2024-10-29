import heapq

def min_cost_connect_cable(cable_lengths):
    """
    Функція приймає список довжин кабелів `cable_lengths` і повертає мінімальну вартість
    """
    heapq.heapify(cable_lengths) # Перетворюємо список `cable_lengths` в купу
    total_cost = 0

    while len(cable_lengths) > 1: #поки кількість кабелів більше 1
        # Вибираємо два найменших кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        cost = first + second  #ініціалізуємо `cost` як суму двох кабелів
        total_cost += cost #додаємо `cost` до загальної вартості
        heapq.heappush(cable_lengths, cost) #додаємо `cost` до купи

    return total_cost

if __name__ == "__main__":
    cable_lengths = [67, 8, 4, 6, 12, 89, 24, 37]
    print("Мінімальна затрати кабелів:", min_cost_connect_cable(cable_lengths)) 