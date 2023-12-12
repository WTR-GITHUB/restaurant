import os

def clear_screen():
    os.system("cls||clear")

def print_category_menu(categories, mark):
    # Your implementation for printing category menu

def print_item_menu(items):
    # Your implementation for printing item menu

def print_from_file(file_name, start_sign, end_sign):
    # Your implementation for printing from file

while True:
    user_key = input().lower()
    
    if user_key == "1":
        clear_screen()
        print_category_menu(categories=categories, mark=0)
        print_item_menu(snacks)
    elif user_key in ["2", "3", "4", "5", "6"]:
        clear_screen()
        print_category_menu(categories=categories, mark=int(user_key) - 2)
    elif user_key == "b":
        clear_screen()
        print_from_file(
            file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>"
        )
        break


categories = {
    0: "Category 1",
    1: "Category 2",
    2: "Category 3",
    3: "Category 4",
    4: "Category 5",
    5: "Category 6",
}

# Usage
category_mark = int(user_key) - 2
print_category_menu(categories=categories, mark=category_mark)


while True:
    try:
        user_key = input().lower()

        if user_key == "1":
            clear_screen()
            print_category_menu(categories=categories, mark=0)
            print_item_menu(snacks)
        elif user_key in ["2", "3", "4", "5", "6"]:
            clear_screen()
            print_category_menu(categories=categories, mark=int(user_key) - 2)
        elif user_key == "b":
            clear_screen()
            print_from_file(
                file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>"
            )
            break
        else:
            print("Invalid input. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a valid option.")
