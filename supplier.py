# supplier.py

from product import add_stock


suppliers = []


def add_supplier():

    print("\n========== ADD SUPPLIER ==========")

    supplier_id = input("Enter Supplier ID: ")

    for supplier in suppliers:

        if supplier["id"] == supplier_id:
            print("Supplier ID already exists!")
            return

    name = input("Enter Supplier Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    company = input("Enter Company Name: ")

    supplier = {
        "id": supplier_id,
        "name": name,
        "phone": phone,
        "email": email,
        "company": company
    }

    suppliers.append(supplier)

    print("\nSupplier added successfully!")


def view_suppliers():

    print("\n========== SUPPLIER LIST ==========")

    if len(suppliers) == 0:
        print("No supplier records found.")
        return

    for supplier in suppliers:

        print("--------------------------------")
        print("Supplier ID :", supplier["id"])
        print("Name        :", supplier["name"])
        print("Phone       :", supplier["phone"])
        print("Email       :", supplier["email"])
        print("Company     :", supplier["company"])


def search_supplier():

    print("\n========== SEARCH SUPPLIER ==========")

    supplier_id = input("Enter Supplier ID: ")

    for supplier in suppliers:

        if supplier["id"] == supplier_id:

            print("\nSupplier Found!")
            print("--------------------------------")
            print("Supplier ID :", supplier["id"])
            print("Name        :", supplier["name"])
            print("Phone       :", supplier["phone"])
            print("Email       :", supplier["email"])
            print("Company     :", supplier["company"])

            return

    print("Supplier not found.")


def purchase_stock():

    print("\n========== PURCHASE STOCK ==========")

    product_id = input("Enter Product ID: ")

    try:
        quantity = int(input("Enter Quantity Purchased: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid quantity.")
        return

    if add_stock(product_id, quantity):

        print("\nStock updated successfully!")
        print("Product ID :", product_id)
        print("Quantity Added :", quantity)

    else:

        print("Product not found.")