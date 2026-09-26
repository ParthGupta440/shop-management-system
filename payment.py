# payment.py

from sales import sales


payments = []


def generate_bill():

    print("\n========== GENERATE BILL ==========")

    customer_id = input("Enter Customer ID: ")

    customer_sales = []

    for sale in sales:

        if sale["customer_id"] == customer_id:
            customer_sales.append(sale)

    if len(customer_sales) == 0:
        print("No sales found for this customer.")
        return

    subtotal = 0

    print("\n========================================")
    print("              SHOP BILL")
    print("========================================")

    print("Customer ID :", customer_id)

    print("----------------------------------------")

    for sale in customer_sales:

        amount = sale["total"]
        subtotal += amount

        print("Product  :", sale["product_name"])
        print("Quantity :", sale["quantity"])
        print("Price    :", "₹", sale["price"])
        print("Amount   :", "₹", amount)
        print("----------------------------------------")

    # 5% GST
    gst = subtotal * 0.05

    total = subtotal + gst

    print("Subtotal  :", "₹", subtotal)
    print("GST (5%)  :", "₹", gst)
    print("----------------------------------------")
    print("TOTAL     :", "₹", total)
    print("========================================")


def make_payment():

    print("\n========== MAKE PAYMENT ==========")

    customer_id = input("Enter Customer ID: ")

    customer_sales = []

    for sale in sales:

        if sale["customer_id"] == customer_id:
            customer_sales.append(sale)

    if len(customer_sales) == 0:
        print("No sales found.")
        return

    subtotal = 0

    for sale in customer_sales:
        subtotal += sale["total"]

    gst = subtotal * 0.05
    total = subtotal + gst

    print("Total Bill:", "₹", total)

    try:
        amount = float(input("Enter Payment Amount: ₹"))

    except ValueError:
        print("Invalid payment amount.")
        return

    if amount <= 0:
        print("Payment must be greater than zero.")
        return

    if amount < total:
        print("Insufficient payment.")
        print("Required Amount:", "₹", total)
        return

    payment = {
        "customer_id": customer_id,
        "amount": amount,
        "bill_amount": total,
        "status": "Paid"
    }

    payments.append(payment)

    change = amount - total

    print("\nPayment successful!")
    print("--------------------------------")
    print("Bill Amount :", "₹", total)
    print("Amount Paid :", "₹", amount)
    print("Change      :", "₹", change)


def payment_history():

    print("\n========== PAYMENT HISTORY ==========")

    if len(payments) == 0:
        print("No payment records found.")
        return

    for payment in payments:

        print("--------------------------------")
        print("Customer ID :", payment["customer_id"])
        print("Bill Amount :", "₹", payment["bill_amount"])
        print("Amount Paid :", "₹", payment["amount"])
        print("Status      :", payment["status"])