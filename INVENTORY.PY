import tkinter as tk
from tkinter import messagebox, ttk
import datetime
from fpdf import FPDF
from database import fetch_db_query, execute_db_query

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")

        # Left Frame
        self.left = tk.Frame(master, width=750, height=768, bg='SkyBlue')
        self.left.pack(side=tk.LEFT)

        # Right Frame
        self.right = tk.Frame(master, width=500, height=768, bg='white')
        self.right.pack(side=tk.RIGHT)

        # Heading Label
        self.heading = tk.Label(self.left, text="MARVELS STORE", font=('ALGERIAN', 40, 'bold'), fg='Black')
        self.heading.place(x=100, y=10)

        # Labels and Entries for Product Details
        self.enterid = tk.Label(self.left, text="Product ID", font=('calibri', 20, 'bold'), fg='black')
        self.enterid.place(x=50, y=80)

        self.enteride = tk.Entry(self.left, width=25, font=('Calibri', 18, 'bold'), bg='lightblue')
        self.enteride.place(x=220, y=80)
        self.enteride.focus()

        self.entername = tk.Label(self.left, text="Product Name", font=('calibri', 20, 'bold'), fg='black')
        self.entername.place(x=50, y=130)

        self.enternamee = tk.Entry(self.left, width=25, font=('Calibri', 18, 'bold'), bg='lightblue')
        self.enternamee.place(x=220, y=130)

        self.enterprice = tk.Label(self.left, text="Product Price", font=('calibri', 20, 'bold'), fg='black')
        self.enterprice.place(x=50, y=180)

        self.enterpricee = tk.Entry(self.left, width=25, font=('Calibri', 18, 'bold'), bg='lightblue')
        self.enterpricee.place(x=220, y=180)

        self.enterquantity = tk.Label(self.left, text="Product Quantity", font=('calibri', 17, 'bold'), fg='black')
        self.enterquantity.place(x=50, y=230)

        self.enterquantitye = tk.Entry(self.left, width=25, font=('Calibri', 18, 'bold'), bg='lightblue')
        self.enterquantitye.place(x=220, y=230)

        # Buttons
        self.add_btn = tk.Button(self.left, text="Add Product", width=18, height=2, fg='black',
                                 command=self.add_product)
        self.add_btn.place(x=580, y=120)

        self.search_btn = tk.Button(self.left, text="Find", width=18, height=2, fg='black',
                                    command=self.search_product)
        self.search_btn.place(x=580, y=70)

        self.edit_btn = tk.Button(self.left, text="Edit Product", width=18, height=2, fg='black',
                                  command=self.edit_product)
        self.edit_btn.place(x=580, y=170)

        self.rename_btn = tk.Button(self.left, text="Rename Product", width=18, height=2, fg='black',
                                    command=self.rename_product)
        self.rename_btn.place(x=580, y=220)

        self.add_to_cart_btn = tk.Button(self.left, text="Add to Cart", width=18, height=2, fg='black',
                                         command=self.add_to_cart)
        self.add_to_cart_btn.place(x=580, y=270)

        self.bill_btn = tk.Button(self.left, text="Generate Bill", width=18, height=2, fg='black',
                                  command=self.generate_bill)
        self.bill_btn.place(x=580, y=320)

        self.showcart_btn = tk.Button(self.left, text="Show Cart", width=18, height=2, fg='black',
                                      command=self.show_cart)
        self.showcart_btn.place(x=580, y=370)

        self.show_products_btn = tk.Button(self.left, text="Show Product Details", width=18, height=2,
                                           fg='black', command=self.show_products)
        self.show_products_btn.place(x=580, y=420)

        self.show_all_products_btn = tk.Button(self.left, text="Show All Products", width=18, height=2,
                                               fg='black', command=self.show_all_products)
        self.show_all_products_btn.place(x=580, y=470)

        self.remove_from_cart_btn = tk.Button(self.left, text="Remove from Cart", width=18, height=2,
                                              fg='black', command=self.remove_from_cart)
        self.remove_from_cart_btn.place(x=580, y=570)

        self.remove_product_btn = tk.Button(self.left, text="Remove Product", width=18, height=2,
                                            fg='black', command=self.remove_product)
        self.remove_product_btn.place(x=580, y=620)

        self.exit_btn = tk.Button(self.left, text="Exit", width=18, height=2, bg='red', fg='white', command=self.exit_app)
        self.exit_btn.place(x=580, y=670)

        # Create a frame for the date label and Treeview
        self.right_top = tk.Frame(self.right, bg='white')
        self.right_top.pack(side=tk.TOP, fill=tk.X)

        # Date Label
        self.date_l = tk.Label(self.right_top, text="Date: " + str(datetime.datetime.now().date()),
                               font=('Calibri', 12, 'bold'), fg='black', bg='white')
        self.date_l.pack(anchor='w', padx=10, pady=5)

        # Treeview for displaying products
        self.tree = ttk.Treeview(self.right, columns=('ID', 'Name', 'Price', 'Quantity'), show='headings')
        self.tree.heading('ID', text='Product ID')
        self.tree.heading('Name', text='Product Name')
        self.tree.heading('Price', text='Product Price')
        self.tree.heading('Quantity', text='Product Quantity')
        self.tree.column('ID', anchor='center')
        self.tree.column('Name', anchor='center')
        self.tree.column('Price', anchor='center')
        self.tree.column('Quantity', anchor='center')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Total Price Label
        self.total_price_label = tk.Label(self.right_top, text="Total Price: $0.00", font=('Calibri', 12, 'bold'),
                                          fg='black', bg='white')
        self.total_price_label.pack(anchor='e', padx=10, pady=5)

        # Initialize the product list
        self.show_all_products()

        # Initialize total price
        self.total_price = 0

        # Bind TreeviewSelect event to function
        self.tree.bind("<<TreeviewSelect>>", self.tree_item_selected)

    def tree_item_selected(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            if item_values:
                # Update entry fields with selected item's details
                self.enteride.delete(0, tk.END)
                self.enteride.insert(0, item_values[0])  # Product ID
                self.enternamee.delete(0, tk.END)
                self.enternamee.insert(0, item_values[1])  # Product Name
                self.enterpricee.delete(0, tk.END)
                self.enterpricee.insert(0, item_values[2])  # Product Price
                self.enterquantitye.delete(0, tk.END)
                self.enterquantitye.insert(0, item_values[3])  # Product Quantity

    def add_product(self):
        product_id = self.enteride.get()
        product_name = self.enternamee.get()
        product_price = self.enterpricee.get()
        product_quantity = self.enterquantitye.get()
        if product_id and product_name and product_price and product_quantity:
            try:
                product_price = float(product_price)
                product_quantity = int(product_quantity)
                execute_db_query('''
                    INSERT INTO products (id, name, price, quantity) VALUES (?, ?, ?, ?)
                ''', (product_id, product_name, product_price, product_quantity))
                messagebox.showinfo("Success", "Product added successfully!")
                self.update_totals()
                self.show_all_products()
            except ValueError:
                messagebox.showerror("Error", "Invalid price or quantity. Please enter valid numbers.")
        else:
            messagebox.showerror("Error", "Please enter all fields.")

    def search_product(self):
        product_id = self.enteride.get()
        result = fetch_db_query("SELECT * FROM products WHERE id = ?", (product_id,))
        if result:
            product_name, product_price, product_quantity = result[0][1], result[0][2], result[0][3]
            self.enternamee.delete(0, tk.END)
            self.enternamee.insert(0, product_name)
            self.enterpricee.delete(0, tk.END)
            self.enterpricee.insert(0, product_price)
            self.enterquantitye.delete(0, tk.END)
            self.enterquantitye.insert(0, product_quantity)
        else:
            messagebox.showinfo("Info", "No product found with the given ID.")

    def edit_product(self):
        product_id = self.enteride.get()
        new_product_name = self.enternamee.get()
        new_product_price = self.enterpricee.get()
        new_product_quantity = self.enterquantitye.get()
        if product_id and new_product_name and new_product_price and new_product_quantity:
            try:
                new_product_price = float(new_product_price)
                new_product_quantity = int(new_product_quantity)
                execute_db_query('''
                    UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?
                ''', (new_product_name, new_product_price, new_product_quantity, product_id))
                messagebox.showinfo("Success", "Product updated successfully!")
                self.update_totals()
                self.show_all_products()
            except ValueError:
                messagebox.showerror("Error", "Invalid price or quantity. Please enter valid numbers.")
        else:
            messagebox.showerror("Error", "Please enter all fields.")

    def rename_product(self):
        product_id = self.enteride.get()
        new_product_name = self.enternamee.get()
        if product_id and new_product_name:
            execute_db_query('''
                UPDATE products SET name = ? WHERE id = ?
            ''', (new_product_name, product_id))
            messagebox.showinfo("Success", "Product name updated successfully!")
            self.show_all_products()
        else:
            messagebox.showerror("Error", "Please enter Product ID and new Product Name.")

    def add_to_cart(self):
        product_id = self.enteride.get()
        result = fetch_db_query("SELECT * FROM products WHERE id = ?", (product_id,))
        if result:
            product_name, product_price, product_quantity = result[0][1], result[0][2], result[0][3]
            if product_quantity > 0:
                self.total_price += product_price
                self.update_totals()
                execute_db_query('''
                    INSERT INTO cart (id, name, price, quantity) VALUES (?, ?, ?, ?)
                ''', (product_id, product_name, product_price, 1))
                execute_db_query('''
                    UPDATE products SET quantity = quantity - 1 WHERE id = ?
                ''', (product_id,))
                messagebox.showinfo("Success", "Product added to cart!")
                self.show_all_products()
                self.show_cart()
            else:
                messagebox.showinfo("Info", "Product is out of stock.")
        else:
            messagebox.showinfo("Info", "No product found with the given ID.")

    def remove_from_cart(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            product_id = item_values[0]
            result = fetch_db_query("SELECT * FROM cart WHERE id = ?", (product_id,))
            if result:
                product_price = result[0][2]
                self.total_price -= product_price
                self.update_totals()
                execute_db_query("DELETE FROM cart WHERE id = ?", (product_id,))
                execute_db_query("UPDATE products SET quantity = quantity + 1 WHERE id = ?", (product_id,))
                messagebox.showinfo("Success", "Product removed from cart!")
                self.show_cart()
            else:
                messagebox.showinfo("Info", "Product not found in cart.")

    def generate_bill(self):
        result = fetch_db_query("SELECT * FROM cart")
        if result:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Bill", ln=True, align='C')
            for row in result:
                pdf.cell(200, 10, txt=f"Product ID: {row[0]}, Name: {row[1]}, Price: ${row[2]}", ln=True)
            pdf.cell(200, 10, txt=f"Total Price: ${self.total_price}", ln=True, align='R')
            pdf.output("bill.pdf")
            messagebox.showinfo("Success", "Bill generated successfully!")
        else:
            messagebox.showinfo("Info", "Cart is empty.")

    def show_products(self):
        product_id = self.enteride.get()
        result = fetch_db_query("SELECT * FROM products WHERE id = ?", (product_id,))
        self.tree.delete(*self.tree.get_children())
        if result:
            self.tree.insert('', tk.END, values=result[0])
        else:
            messagebox.showinfo("Info", "No product found with the given ID.")

    def show_all_products(self):
        result = fetch_db_query("SELECT * FROM products")
        self.tree.delete(*self.tree.get_children())
        for row in result:
            self.tree.insert('', tk.END, values=row)

    def show_cart(self):
        result = fetch_db_query("SELECT * FROM cart")
        self.tree.delete(*self.tree.get_children())
        for row in result:
            self.tree.insert('', tk.END, values=row)

    def remove_product(self):
        product_id = self.enteride.get()
        execute_db_query("DELETE FROM products WHERE id = ?", (product_id,))
        messagebox.showinfo("Success", "Product removed successfully!")
        self.show_all_products()

    def exit_app(self):
        self.master.destroy()

    def update_totals(self):
        result = fetch_db_query("SELECT SUM(price) FROM cart")
        self.total_price = result[0][0] if result[0][0] is not None else 0
        self.total_price_label.config(text=f"Total Price: ${self.total_price:.2f}")

# Mainloop
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
