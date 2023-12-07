import tkinter as tk
from tkinter import simpledialog, font

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.customers = []
        self.transactions = []

    def add_book(self):
        title = simpledialog.askstring("Input", "Enter book title:")
        author = simpledialog.askstring("Input", "Enter author:")
        isbn = simpledialog.askstring("Input", "Enter ISBN:")
        quantity = int(simpledialog.askstring("Input", "Enter quantity:"))
        price = float(simpledialog.askstring("Input", "Enter price:"))

        book = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'quantity': quantity,
            'price': price
        }
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\nLibrary Books:")
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Quantity: {book['quantity']}, Price: {book['price']}")

    def add_customer(self):
        name = simpledialog.askstring("Input", "Enter customer name:")
        contact = simpledialog.askstring("Input", "Enter contact number:")

        customer = {
            'name': name,
            'contact': contact
        }
        self.customers.append(customer)
        print(f"Customer '{name}' added successfully!")

    def display_customers(self):
        if not self.customers:
            print("No customers in the library.")
            return

        print("Customers:")
        for customer in self.customers:
            print(f"Name: {customer['name']}, Contact: {customer['contact']}")

    def borrow_book(self):
        customer_name = simpledialog.askstring("Input", "Enter customer name:")
        isbn = simpledialog.askstring("Input", "Enter ISBN of the book to borrow:")

        customer = next((c for c in self.customers if c['name'] == customer_name), None)
        book = next((b for b in self.books if b['isbn'] == isbn), None)

        if customer and book and book['quantity'] > 0:
            transaction = {
                'customer': customer_name,
                'book': book['title'],
                'isbn': isbn,
                'date': '2023-12-06'
            }
            self.transactions.append(transaction)
            book['quantity'] -= 1
            print(f"{customer_name} borrowed '{book['title']}' successfully!")
        elif not customer:
            print(f"Customer '{customer_name}' not found!")
        elif not book:
            print(f"Book with ISBN '{isbn}' not found!")
        elif book['quantity'] == 0:
            print(f"Book '{book['title']}' is out of stock!")

    def display_transactions(self):
        if not self.transactions:
            print("No transactions in the library.")
            return

        print("\nTransactions:")
        for transaction in self.transactions:
            print(f"Customer: {transaction['customer']}, Book: {transaction['book']}, ISBN: {transaction['isbn']}, Date: {transaction['date']}")

library_system = LibraryManagementSystem()

# Tkinter GUI setup
root = tk.Tk()
root.title("Library Management System")

def handle_button_click(choice):
    if choice.strip() == 'Add book':
        library_system.add_book()
    elif choice.strip() == 'Display books':
        library_system.display_books()
    elif choice.strip() == 'Add customer':
        library_system.add_customer()
    elif choice.strip() == 'Display customer':
        library_system.display_customers()
    elif choice.strip() == 'Borrow book':
        library_system.borrow_book()
    elif choice.strip() == 'Display transactions':
        library_system.display_transactions()
    elif choice.strip() == 'Exiting the library management system':
        print("Exiting the Library Management System. Goodbye!")
        root.destroy()
    else:
        print("Invalid choice. Please enter a valid option.")

# GUI components
label = tk.Label(root, text="Library Management System Menu")
label.pack()

options = ["Add book", "Display books", "Add customer", "Display customer", "Borrow book", "Display transactions","Search books", "Exiting the library management system"]

bold_font = font.Font(weight="bold")

for i, button_text in enumerate(options):
    button = tk.Button(root, text=button_text, command=lambda value=button_text: handle_button_click(value), width=40, bg='gray', pady=5, font=bold_font)
    button.pack()

root.mainloop()