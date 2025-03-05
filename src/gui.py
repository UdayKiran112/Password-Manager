import tkinter as tk
from tkinter import messagebox, simpledialog
from database import save_password, get_password, delete_password
from encryption import encrypt_data, decrypt_data


class PasswordManagerApp:
    def __init__(self, root, key):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x300")
        self.key = key

        # UI Elements
        tk.Label(root, text="Website:").pack()
        self.website_entry = tk.Entry(root)
        self.website_entry.pack()

        tk.Label(root, text="Username:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Password:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Button(root, text="Save", command=self.save_password).pack()
        tk.Button(root, text="Retrieve", command=self.retrieve_password).pack()
        tk.Button(root, text="Delete", command=self.delete_password).pack()

    def save_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not website or not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        encrypted_password = encrypt_data(password, self.key)
        save_password(website, username, encrypted_password)
        messagebox.showinfo("Success", "Password saved successfully!")

    def retrieve_password(self):
        website = simpledialog.askstring("Retrieve Password", "Enter website:")
        if not website:
            return
        result = get_password(website)
        if result:
            username, encrypted_password = result
            password = decrypt_data(encrypted_password, self.key)
            messagebox.showinfo(
                "Retrieved", f"Username: {username}\nPassword: {password}"
            )
        else:
            messagebox.showerror("Error", "No record found!")

    def delete_password(self):
        website = simpledialog.askstring("Delete Password", "Enter website:")
        if not website:
            return
        delete_password(website)
        messagebox.showinfo("Deleted", "Password deleted successfully!")
