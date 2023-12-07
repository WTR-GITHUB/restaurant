import os

meniu_text = f"""Welcome to our restaurant:

Enter '1' to get info about us.
Enter '2' to see menu and order.
Enter '3' for table reservations and administration.
Enter '4' pay and make it happen.
Enter 'q' to exit program.
"""
wrong_key = ""


while True:
    print(meniu_text)
    user_key = input()

    if user_key == "q":
        os.system("cls||clear")
        exit()
    elif user_key == "1":
        os.system("cls||clear")
        print("This will be information about us")
    elif user_key == "2":
        os.system("cls||clear")
        print("This will be food menu and order information")
    elif user_key == "3":
        os.system("cls||clear")
        print("This will be table order and administration")
    elif user_key == "4":
        os.system("cls||clear")
        print("Pay and go")
    else:
        wrong_key = f"You have entered '{user_key}' a bad key, please do better."
        print(wrong_key)
