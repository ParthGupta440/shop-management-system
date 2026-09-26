# product.py

products = []


def add_product():
    print("\n========== ADD PRODUCT ==========")

    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:
            print("Product ID already exists!")
            return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")

    try:
        price = float(input("Enter Price: ₹"))
        quantity = int(input("Enter Quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

    print("\nProduct added successfully!")


def view_products():
    print("\n========== PRODUCT / STOCK LIST ==========")

    if len(products) == 0:
        print("No products found.")
        return

    for product in products:
        print("--------------------------------")
        print("Product ID :", product["id"])
        print("Name       :", product["name"])
        print("Category   :", product["category"])
        print("Price      :", "₹", product["price"])
        print("Quantity   :", product["quantity"])


def search_product():
    print("\n========== SEARCH PRODUCT ==========")

    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:
            print("\nProduct Found!")
            print("--------------------------------")
            print("Product ID :", product["id"])
            print("Name       :", product["name"])
            print("Category   :", product["category"])
            print("Price      :", "₹", product["price"])
            print("Quantity   :", product["quantity"])
            return

    print("Product not found.")


def update_stock(product_id, quantity):
    for product in products:

        if product["id"] == product_id:

            if product["quantity"] >= quantity:
                product["quantity"] -= quantity
                return True

            return False

    return False


def add_stock(product_id, quantity):

    for product in products:

        if product["id"] == product_id:
            product["quantity"] += quantity
            return True

    return False


def get_product(product_id):

    for product in products:

        if product["id"] == product_id:
            return product

    return None