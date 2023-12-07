import tkinter as tk
from tkinter import simpledialog
from tkinter import simpledialog, font
import datetime


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
        result_text.insert(tk.END, f"Book '{title}' added successfully!\n")

    def add_customer(self):
        name = simpledialog.askstring("Input", "Enter customer name:")
        contact = simpledialog.askstring("Input", "Enter contact number:")

        customer = {
            'name': name,
            'contact': contact
        }
        self.customers.append(customer)
        result_text.insert(tk.END, f"Customer '{name}' added successfully!\n")

    def search_books(self):
        title_to_search = simpledialog.askstring("Input", "Enter title of the book to be searched:")
        title_to_search_lower = title_to_search.lower()

        book = next((b for b in self.books if b['title'].lower() == title_to_search_lower), None)

        if book:
            result_text.insert(tk.END, f"{title_to_search} is available\n")
        else:
            result_text.insert(tk.END, f"{title_to_search} is not available\n")


    def display_books(self):
        result_text.delete("1.0", tk.END) 
        result_text.insert(tk.END, "\nLibrary Books:\n")
        if len(self.books) > 0:
            for book in self.books:
                result_text.insert(tk.END, f" Title: {book['title']} \n Author: {book['author']} \n ISBN: {book['isbn']} \n Quantity: {book['quantity']} \n Price: {book['price']}\n")
        else:
            result_text.insert(tk.END, "SORRY! NO BOOKS AVAILABLE CURRENTLY\n")

    def display_customers(self):
        result_text.delete("1.0", tk.END)  
        result_text.insert(tk.END, "\nCustomers:\n")
        if len(self.customers) > 0:
            for customer in self.customers:
                result_text.insert(tk.END, f"Name: {customer['name']}, Contact: {customer['contact']}\n")
        else:
            result_text.insert(tk.END, "NO CUSTOMERS AVAILABLE\n")

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
                'date': datetime.datetime.now()
            }
            self.transactions.append(transaction)
            book['quantity'] -= 1
            result_text.insert(tk.END, f"{customer_name} borrowed '{book['title']}' successfully!\n")
        elif not customer:
            result_text.insert(tk.END, f"Customer '{customer_name}' not found!\n")
        elif not book:
            result_text.insert(tk.END, f"Book with ISBN '{isbn}' not found!\n")
        elif book['quantity'] == 0:
            result_text.insert(tk.END, f"Book '{book['title']}' is out of stock!\n")

    def display_transactions(self):
        result_text.delete("1.0", tk.END)  
        result_text.insert(tk.END, "\nTransactions:\n")
        for transaction in self.transactions:
            result_text.insert(tk.END, f"Customer: {transaction['customer']}, Book: {transaction['book']}, ISBN: {transaction['isbn']}, Date: {transaction['date']}\n")

lm = LibraryManagementSystem()

root = tk.Tk()
root.title("Library Management System")

result_text = tk.Text(root, height=20, width=50)
result_text.pack()

def handle_button_click(choice):
    if choice == '1':
        lm.add_book()
    elif choice == '2':
        lm.display_books()
    elif choice == '3':
        lm.add_customer()
    elif choice == '4':
        lm.display_customers()
    elif choice == '5':
        lm.borrow_book()
    elif choice == '6':
        lm.display_transactions()
    elif choice == '7':
        lm.search_books()
    elif choice == '8':
        result_text.insert(tk.END, "Exiting the Library Management System. Goodbye!\n")
        root.destroy()
    else:
        result_text.insert(tk.END, "Invalid choice. Please enter a number between 1 and 8.\n")

# GUI components
label = tk.Label(root, text="Library Management System Menu")
label.pack()

options = ["Add book", "Display books", "Add customer", "Display customer", "Borrow book", "Display transactions","Search books", "Exiting the library management system"]

bold_font = font.Font(weight="bold")


for i, button_text in enumerate(options):
    button = tk.Button(root, text=button_text, command=lambda i=i: handle_button_click(str(i)), width=40, bg='gray', pady=5, font=bold_font)
    button.pack()
    print(i)

root.mainloop()