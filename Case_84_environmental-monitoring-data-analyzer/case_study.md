# Case Study 84: Environmental Monitoring Data Analyzer

## Problem statement
Analyse nested lists of air-quality or water-quality readings, calculate averages and extremes, and classify observations using supplied threshold values.

## Objectives
1. Store monitoring readings as a nested list.
2. Calculate average, minimum, and maximum readings for each station.
3. Classify each observation using supplied thresholds.
4. Identify the station with the highest average reading.

## Assumptions
- Readings are non-negative numeric values.
- This sample uses illustrative air-quality index (AQI)-style values, not live measurements.
- For this exercise: below 50 = GOOD, 50 to 100 = MODERATE, and above 100 = HIGH.
- Each station has the same number of readings.

## Algorithm
1. Store station names and a nested list of readings.
2. For each station, initialise total, minimum, and maximum.
3. Visit each reading, update total/minimum/maximum, and classify it using thresholds.
4. Calculate and display station average and extremes.
5. Track the station with the highest average.
6. Display the station with the highest average.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET station names and nested list of readings
SET highest_average = -1
FOR each station
    SET total = 0; minimum = first reading; maximum = first reading
    FOR each reading
        ADD reading to total
        UPDATE minimum and maximum
        IF reading < 50: category = GOOD
        ELSE IF reading <= 100: category = MODERATE
        ELSE: category = HIGH
        DISPLAY reading and category
    CALCULATE average = total / number of readings
    DISPLAY average, minimum, maximum
    IF average > highest_average: update station
DISPLAY station with highest average
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal dataset | Use all station readings | Library has the highest average reading of 86.0. |
| All low readings | Set all values for a station below 50 | Every observation is classified GOOD. |
| High observation | Set one observation to 120 | That observation is classified HIGH and affects its station maximum and average. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The program analyses a nested list of environmental readings and uses loops and conditional statements to calculate statistics and classify observations. The thresholds are explicitly illustrative.
