import os

def print_from_file(file_name: str, start_sign: str, end_sign: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        is_between_signs = False
    
        for line in file:
            if start_sign in line:
                is_between_signs = True
                continue
            elif end_sign in line:
                is_between_signs = False
                break
            
            if is_between_signs:
                print(line.strip())

wrong_key = ""

os.system("cls||clear")
print_from_file(file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>")

while True:

    user_key = input().lower()

    if user_key == "q":
        os.system("cls||clear")
        exit()
    elif user_key == "1":
        os.system("cls||clear")
        print_from_file("test.txt", "<<2>>", "<<3>>")
    elif user_key == "2":
        os.system("cls||clear")
        print("This will be food menu and order information")
    elif user_key == "3":
        os.system("cls||clear")
        print("This will be table order and administration")
    elif user_key == "4":
        os.system("cls||clear")
        print("Pay and go")
    elif user_key == "b":
        os.system("cls||clear")
        print_from_file(file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>")
    else:
        wrong_key = f"You have entered '{user_key}' a bad key, please do better."
        print(wrong_key)