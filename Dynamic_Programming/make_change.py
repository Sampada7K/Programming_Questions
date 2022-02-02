def make_change(change, coin_list):
    min_coins = [i for i in range(change+1)]
    coins_used = [1] * (change+1)
    for value in range(change+1):
        valid_coin_list = [coin for coin in coin_list if coin <= value]
        for coin in valid_coin_list:
            new_coin = coin
            if value == coin:
                coins_required = 1
            else:
                coins_required = min(min_coins[value], 1+min_coins[value-coin])

            if coins_required < min_coins[value]:
                min_coins[value] = coins_required
                coins_used[value] = new_coin

    return min_coins[change], coins_used


clist = [1,5,10,21,25]
amnt = 17

coins, last_coin_used = make_change(amnt, clist)

list_coins_used = []

while amnt > 0:
    list_coins_used.append(last_coin_used[amnt])
    amnt -= last_coin_used[amnt]

print(f"num coins to make change is {coins}")
print(f"coins used to make change are {list_coins_used}")


