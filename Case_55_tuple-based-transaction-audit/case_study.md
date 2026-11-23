# Case Study 55: Tuple-Based Transaction Audit

## Problem statement
Process transaction tuples containing identifiers, amounts, and transaction types; detect duplicate identifiers, invalid amounts, and suspicious sequences.

## Objectives
1. Store transaction records as tuples.
2. Detect repeated transaction identifiers.
3. Flag zero or negative transaction amounts.
4. Flag unusually large withdrawals according to a sample threshold.

## Assumptions
- Each tuple stores (transaction_id, amount, transaction_type).
- Valid types are DEPOSIT and WITHDRAWAL.
- Amount must be greater than zero.
- A withdrawal above 20,000 is flagged for review; this is a sample rule, not a banking rule.

## Algorithm
1. Store transaction tuples in a list.
2. For each tuple, unpack identifier, amount, and type.
3. Check whether the identifier has appeared earlier.
4. Validate amount and transaction type.
5. If the record is valid, add the identifier to the seen list.
6. Flag a withdrawal above 20,000 as suspicious for review.
7. Display each finding and the audit totals.

## Flowchart
See `flowchart.png`.

## Pseudocode
```text
START
SET transaction tuple list and empty seen-ID list
SET valid_count = 0 and flagged_count = 0
FOR each transaction tuple
    UNPACK ID, amount, type
    IF ID is already in seen-ID list: report duplicate; increment flagged_count
    IF amount <= 0 OR type is not an allowed type: report invalid; increment flagged_count
    ELSE
        ADD ID to seen-ID list; increment valid_count
        IF type is WITHDRAWAL AND amount > threshold: report review flag
DISPLAY audit counts
STOP
```

## Python source code
See `solution.py`.

## Test cases
| Test case | Input/change | Expected result |
|---|---|
| Normal audit | Use the supplied six transaction records | TX102 is duplicate; TX105 has an invalid amount; TX106 has an invalid type. |
| Repeated ID | Add another record with TX101 | The repeated identifier is flagged. |
| Large withdrawal | Set a valid withdrawal to 25,000 | The record is valid but a review message is displayed. |

## Sample output
The screenshot `output_screenshot.png` and text file `sample_output.txt` were generated from an execution of `solution.py` using the sample data in that file.

## Conclusion
The program audits transaction tuples by checking identifiers, amounts, and transaction types. A large withdrawal is separately flagged for review without being treated as an invalid record.
