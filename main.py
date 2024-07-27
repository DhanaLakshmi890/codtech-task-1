# main.py
import tkinter as tk
from INVENTORY import Application
from database import database
from login import LoginApplication

def main():
    # Initialize database
    database()

    # Create the login window
    mw = tk.Tk()
    login_app = LoginApplication(mw)
    mw.mainloop()  # Start the Tkinter event loop for the login window

    # Check if login was successful before opening the main application window
    if login_app.login_successful:
        root = tk.Tk()
        app = Application(root)
        root.mainloop()  # Start the Tkinter event loop for the main application

if __name__ == "__main__":
    main()
