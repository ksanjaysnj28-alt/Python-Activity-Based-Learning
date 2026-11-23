# Case Study 61: Nested List Examination Seating Validation

## Problem statement
Validate a complete seating matrix for duplicate roll numbers, reserved positions, empty seats, and invalid student allocations.

## Objectives
1. Represent a classroom seating plan as a nested list.
2. Check reserved positions against the seating policy.
3. Detect duplicate roll numbers.
4. Report empty seats and invalid entries.

## Assumptions
- The classroom has 3 rows and 4 columns.
- The reserved positions are row 1, column 2 and row 3, column 4 (using 1-based positions).
- The text RESERVED must appear in reserved positions.
- Other occupied seats must contain a roll number beginning with ST and followed by digits.
- A value of EMPTY indicates a vacant seat.

## Algorithm
1. Create the seating matrix and reserved-position list.
2. Visit each row and each seat.
3. If the seat is reserved, check whether its value is RESERVED.
4. Otherwise, report EMPTY seats, validate roll-number format, and check for duplicates.
5. Store every valid roll number already seen.
6. Display duplicate, invalid, reserved-seat, and vacancy findings.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET seating matrix and reserved positions
SET seen roll numbers to empty list
FOR each row and column
    IF position is reserved
        IF seat is not RESERVED: report reserved-position error
    ELSE IF seat is EMPTY: report vacant seat
    ELSE
        IF seat does not start with ST and contain digits: report invalid roll
        IF seat already appears in seen list: report duplicate
        ELSE: add seat to seen list
DISPLAY validation summary
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal seating matrix | Use the supplied seating matrix | ST101 is duplicated, EMPTY is vacant, and BAD09 is invalid. |
| Reserved mismatch | Replace RESERVED at row 3 column 4 with a roll number | A reserved-seat error is displayed. |
| No duplicate | Replace the second ST101 with ST106 | Duplicate count becomes zero. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The program uses a nested list to model classroom seats and tuples to represent reserved coordinates. It checks seat rules, duplicate roll numbers, invalid identifiers, and vacancies.
