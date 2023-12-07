def search_books(self):
        title = simpledialog.askstring("Input", "Enter title of the book to be searched:")
        book = next((b for b in self.books if b['title'] == title), None)
        if book:
            result_text.insert(tk.END, f"{title} is available\n")
        else:
            result_text.insert(tk.END, f"{title} is not available\n")