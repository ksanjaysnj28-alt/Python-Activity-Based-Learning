# Case Study 63: Multi-Product Price Fluctuation Analysis

## Problem statement
Process historical product prices stored in lists, calculate percentage changes, identify maximum fluctuations, and flag products exceeding a supplied threshold.

## Objectives
1. Store historical prices for several products.
2. Calculate percentage change between consecutive observations.
3. Identify the largest absolute percentage change.
4. Flag changes above the selected threshold.

## Assumptions
- Each product has the same number of observations.
- All starting prices are greater than zero.
- A change greater than 10% in absolute value is flagged.
- Percentage change is calculated using the earlier price as the base.

## Algorithm
1. Store product names and their historical price lists.
2. For each product, compare each price with the previous observation.
3. Calculate percentage change.
4. Display each change and flag its absolute value if above 10%.
5. Track the largest absolute change with product and period.
6. Display the largest fluctuation.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET product names, historical price lists, and threshold
SET largest_change = -1
FOR each product
    FOR each pair of consecutive prices
        previous = earlier price; current = next price
        percentage = (current - previous) / previous * 100
        DISPLAY percentage
        IF absolute percentage > threshold: flag change
        IF absolute percentage > largest_change: save product and period
DISPLAY largest fluctuation
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal price history | Use the supplied prices | Cooking Oil has the largest fluctuation (about 14.41%) from period 2 to 3. |
| No change | Set two consecutive prices to the same value | The percentage change for that pair is 0%. |
| Decrease | Reduce a later price below the earlier price | The percentage change is negative and its absolute value is used for threshold comparison. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The program compares consecutive price observations and calculates percentage changes. It reports both increases and decreases and uses absolute percentage change to identify the largest fluctuation.
