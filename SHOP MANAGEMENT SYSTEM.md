# SHOP MANAGEMENT SYSTEM

## Project Report

### Submitted By

**Name:** Parth Gupta

**Course:** B.Tech CSE

**University:** VIT Bhopal

**Course:** Python Essentials

---

# 1. Introduction

Shop Management System is a Python-based project developed to manage different activities of a shop. The system provides a simple menu-driven interface through which users can manage customers, products, suppliers, sales, and payments.

The main aim of this project is to reduce manual work and organize shop-related information in a structured manner. This project demonstrates the use of Python programming concepts such as functions, lists, dictionaries, and modules.

---

# 2. Problem Statement

Managing customer records, product inventory, sales transactions, and supplier information manually can be time-consuming and difficult. There is also a possibility of errors while maintaining records.

This project provides a simple solution by allowing users to store and manage shop-related information through a Python application.

---

# 3. Objectives

* To manage customer information.
* To maintain product and stock records.
* To record sales transactions.
* To manage supplier details.
* To generate bills and process payments.
* To generate basic shop reports.

---

# 4. Technologies Used

* Python 3
* Functions
* Lists
* Dictionaries
* Modular Programming

---

# 5. Project Modules

## 5.1 Customer Management
This module allows users to:
* Add new customers
* View customer records
* Search customers using Customer ID

---

## 5.2 Product Management
This module is responsible for:
* Adding products
* Viewing product details
* Searching products
* Managing stock quantity

---

## 5.3 Sales Management
This module allows users to:
* Create sales transactions
* View sales records
* Search sales using Customer ID

Whenever a sale is completed, the stock quantity is automatically updated.

---

## 5.4 Supplier Management
This module is used to:
* Add supplier information
* View supplier records
* Search suppliers
* Purchase stock from suppliers

---

## 5.5 Payment Management
This module handles:
* Bill generation
* GST calculation
* Payment processing
* Payment history

---

## 5.6 Report Generation
The report module displays:
* Total customers
* Total products
* Total suppliers
* Total sales
* Available stock
* Total revenue

---

# 6. Project Structure
```text
main.py
customer.py
product.py
sales.py
supplier.py
payment.py
```

### File Description
| File Name   | Purpose                        |
| ----------- | ------------------------------ |
| main.py     | Main menu and program control  |
| customer.py | Customer management            |
| product.py  | Product and stock management   |
| sales.py    | Sales management               |
| supplier.py | Supplier management            |
| payment.py  | Billing and payment management |

---

# 7. Working of the Project
1. The user starts the application by running the main.py file.
2. A menu is displayed containing different management options.
3. Users can add customers and products.
4. Suppliers can be added and stock can be updated.
5. Sales can be created for existing products and customers.
6. Bills are generated based on sales records.
7. Payments are recorded in the system.
8. Reports can be generated to view overall shop information.

---

# 8. Learning Outcomes
Through this project, I learned:
* Working with multiple Python modules.
* Creating and using functions.
* Managing data using lists and dictionaries.
* Connecting different modules in a single application.
* Implementing a menu-driven program.
* Applying basic problem-solving skills using Python.

---

# 9. Future Improvements
The following features can be added in future versions:
* Database integration using MySQL or SQLite.
* Graphical User Interface (GUI).
* User authentication and login system.
* Export reports to PDF or Excel.
* Advanced inventory tracking.

---

# 10. Conclusion
The Shop Management System successfully performs basic shop management operations such as customer handling, product management, sales processing, supplier management, billing, and reporting. The project helped in understanding practical implementation of Python programming concepts and provided experience in developing a modular application.

---

# References
* Python Official Documentation
* Course Material Provided in Python Essentials
* VS Code Documentation