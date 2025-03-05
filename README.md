# Password Manager 🔐

A **secure password manager** with **AES-GCM encryption**, **master password authentication**, and a **Tkinter GUI**. It securely stores credentials in an **SQLite database** and allows users to **save, retrieve, and delete passwords** easily.

## Features 🚀

- **AES-GCM Encryption** for strong security
- **Master Password Authentication** (PBKDF2 hashing)
- **SQLite Database** for storing encrypted passwords
- **User-friendly GUI** (Tkinter)
- **Password Management** (Save, Retrieve, Delete)

## Installation ⚙️

```bash
pip install -r requirements.txt
```

## Usage ▶️

```bash
python main.py
```

## File Structure 📂

```
PasswordManager/
│── main.py                   # Entry point to launch the app
│── database.py                # Handles SQLite database operations
│── encryption.py              # Encrypts & decrypts passwords (AES-GCM)
│── auth.py                    # Manages master password authentication
│── gui.py                     # Tkinter GUI for user interaction
│── config.py                  # Stores encryption & database settings
│── requirements.txt           # Required dependencies
│── README.md                  # Project documentation
│── data/                      # Stores encrypted database (passwords.db)
│── assets/                    # Icons, images, or other resources
```

## Security Notice ⚠️

- The **master password must be strong** to ensure security.
- All passwords are **AES-GCM encrypted** before being stored.
- **Never share your master password** with anyone!

## License 📜

This project is open-source. Feel free to contribute! 🚀
