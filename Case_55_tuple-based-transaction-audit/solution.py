# Case Study 55: Tuple-Based Transaction Audit
# Each tuple stores (transaction ID, amount, transaction type).

transactions = [
    ("TX101", 5000, "DEPOSIT"),
    ("TX102", 2500, "WITHDRAWAL"),
    ("TX103", 28000, "WITHDRAWAL"),
    ("TX102", 1200, "DEPOSIT"),  # Duplicate identifier.
    ("TX105", -500, "WITHDRAWAL"),  # Invalid amount.
    ("TX106", 900, "TRANSFER")  # Invalid type for this policy.
]
allowed_types = ["DEPOSIT", "WITHDRAWAL"]
withdrawal_review_limit = 20000
seen_ids = []
valid_count = 0
flagged_count = 0

print("TRANSACTION AUDIT REPORT")
for transaction in transactions:
    transaction_id, amount, transaction_type = transaction
    record_valid = True

    if transaction_id in seen_ids:
        print(transaction_id, "Duplicate transaction ID")
        flagged_count = flagged_count + 1
        record_valid = False

    if amount <= 0:
        print(transaction_id, "Invalid amount")
        flagged_count = flagged_count + 1
        record_valid = False

    if transaction_type not in allowed_types:
        print(transaction_id, "Invalid transaction type")
        flagged_count = flagged_count + 1
        record_valid = False

    if record_valid:
        seen_ids.append(transaction_id)
        valid_count = valid_count + 1
        if transaction_type == "WITHDRAWAL" and amount > withdrawal_review_limit:
            print(transaction_id, "Large withdrawal - review required")

print("\nValid records:", valid_count)
print("Audit flags:", flagged_count)
