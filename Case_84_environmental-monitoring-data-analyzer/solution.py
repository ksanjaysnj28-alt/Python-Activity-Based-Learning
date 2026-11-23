# Case Study 84: Environmental Monitoring Data Analyzer
# Values are illustrative AQI-style readings, not live environmental data.

stations = ["Campus Gate", "Library", "Sports Ground"]
readings = [
    [42, 55, 48, 61],
    [78, 83, 95, 88],
    [35, 44, 39, 47]
]

highest_average = -1
highest_station = ""
print("ENVIRONMENTAL MONITORING REPORT")

for i in range(len(stations)):
    total = 0
    minimum = readings[i][0]
    maximum = readings[i][0]
    print(stations[i])

    for j in range(len(readings[i])):
        value = readings[i][j]
        total = total + value
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

        if value < 50:
            category = "GOOD"
        elif value <= 100:
            category = "MODERATE"
        else:
            category = "HIGH"
        print("  Reading", j + 1, ":", value, "-", category)

    average = total / len(readings[i])
    print("  Average:", round(average, 2), "Minimum:", minimum, "Maximum:", maximum)
    if average > highest_average:
        highest_average = average
        highest_station = stations[i]

print("\nHighest average reading:", highest_station, "-", round(highest_average, 2))
