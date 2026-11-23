# Case Study 53: Food Waste Monitoring System

## Problem statement
Compare prepared meals, meals served, and leftovers across several days; calculate wastage percentages and identify days exceeding acceptable limits.

## Objectives
1. Store daily meal counts in lists.
2. Calculate leftovers and wastage percentage for each day.
3. Compare wastage with the acceptable threshold.
4. Identify the day with the highest wastage percentage.

## Assumptions
- Prepared meals are greater than zero.
- Meals served cannot exceed meals prepared.
- Leftovers are calculated as prepared minus served.
- A wastage percentage above 15% is considered excessive in this sample.

## Algorithm
1. Store day names, meals prepared, and meals served.
2. For each day, calculate leftovers.
3. Calculate wastage percentage as leftovers divided by meals prepared multiplied by 100.
4. Display daily values.
5. Flag any day above the acceptable threshold.
6. Track and display the day with the highest percentage.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET days, prepared list, served list, and wastage limit
SET highest_percentage = -1
FOR each day index
    leftovers = prepared - served
    percentage = leftovers / prepared * 100
    DISPLAY day, leftovers, percentage
    IF percentage > limit: report excessive wastage
    IF percentage > highest_percentage: update highest day
DISPLAY highest-wastage day
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal week | Use the supplied prepared and served counts | Wednesday and Friday tie at 15%; Wednesday is retained as the first maximum. |
| No leftovers | Set served equal to prepared for one day | That day reports 0% wastage. |
| Invalid served count | Set served greater than prepared | The day is reported as invalid instead of calculating a negative leftover. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The program compares prepared and served meal counts, calculates food waste percentages, and highlights days above the acceptable limit. Input validation prevents impossible negative leftovers.
