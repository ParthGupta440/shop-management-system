# sales.py

from customer import customers
from product import products, get_product, update_stock


sales = []


def create_sale():

    print("\n========== CREATE SALE ==========")

    customer_id = input("Enter Customer ID: ")

    customer_found = False

    for customer in customers:

        if customer["id"] == customer_id:
            customer_found = True
            break

    if not customer_found:
        print("Customer not found.")
        print("Please add the customer first.")
        return

    product_id = input("Enter Product ID: ")

    product = get_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nProduct Details")
    print("--------------------------------")
    print("Product Name :", product["name"])
    print("Price        :", "₹", product["price"])
    print("Stock        :", product["quantity"])

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid quantity.")
        return

    if product["quantity"] < quantity:
        print("Insufficient stock.")
        return

    total = product["price"] * quantity

    update_stock(product_id, quantity)

    sale = {
        "customer_id": customer_id,
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "price": product["price"],
        "total": total
    }

    sales.append(sale)

    print("\nSale completed successfully!")
    print("--------------------------------")
    print("Customer ID :", customer_id)
    print("Product     :", product["name"])
    print("Quantity    :", quantity)
    print("Price       :", "₹", product["price"])
    print("Total       :", "₹", total)


def view_sales():

    print("\n========== SALES RECORDS ==========")

    if len(sales) == 0:
        print("No sales records found.")
        return

    for sale in sales:

        print("--------------------------------")
        print("Customer ID :", sale["customer_id"])
        print("Product ID  :", sale["product_id"])
        print("Product     :", sale["product_name"])
        print("Quantity    :", sale["quantity"])
        print("Price       :", "₹", sale["price"])
        print("Total       :", "₹", sale["total"])


def search_sale():

    print("\n========== SEARCH SALE ==========")

    customer_id = input("Enter Customer ID: ")

    found = False

    for sale in sales:

        if sale["customer_id"] == customer_id:

            found = True

            print("--------------------------------")
            print("Product     :", sale["product_name"])
            print("Quantity    :", sale["quantity"])
            print("Total       :", "₹", sale["total"])

    if not found:
        print("No sales found for this customer.")