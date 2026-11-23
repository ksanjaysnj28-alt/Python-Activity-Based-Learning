# Case Study 43: Multi-Branch Sales Matrix Comparison
# sales[branch][product][day] stores units sold.

branches = ["Central", "North", "South"]
products = ["Notebook", "Pen", "Bottle"]
sales = [
    [[20, 25, 22], [40, 35, 45], [12, 15, 14]],
    [[18, 20, 24], [30, 32, 28], [20, 18, 22]],
    [[25, 28, 30], [26, 29, 27], [15, 17, 19]]
]

product_totals = [0, 0, 0]
highest_branch_total = -1
leading_branch = ""

print("BRANCH SALES SUMMARY")
for i in range(len(branches)):
    branch_total = 0
    best_product_total = -1
    best_product = ""

    for j in range(len(products)):
        product_total = 0
        for k in range(len(sales[i][j])):
            product_total = product_total + sales[i][j][k]
        product_totals[j] = product_totals[j] + product_total
        branch_total = branch_total + product_total
        if product_total > best_product_total:
            best_product_total = product_total
            best_product = products[j]

    print(branches[i], "Total units:", branch_total)
    print("  Best product:", best_product, "-", best_product_total, "units")
    if branch_total > highest_branch_total:
        highest_branch_total = branch_total
        leading_branch = branches[i]

print("\nPRODUCT-WISE TOTALS")
for j in range(len(products)):
    print(products[j], ":", product_totals[j], "units")
print("\nLeading branch:", leading_branch, "with", highest_branch_total, "units")
