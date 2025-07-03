def login():
    print("----- Login -----")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open("users.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) != 2:
                    continue  # skip invalid lines
                user, pwd = data
                if user == username and pwd == password:
                    print(f"Welcome {username}! You have successfully logged in to the Library Management System.")
                    return True
        print("Invalid username or password.")
        return False
    except FileNotFoundError:
        print("User database not found. Please sign up first.")
        return False
