from auth import check_master_password
from gui import PasswordManagerApp
import tkinter as tk

# Authenticate user
key = check_master_password()

# Initialize GUI
root = tk.Tk()
app = PasswordManagerApp(root, key)
root.mainloop()
