# customer.py

customers = []


def add_customer():
    print("\n========== ADD CUSTOMER ==========")

    customer_id = input("Enter Customer ID: ")

    for customer in customers:
        if customer["id"] == customer_id:
            print("Customer ID already exists!")
            return

    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    customer = {
        "id": customer_id,
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    customers.append(customer)

    print("\nCustomer added successfully!")


def view_customers():
    print("\n========== CUSTOMER LIST ==========")

    if len(customers) == 0:
        print("No customer records found.")
        return

    for customer in customers:
        print("--------------------------------")
        print("Customer ID :", customer["id"])
        print("Name        :", customer["name"])
        print("Phone       :", customer["phone"])
        print("Email       :", customer["email"])
        print("Address     :", customer["address"])


def search_customer():
    print("\n========== SEARCH CUSTOMER ==========")

    customer_id = input("Enter Customer ID: ")

    for customer in customers:
        if customer["id"] == customer_id:
            print("\nCustomer Found!")
            print("--------------------------------")
            print("Customer ID :", customer["id"])
            print("Name        :", customer["name"])
            print("Phone       :", customer["phone"])
            print("Email       :", customer["email"])
            print("Address     :", customer["address"])
            return

    print("Customer not found.")