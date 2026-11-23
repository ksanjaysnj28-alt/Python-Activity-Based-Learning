# Case Study 49: Tuple-Based Product Catalogue Audit

## Problem statement
Store product identifiers, prices, and stock quantities in tuples; detect invalid records, calculate inventory values, and identify items requiring replenishment.

## Objectives
1. Represent each product record as a tuple.
2. Validate product price and stock values.
3. Calculate total inventory value.
4. Identify products at or below their reorder level.

## Assumptions
- Each tuple is (product_id, price, stock_quantity, reorder_level).
- A valid price is greater than zero and stock/reorder levels are zero or higher.
- A product needs replenishment when stock is less than or equal to its reorder level.
- The supplied catalogue is sample data.

## Algorithm
1. Store product records as tuples in a list.
2. Set inventory value to zero.
3. Visit each tuple and unpack its four values.
4. Check whether price and quantities are valid.
5. For a valid record, calculate price multiplied by stock and add it to total inventory value.
6. If stock is at or below reorder level, add the product to the reorder report.
7. Display invalid records, inventory value, and reorder list.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET product tuple list
SET inventory_value = 0
FOR each product tuple
    UNPACK product_id, price, stock, reorder_level
    IF price <= 0 OR stock < 0 OR reorder_level < 0: report invalid
    ELSE
        inventory_value = inventory_value + price * stock
        IF stock <= reorder_level: report replenishment required
DISPLAY inventory value
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal catalogue | Use all five supplied product tuples | P102 and P103 need replenishment; P105 is flagged invalid. |
| Negative stock | Change P101 stock to -2 | P101 is reported as an invalid record and is excluded from value. |
| Stock at reorder level | Set P104 stock equal to 6 | P104 is included in the replenishment report. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The audit uses tuples to keep each product record together. It validates records, calculates the value of valid stock, and reports products that have reached their reorder level.
