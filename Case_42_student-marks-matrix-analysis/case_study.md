# Case Study 42: Student Marks Matrix Analysis

## Problem statement
Analyse a matrix of student marks across subjects, calculate row-wise and column-wise statistics, identify top performers, and detect subjects with low average performance.

## Objectives
1. Store student marks in a nested list (matrix).
2. Calculate each student total and average.
3. Calculate each subject average.
4. Identify the top-performing student and subjects below the defined average threshold.

## Assumptions
- All marks are numeric and lie between 0 and 100.
- Every student has a mark for every subject.
- A subject average below 60 is treated as low for this sample.
- The supplied names and marks are sample data and can be edited.

## Algorithm
1. Start with student names, subject names, and the marks matrix.
2. For each student row, add the marks and calculate the average.
3. Track the student with the highest total.
4. For each subject column, add marks across all students and calculate its average.
5. Report subject averages and flag any average below 60.
6. Display the top student and stop.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET students, subjects, and marks matrix
SET highest_total = -1
FOR each student row
    SET total = 0
    FOR each mark in the row: total = total + mark
    CALCULATE average = total / number of subjects
    DISPLAY student total and average
    IF total > highest_total: update highest_total and topper
FOR each subject column
    ADD marks from all student rows
    CALCULATE and DISPLAY subject average
    IF average < 60: DISPLAY low-average warning
DISPLAY topper
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal dataset | Four students with marks in all three subjects | Charan is the top performer with 272 marks. |
| Low subject average | Change every Statistics mark to 40 | Statistics average is below 60 and a warning is shown. |
| Tie in total | Give two students the same highest total | The first student encountered with that total remains the displayed topper. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The program uses a nested list and nested loops to calculate student-wise and subject-wise statistics. It also identifies the highest total and highlights a subject whose average is below the chosen threshold.
