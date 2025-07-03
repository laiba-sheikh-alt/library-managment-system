import os
from signup import sign_up
from login import login
from books import add_book, view_books
from issue_return import issue_book, return_book

def print_banner():
    print("\n" + "*" * 44)
    print("      WELCOME TO THE LIBRARY SYSTEM      ")
    print("*" * 44 + "\n")

def main_menu():
    while True:
        print("\n----- Main Menu -----")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        os.system('cls')  # clear screen (Windows)
        print_banner()
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            if login():
                os.system('cls')
                main_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
