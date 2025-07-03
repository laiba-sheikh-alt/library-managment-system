def add_book():
    print("----- Add Book -----")
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    category = input("Enter Category (book/magazine/article): ").strip().lower()

    if category not in ["book", "magazine", "article"]:
        print("Invalid category. Must be 'book', 'magazine' or 'article'.")
        return

    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},available,{category}\n")
    print("Book added successfully.")

def view_books():
    while True:
        print("\n----- View Books -----")
        print("1. View All Books")
        print("2. View by Alphabet (A-Z)")
        print("3. View Most Famous Books")
        print("4. View Magazines")
        print("5. View Articles")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_books()
        elif choice == "2":
            view_by_alphabet()
        elif choice == "3":
            view_famous_books()
        elif choice == "4":
            view_category("magazine")
        elif choice == "5":
            view_category("article")
        elif choice == "6":
            break
        else:
            print("Invalid option. Try again.")



def show_all_books():
    try:
        with open("books.txt", "r") as f:
            for line in f:
                book_id, title, author, status, category = line.strip().split(",")
                print(f"ID: {book_id} | Title: {title} | Author: {author} | Status: {status} | Category: {category}")
    except FileNotFoundError:
        print("No books found.")
        
        

def view_by_alphabet():
    letter = input("Enter an alphabet (A-Z): ").strip().upper()
    found = False
    try:
        with open("books.txt", "r") as f:
            for line in f:
                book_id, title, author, status, category = line.strip().split(",")
                if title.upper().startswith(letter):
                    print(f"ID: {book_id} | Title: {title} | Author: {author} | Status: {status} | Category: {category}")
                    found = True
        if not found:
            print(f"No books starting with '{letter}' found.")
    except FileNotFoundError:
        print("No books found.")
        
        

def view_famous_books():
    print("----- Most Famous Books -----")
    famous_titles = ["Atomic Habits", "The Alchemist", "Harry Potter", "Rich Dad Poor Dad"]
    try:
        with open("books.txt", "r") as f:
            for line in f:
                book_id, title, author, status, category = line.strip().split(",")
                if title in famous_titles:
                    print(f"⭐ {title} by {author} (Status: {status})")
    except FileNotFoundError:
        print("No books found.")
        
        

def view_category(category_name):
    print(f"----- {category_name.capitalize()}s -----")
    try:
        with open("books.txt", "r") as f:
            for line in f:
                book_id, title, author, status, category = line.strip().split(",")
                if category.lower() == category_name.lower():
                    print(f"{title} by {author} | Status: {status}")
    except FileNotFoundError:
        print("No books found.")
