def coin_change(coins, amount):

    # dp[i] = minimum number of coins needed
    # to make amount i
    dp = [float('inf')] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    # Calculate minimum coins for every amount
    for i in range(1, amount + 1):

        for coin in coins:

            if coin <= i:
                dp[i] = min(
                    dp[i],
                    1 + dp[i - coin]
                )

    return dp[amount]


# Input
coins = list(map(int, input("Enter coin values: ").split()))
amount = int(input("Enter amount: "))

result = coin_change(coins, amount)

if result == float('inf'):
    print("Amount cannot be made using given coins")
else:
    print("Minimum number of coins:", result)