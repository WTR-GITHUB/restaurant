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


def print_category_menu(categories: list, mark: int) -> None:
    new_categories = []
    for index, category in enumerate(categories):
        if index == mark:
            category = f"<< {category} >>"
        else:
            category = category

        new_categories.append(category)

    print(*new_categories, sep=" | ")
    print("\n")


def print_item_menu(food_dict: dict) -> None:
    for key, value in food_dict.items():
        print(f"{key:30}{value} €")
    print("\n")


wrong_key = ""

categories = [
    "1. Snacks",
    "2. Soups",
    "3. Salad",
    "4. Burgers with fries",
    "5. Main dishes",
    "6. For kids",
]
snacks = {
    "French fries": 3,
    "Fried sweet potatoes": 5,
    "Fried bread": 4,
    "Nachos": 6,
    "Prawns pil pil": 8,
    "Beef carpaccio": 8,
    "Chicken wing": 6,
}

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
        print_category_menu(categories=categories, mark=0)
        print_item_menu(snacks)
        while True:
            user_key = input().lower()
            if user_key == "1":
                os.system("cls||clear")
                print_category_menu(categories=categories, mark=0)
                print_item_menu(snacks)
            elif user_key == "2":
                os.system("cls||clear")
                print_category_menu(categories=categories, mark=1)
            elif user_key == "3":
                os.system("cls||clear")
                print_category_menu(categories=categories, mark=2)
            elif user_key == "4":
                os.system("cls||clear")
                print_category_menu(categories=categories, mark=3)
            elif user_key == "5":
                os.system("cls||clear")
                print_category_menu(categories=categories, mark=4)
            elif user_key == "6":
                os.system("cls||clear")
                print_category_menu(categories=categories, mark=5)
            elif user_key == "b":
                os.system("cls||clear")
                print_from_file(
                    file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>"
                )
                break

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
