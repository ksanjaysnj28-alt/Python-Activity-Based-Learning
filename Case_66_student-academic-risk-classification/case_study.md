# Case Study 66: Student Academic Risk Classification

## Problem statement
Combine lists of marks, attendance, and laboratory scores to classify students into risk categories, identify multiple simultaneous risk factors, and generate a summary.

## Objectives
1. Combine marks, attendance, and laboratory scores for each student.
2. Identify risk factors using supplied thresholds.
3. Classify students as LOW, MODERATE, or HIGH risk.
4. Display a summary of the number of students in each category.

## Assumptions
- All sample scores and attendance percentages are between 0 and 100.
- Academic mark below 50, attendance below 75%, and lab score below 50 are risk factors.
- Two or more risk factors means HIGH risk; one means MODERATE; none means LOW.
- The thresholds are illustrative rules supplied for this case study, not official institutional policy.

## Algorithm
1. Store student names and parallel lists of marks, attendance, and lab scores.
2. For each student, set risk factor count to zero.
3. Check marks, attendance, and lab score against their thresholds.
4. Increase risk factor count for every failed condition.
5. Classify using the number of risk factors.
6. Display factor count and category.
7. Update and display category totals.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET student names, marks, attendance, and lab lists
SET low_count, moderate_count, high_count to zero
FOR each student
    SET risk_factors = 0
    IF marks < 50: risk_factors = risk_factors + 1
    IF attendance < 75: risk_factors = risk_factors + 1
    IF lab score < 50: risk_factors = risk_factors + 1
    IF risk_factors >= 2: category = HIGH
    ELSE IF risk_factors == 1: category = MODERATE
    ELSE: category = LOW
    UPDATE category count and display result
DISPLAY category totals
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal dataset | Use supplied student records | Aarav is LOW, Bhavna and Chirag are HIGH, and Divya is MODERATE risk. |
| All thresholds met | Set marks, attendance, and lab score above their limits | The student is classified LOW risk. |
| Two risk factors | Set any two measures below their thresholds | The student is classified HIGH risk. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The program combines three academic indicators and counts risk factors for each student. It uses nested conditions to classify each record and produces a category summary.
