import timeit

def find_coins_greedy(sum, coins):
    coins_count = {}

    # coins = [50, 25, 10, 5, 2, 1]
    for coin in coins:
        # coin = 50
        count = sum // coin
        # count = 2
        if count > 0:
            coins_count[coin] = count  # coins_count.get(coin, count)
            sum -= coin * count
            # sum = 37, більша монета 50 не підходить, використовуємо наступну найбільшу доступну монету
    return coins_count

def find_coins_greedy_slow(sum, coins):
    coins_count = {}

    for coin in coins:
        while sum >= coin:
            sum -= coin
            coins_count[coin] = coins_count.get(coin, 0) + 1

    return coins_count

def find_coins_greedy_fast(sum, coins):
    coins_count = {}

    for coin in coins:
        count = sum // coin
        if count:
            coins_count[coin] = count
            sum %= coin
        if sum == 0:
            break

    return coins_count

if __name__ == '__main__':
    cases = [
        ([50, 25, 10, 5, 2, 1], 137),
        ([25, 10, 5, 2, 1], 543210),
    ]
    functions = [find_coins_greedy, find_coins_greedy_slow, find_coins_greedy_fast]

    for coins, cash_amount in cases:
        print(f"\nCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(cash_amount, coins), number=10)
            print("Result for {}: {}".format(fun.__name__, fun(cash_amount, coins)))
            print("Time taken for {}: {:.6f} seconds".format(fun.__name__, time))


