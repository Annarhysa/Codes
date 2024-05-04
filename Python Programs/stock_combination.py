import sys
def find_stock_combinations(target_price, num_stocks, stocks):
    valid_combinations = []
    
    # Generate all combinations of quantities for each stock
    for i in range(stocks[0][1] + 1):
        for j in range(stocks[1][1] + 1):
            if num_stocks == 3:
                for k in range(stocks[2][1] + 1):
                    total_price = i * stocks[0][1] + j * stocks[1][1] + k * stocks[2][1]
                    if total_price == target_price:
                        valid_combinations.append([i, j, k])
            elif num_stocks == 2:
                total_price = i * stocks[0][1] + j * stocks[1][1]
                if total_price == target_price:
                    valid_combinations.append([i, j])
    
    # Print valid combinations
    for combination in valid_combinations:
        for i, stock in enumerate(stocks):
            print(stock[0] + ":", combination[i], end=" ")
        print()
    
    return len(valid_combinations)

# Input
try:
    target_price = int(input())
    num_stocks = int(input())
    
    stocks = []
    for i in range(num_stocks):
        stock_name, stock_price = input().split()
        stock_price = int(stock_price)
        if stock_price <= 0:
            print("The stock prices should be at least greater than 0")
            sys.exit()
        if stock_price > target_price:
            print("One of the stock price is higher than the target price")
            sys.exit()
        stocks.append((stock_name, stock_price))
except ValueError:
    print("Invalid Input")
    sys.exit()

# Find and print stock combinations
total_combinations = find_stock_combinations(target_price, num_stocks, stocks)
print(total_combinations)