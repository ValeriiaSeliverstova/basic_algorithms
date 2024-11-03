import timeit

def find_min_coins(sum, coins):
    # Створюємо масив для зберігання мінімальної кількості монет для кожної суми від 0 до `sum`
    min_coins_required = [float('inf')] * (sum + 1)
    min_coins_required[0] = 0  # Для суми 0 потрібно 0 монет

    # Заповнюємо масив мінімальної кількості монет
    for i in range(1, sum + 1):  # i = можливі суми з монетами (1, 2, 3, ..., sum)
        for coin in coins:  # coin = монети
            if i >= coin:  # Якщо ми можемо використати монету для досягнення суми
                min_coins_required[i] = min(min_coins_required[i], min_coins_required[i - coin] + 1)

    # Якщо значення для `sum` залишилося inf, це означає, що неможливо досягти суми з доступними монетами
    if min_coins_required[sum] == float('inf'):
        return -1  # Повертаємо -1, якщо неможливо досягти заданої суми

    return min_coins_required[sum]  # Повертаємо мінімальну кількість монет для заданої суми

# Приклад використання
coins = [50, 25, 10, 5, 2, 1]
sum = 137
print(find_min_coins(sum, coins))  # Повинно повернути мінімальну кількість монет для суми 137

if __name__ == '__main__':
    cases = [
        ([50, 25, 10, 5, 2, 1], 137),
        ([25, 10, 5, 2, 1], 543210),
    ]
    functions = [find_min_coins]

    for coins, cash_amount in cases:
        print(f"\nCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(cash_amount, coins), number=10)
            print("Result for {}: {}".format(fun.__name__, fun(cash_amount, coins)))
            print("Time taken for {}: {:.6f} seconds".format(fun.__name__, time))
