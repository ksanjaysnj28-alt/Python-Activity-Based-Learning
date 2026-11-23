# Case Study 49: Tuple-Based Product Catalogue Audit
# Each tuple stores (product ID, price, stock, reorder level).

products = [
    ("P101", 45.0, 18, 10),
    ("P102", 12.5, 5, 8),
    ("P103", 120.0, 0, 5),
    ("P104", 75.0, 14, 6),
    ("P105", -20.0, 4, 3)  # Deliberately invalid price for validation.
]

inventory_value = 0
print("PRODUCT CATALOGUE AUDIT")
print("Replenishment required:")

for product in products:
    product_id, price, stock, reorder_level = product
    if price <= 0 or stock < 0 or reorder_level < 0:
        print(product_id, "Invalid record")
    else:
        value = price * stock
        inventory_value = inventory_value + value
        print(product_id, "Inventory value:", round(value, 2))
        if stock <= reorder_level:
            print("  Reorder:", product_id, "(stock", stock, ")")

print("\nTotal valid inventory value:", round(inventory_value, 2))
