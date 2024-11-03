# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if budget >= info["cost"]:
            selected_items.append(item)
            total_calories += info["calories"]
            budget -= info["cost"]

    return selected_items, total_calories

# Динамічне програмування
def dynamic_programming(items, budget):
    # Створюємо таблицю для збереження максимальних калорій для різних бюджетів
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    item_list = list(items.items())

    for i in range(1, n + 1):
        item_name, item_info = item_list[i - 1]
        cost = item_info["cost"]
        calories = item_info["calories"]

        for j in range(budget + 1):
            if cost <= j:
                # Максимум калорій при включенні або виключенні поточного предмета
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    # Визначення обраних страв для досягнення максимальних калорій
    total_calories = dp[n][budget]
    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, _ = item_list[i - 1]
            selected_items.append(item_name)
            j -= items[item_name]["cost"]

    return selected_items, total_calories

# Тестування обох функцій
budget = 250

# Використання жадібного алгоритму
greedy_items, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_items)
print("Загальна калорійність:", greedy_calories)

# Використання динамічного програмування
dp_items, dp_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Обрані страви:", dp_items)
print("Загальна калорійність:", dp_calories)
