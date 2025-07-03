# library-managment-system
This is a Python-based Library Management System that runs in the command-line interface (CLI). 
### 📝 Description

This is a **Command-Line Interface (CLI)** based Library Management System developed in Python. It allows users to sign up, log in, add/view books, and issue or return them. The system stores data using **text files** — no database required.

It’s organized into separate Python files for better modularity and reusability.

---

### 🚀 Features

- 🔐 **User Authentication**
  - Sign Up with unique username and 8-character password
  - Secure Login with validation

- 📖 **Book Management**
  - Add books, magazines, or articles
  - View all books or filter:
    - A–Z by title
    - By category (book/magazine/article)
    - Popular titles like *Atomic Habits*, *Harry Potter*, etc.

- 📦 **Issuing & Returning**
  - Issue available books to users
  - Return issued books with proper status update

---

### 🗂️ File Structure

```bash
library-management-cli/
│
├── main.py             # Entry point
├── signup.py           # Sign up logic
├── login.py            # Login logic
├── books.py            # Add/View books
├── issue_return.py     # Issue and return functionality
├── users.txt           # Stores usernames & passwords
├── books.txt           # Stores book records
└── issued.txt          # Tracks issued books

