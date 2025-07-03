def sign_up():
    print("----- Sign Up -----")
    username = input("Enter a username: ")
    password = input("Enter an 8-character password: ")

    if len(password) != 8:
        print("Password must be exactly 8 characters.")
        return

    # Check if username already exists
    try:
        with open("users.txt", "r") as f:
            for line in f:
                existing_user = line.strip().split(",")[0]
                if existing_user == username:
                    print("Username already exists. Try another.")
                    return
    except FileNotFoundError:
        pass  # File doesn't exist, first user will be created

    # Save user
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Sign up successful! You can now login.")
