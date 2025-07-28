sales_product = {
    "laptop":[ 1000, 1200, 1100],
    "phone":[500, 600, 700],
    "buds":[300, 250, 200]
}

total_sales = {}

for product, sales in sales_product.items():
    total_sales[product] = sum(sales)
print(total_sales)
