coins = [1, 2, 4, 5, 9, 69, 420]

# minimum number of coins needed to make n cents
# dynamic programming

def min_coins(n):
    table = [0] + [10000] * n
    for i in range(1, n + 1):
        for j in coins:
            if i >= j and table[i - j] + 1 < table[i]:
                table[i] = table[i - j] + 1
    return table[n]