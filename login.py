import tkinter as tk
from tkinter import messagebox, PhotoImage

class LoginApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Application")
        self.master.geometry("400x500")
        self.master.config(bg="black")  # Set background color to black

        self.login_successful = False

        self.name = "Marvel"
        self.pas = "3434"

        self.create_widgets()

    def create_widgets(self):
        # Load image
        self.image = PhotoImage(file=r"C:\Users\THIRUPATHI\Pictures\Camera Roll\dhana.png")  # Replace with the path to your image
        self.image_label = tk.Label(self.master, image=self.image, bg="black")
        self.image_label.pack(pady=10)

        # Title label for university
        self.uni_title_label = tk.Label(self.master, text="AURORA Deemed to be University", font=("Arial", 18, "bold"), bg="black", fg="cyan")
        self.uni_title_label.pack(pady=10)

        # Title label for login
        self.title_label = tk.Label(self.master, text="MARVEL STORE LOGIN", font=("Arial", 20, "bold"), bg="black", fg="magenta")
        self.title_label.pack(pady=10)

        # Username label and entry
        self.username_label = tk.Label(self.master, text="Username:", font=("Arial", 14), bg="black", fg="white")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Arial", 14), bg="white", fg="black")
        self.username_entry.pack(pady=5)

        # Password label and entry
        self.password_label = tk.Label(self.master, text="Password:", font=("Arial", 14), bg="black", fg="white")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 14), bg="white", fg="black")
        self.password_entry.pack(pady=5)

        # Login button
        self.login_button = tk.Button(self.master, text="Login", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        name1 = self.username_entry.get()
        pas1 = self.password_entry.get()

        if name1 == self.name and pas1 == self.pas:
            messagebox.showinfo("Login Success", "Welcome to MARVEL STORE")
            self.login_successful = True
            self.master.destroy()  # Close the login window
        else:
            messagebox.showinfo("Error", "Enter the details correctly or fill all the details")
            self.username_entry.delete(0, tk.END)  # Clear username field
            self.password_entry.delete(0, tk.END)  # Clear password field

# Main code to run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = LoginApplication(root)
    root.mainloop()
