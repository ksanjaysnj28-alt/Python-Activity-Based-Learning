# Case Study 53: Food Waste Monitoring System

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
prepared = [200, 180, 220, 160, 200]
served = [180, 165, 187, 152, 170]
acceptable_limit = 15

highest_percentage = -1
highest_day = ""
print("DAILY FOOD WASTE REPORT")

for i in range(len(days)):
    if prepared[i] <= 0 or served[i] < 0 or served[i] > prepared[i]:
        print(days[i], "Invalid meal-count data")
    else:
        leftovers = prepared[i] - served[i]
        percentage = (leftovers / prepared[i]) * 100
        print(days[i], "Prepared:", prepared[i], "Served:", served[i], "Leftovers:", leftovers, "Wastage:", round(percentage, 2), "%")
        if percentage > acceptable_limit:
            print("  Warning: wastage exceeds", acceptable_limit, "%")
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_day = days[i]

print("\nHighest wastage:", highest_day, "-", round(highest_percentage, 2), "%")
