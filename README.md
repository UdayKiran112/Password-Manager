# Password Manager

A secure password manager built with Flask and a basic GUI version using Tkinter. It allows users to store, retrieve, and manage their passwords securely with encryption.

## Features

- **Master Password Authentication**: Secure access with a master password.
- **Encryption**: Stored passwords are encrypted for security.
- **Web Interface**: Manage passwords via a Flask-based web UI.
- **Basic GUI Version**: Tkinter-based desktop version.
- **CRUD Operations**: Create, Read, Update, and Delete passwords.

---

## Installation & Setup

### Prerequisites

Ensure you have Python 3 installed along with `pip`.

### Step 1: Clone the Repository

```bash
git clone https://github.com/UdayKiran112/Password-Manager.git
cd Password-Manager
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Master Password

```bash
cd "Flask app"  # Navigate to the Flask app directory
python set_master.py  # Set the master password
```

This will create `data/master_password.txt`, storing the hashed master password.

### Step 4: Initialize the Database

```bash
python database.py  # Creates 'passwords.db' inside 'data/'
```

---

## Running the Application

### Flask Web App

To start the web-based password manager:

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### Basic GUI Version

To run the Tkinter-based version:

```bash
cd "Basic GUI"
python main.py
```

---

## Security Measures

- **Encryption**: Passwords are encrypted before being stored.
- **Hashing**: The master password is securely hashed.
- **Session Handling**: Secure authentication with session management.

---

## Contributing

Feel free to fork this repository and submit a pull request with improvements!

## License

This project is licensed under the MIT License.
