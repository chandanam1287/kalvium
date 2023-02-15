def calculate_min_coins(coins_list, amount_value):
    
    coins_list = sorted(coins_list, reverse=True)

    
    result_list = [0] * len(coins_list)

    
    for i in range(len(coins_list)):
        
        max_coins = amount_value // coins_list[i]

        
        result_list[i] = max_coins

        
        amount_value -= max_coins * coins_list[i]

    return result_list

coins_input = input("Enter the coin denominations (separated by commas): ")
coins_list = list(map(int, coins_input.split(",")))
amount_value = int(input("Enter the amount of change to be made: "))


result_list = calculate_min_coins(coins_list, amount_value)


print("Minimum number of coins required:", result_list)
