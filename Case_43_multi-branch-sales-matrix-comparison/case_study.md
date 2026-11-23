# Case Study 43: Multi-Branch Sales Matrix Comparison

## Problem statement
Store product sales across branches and days in nested lists, calculate product totals, compare branches, and identify the best-performing product for each branch.

## Objectives
1. Represent branch, product, and daily sales using nested lists.
2. Calculate product-wise totals across branches and days.
3. Compare total sales among branches.
4. Identify the best-selling product in each branch.

## Assumptions
- Sales values are non-negative quantities.
- Each branch has the same products and number of days.
- The sample contains three branches, three products, and three days.
- A tie is resolved by keeping the first product or branch encountered.

## Algorithm
1. Store branch names, product names, and sales data (branch -> product -> day).
2. For each branch, calculate each product total across days.
3. Add product totals to get the branch total.
4. Track the best-performing product in each branch.
5. Add every branch/product/day value to product-wise totals.
6. Compare branch totals and display the leading branch.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET branches, products, and 3-dimensional sales list
SET product_totals to zero for every product
SET highest_branch_total = -1
FOR each branch
    SET branch_total = 0 and best_product_total = -1
    FOR each product
        SET product_total = 0
        FOR each day: add sales to product_total
        ADD product_total to branch_total and product_totals
        IF product_total > best_product_total: update best product
    DISPLAY branch total and best product
    IF branch_total > highest_branch_total: update leading branch
DISPLAY product_totals and leading branch
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal dataset | Use the supplied 3-branch and 3-day sales data | Central branch leads with 228 units. |
| Zero sales day | Change one day of sales to zero for all products | Totals decrease correctly; no negative values are generated. |
| Branch tie | Adjust sales so two branches have equal totals | The first branch with the tied maximum is retained. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The three-level nested list represents sales by branch, product, and day. Nested loops calculate totals and comparisons without requiring external libraries.
