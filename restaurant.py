import os


def clear_screen():
    os.system("cls||clear")


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


def print_category_menu(categories: dict, mark: int) -> None:
    new_categories = []
    for key, value in categories.items():
        if key == mark:
            value = f"<< {value} >>"
        else:
            value = value
        new_categories.append(value)
    print(*new_categories, sep=" | ")
    print("\n")


def print_item_menu(food_dict: dict) -> None:
    for key, value in food_dict.items():
        print(f"{key:30}{value} €")
    print("\n")


wrong_key = ""

categories = {
    1: "1. Snacks",
    2: "2. Soups",
    3: "3. Salad",
    4: "4. Burgers with fries",
    5: "5. Main dishes",
    6: "6. For kids",
}
snacks = {
    "French fries": 3,
    "Fried sweet potatoes": 5,
    "Fried bread": 4,
    "Nachos": 6,
    "Prawns pil pil": 8,
    "Beef carpaccio": 8,
    "Chicken wing": 6,
}

clear_screen()

print_from_file(file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>")

while True:
    user_key = input().lower()
    if user_key == "q":
        clear_screen()
        exit()
    elif user_key == "1":
        clear_screen()
        print_from_file("test.txt", "<<2>>", "<<3>>")
    elif user_key == "2":
        clear_screen()
        print_category_menu(categories=categories, mark=1)
        print_item_menu(snacks)

        while True:
            user_key = input().lower()
            if user_key in ["1", "2", "3", "4", "5", "6"]:
                clear_screen()
                print_category_menu(categories=categories, mark=int(user_key))
                print_item_menu(snacks)
            elif user_key == "b":
                clear_screen()
                print_from_file(
                    file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>"
                )
                break
            else:
                wrong_key = (
                    f"You have entered '{user_key}' a bad key, please do better."
                )
                print(wrong_key)

    elif user_key == "3":
        clear_screen()
        print("This will be table order and administration")
    elif user_key == "4":
        clear_screen()
        print("Pay and go")
    elif user_key == "b":
        clear_screen()
        print_from_file(file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>")
    else:
        wrong_key = f"You have entered '{user_key}' a bad key, please do better."
        print(wrong_key)
