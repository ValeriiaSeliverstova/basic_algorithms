import random
import matplotlib.pyplot as plt


num_rolls = 100  # Кількість кидків

# Ініціалізуємо підрахунок сум від 2 до 12
sums_count = {i: 0 for i in range(2, 13)}

# Кидаємо кубики num_rolls разів
for _ in range(num_rolls):
    roll_sum = random.randint(1, 6) + random.randint(1, 6)
    sums_count[roll_sum] += 1

simulated_probabilities = {sum_val: count / num_rolls for sum_val, count in sums_count.items()}

# Теоретичні ймовірності для порівняння
theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Виведення результатів
print("Сума | Симульована ймовірність | Теоретична ймовірність")
print("-------------------------------------------------------")
for sum_val in range(2, 13):
    sim_prob = simulated_probabilities[sum_val]
    theo_prob = theoretical_probabilities[sum_val]
    print(f"  {sum_val}  |     {sim_prob:.4f}            |     {theo_prob:.4f}")

