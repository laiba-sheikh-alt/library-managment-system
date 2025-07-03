def issue_book():
    print("----- Issue Book -----")
    book_id = input("Enter Book ID to issue: ").strip()
    user = input("Enter your username: ").strip()

    books = []
    issued = False

    with open("books.txt", "r") as f:
        for line in f:
            book = line.strip().split(",")
            if book[0] == book_id and book[3] == "available":
                book[3] = "issued"
                issued = True
                with open("issued.txt", "a") as i:
                    i.write(f"{book_id},{user}\n")
            books.append(book)

    with open("books.txt", "w") as f:
        for book in books:
            f.write(",".join(book) + "\n")

    if issued:
        print("Book issued successfully.")
    else:
        print("Book not available or does not exist.")

def return_book():
    print("----- Return Book -----")
    book_id = input("Enter Book ID to return: ").strip()
    user = input("Enter your username: ").strip()

    books = []
    returned = False

    with open("books.txt", "r") as f:
        for line in f:
            book = line.strip().split(",")
            if book[0] == book_id and book[3] == "issued":
                book[3] = "available"
                returned = True
            books.append(book)

    with open("books.txt", "w") as f:
        for book in books:
            f.write(",".join(book) + "\n")

    if returned:
        with open("issued.txt", "r") as i:
            lines = i.readlines()
        with open("issued.txt", "w") as i:
            for line in lines:
                if not (book_id in line and user in line):
                    i.write(line)
        print("Book returned successfully.")
    else:
        print("Invalid return request.")
