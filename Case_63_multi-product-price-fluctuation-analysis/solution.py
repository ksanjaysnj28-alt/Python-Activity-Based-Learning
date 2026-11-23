# Case Study 63: Multi-Product Price Fluctuation Analysis

products = ["Rice", "Milk", "Cooking Oil"]
prices = [
    [50, 52, 54, 53],
    [28, 29, 31, 30],
    [120, 118, 135, 150]
]
fluctuation_limit = 10
largest_change = -1
largest_product = ""
largest_period = ""

print("PRICE CHANGE REPORT")
for i in range(len(products)):
    print(products[i])
    for j in range(1, len(prices[i])):
        previous_price = prices[i][j - 1]
        current_price = prices[i][j]
        if previous_price <= 0:
            print("  Invalid previous price")
        else:
            percentage = ((current_price - previous_price) / previous_price) * 100
            absolute_change = abs(percentage)
            print("  Period", j, "to", j + 1, ":", round(percentage, 2), "%")
            if absolute_change > fluctuation_limit:
                print("    Warning: fluctuation exceeds", fluctuation_limit, "%")
            if absolute_change > largest_change:
                largest_change = absolute_change
                largest_product = products[i]
                largest_period = str(j) + " to " + str(j + 1)

print("\nLargest fluctuation:", largest_product, "during period", largest_period)
print("Absolute change:", round(largest_change, 2), "%")
