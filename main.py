from customer import add_customer, view_customers, search_customer, customers
from product import add_product, view_products, search_product, products
from sales import create_sale, view_sales, search_sale, sales
from payment import generate_bill, make_payment, payment_history
from supplier import (
    add_supplier,
    view_suppliers,
    search_supplier,
    purchase_stock,
    suppliers
)
def customer_management():
    while True:
        print("\n----- Customer Management -----")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
def product_management():
    while True:
        print("\n----- Product / Stock Management -----")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Purchase / Add Stock")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            purchase_stock()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
def sales_management():
    while True:
        print("\n----- Sales Management -----")
        print("1. Create Sale")
        print("2. View Sales")
        print("3. Search Customer Sales")
        print("4. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            search_sale()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
def payment_management():
    while True:
        print("\n----- Payment Management -----")
        print("1. Generate Bill")
        print("2. Make Payment")
        print("3. Payment History")
        print("4. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            generate_bill()
        elif choice == "2":
            make_payment()
        elif choice == "3":
            payment_history()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
def supplier_management():
    while True:
        print("\n----- Supplier Management -----")
        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Search Supplier")
        print("4. Purchase / Add Stock")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_supplier()
        elif choice == "2":
            view_suppliers()
        elif choice == "3":
            search_supplier()
        elif choice == "4":
            purchase_stock()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
def generate_report():
    print("\n----- Shop Report -----")

    total_customers = len(customers)
    total_products = len(products)
    total_sales = len(sales)
    total_suppliers = len(suppliers)
    total_revenue = 0
    for sale in sales:
        total_revenue += sale["total"]
    total_stock = 0
    for product in products:
        total_stock += product["quantity"]
    print("Total Customers :", total_customers)
    print("Total Products  :", total_products)
    print("Total Suppliers :", total_suppliers)
    print("Total Sales     :", total_sales)
    print("Current Stock   :", total_stock)
    print("Sales Revenue   : ₹", total_revenue)
def main():
    while True:
        print("\n===================================")
        print("       SHOP MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Customer Management")
        print("2. Product / Stock Management")
        print("3. Sales Management")
        print("4. Payment / Bill")
        print("5. Supplier Management")
        print("6. Generate Shop Report")
        print("7. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            customer_management()
        elif choice == "2":
            product_management()
        elif choice == "3":
            sales_management()
        elif choice == "4":
            payment_management()
        elif choice == "5":
            supplier_management()
        elif choice == "6":
            generate_report()
        elif choice == "7":
            print("\nThank you for using the Shop Management System!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")
if __name__ == "__main__":
    main()
