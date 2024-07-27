Name: J DHANALAKSHMI,
Company: CODTECT IT SOLUTIONS
ID:CT8PP1286
Duration: JUNE 20th,2024 to AUGUST 20th, 2024.

Project Overview
Components

Main Module (main.py)


This is the entry point of the application.
It initializes the database and manages the flow between the login window and the main application window.
Database Module (database.py)

Responsible for setting up and managing the database.
Ensures that all necessary tables and data structures are in place for the application to function correctly.
Login Module (login.py)

Handles user authentication.
Displays a login window where users can enter their credentials.
Verifies user credentials and sets a flag (login_successful) if the login is successful.
Inventory Module (INVENTORY.py)

Contains the main application logic for the inventory management system.
Provides a user interface for managing inventory items (e.g., adding, updating, deleting items).
Workflow
Initialization

The main() function is called, which initializes the database by calling the database() function from the database.py module.
Login Process

A Tkinter window (mw) is created for the login process.
An instance of LoginApplication is created, which handles the login logic and interface.
The Tkinter event loop (mw.mainloop()) starts, allowing the user to interact with the login window.
Post-Login

After the login window is closed, the application checks if the login was successful (login_app.login_successful).
If the login was successful, a new Tkinter window (root) is created for the main application.
An instance of Application is created, which contains the main inventory management interface and logic.
The Tkinter event loop (root.mainloop()) starts, allowing the user to interact with the inventory management system.
