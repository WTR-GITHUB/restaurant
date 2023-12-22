import os
from sqlite import fetch_categories

def clear_screen():
    os.system("cls||clear")


class Menu:
    def __init__(self, file_name: str, start_sign: str, end_sign: str) -> None:
        self.file_name = file_name
        self.start_sign = start_sign
        self.end_sign = end_sign
        self.readed_data = None

    def read_from_file(self) -> "Menu":
        self.readed_data = []
        with open(self.file_name, "r", encoding="utf-8") as file:
            is_between_signs = False
            for line in file:
                if self.start_sign in line:
                    is_between_signs = True
                    continue
                elif self.end_sign in line:
                    is_between_signs = False
                    break

                if is_between_signs:
                    self.readed_data.append(line.strip())
        return self

    def make_categories(self) -> "Menu":
        self.category_dict = {i + 1: item for i, item in enumerate(self.readed_data)}
        return self

    def print_vertical(self) -> None:
        self.read_from_file()
        for line in self.readed_data:
            print(line)

    def print_category_menu(self, mark: int) -> None:
        self.read_from_file()
        self.make_categories()
        new_categories = []
        for key, value in self.category_dict.items():
            if key == mark:
                value = f"<< {value} >>"
            else:
                value = value
            new_categories.append(value)
        print(*new_categories, sep=" | ")
        print("\n")

    def print_item_menu(self) -> None:
        self.make_categories()
        for key, value in self.category_dict.items():
            print(f"{key:30}{value} €")
        print("\n")


start_menu = Menu(file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>")
about_us = Menu("test.txt", "<<2>>", "<<3>>")
food_menu = Menu("test.txt", "<<3>>", "<<4>>")


wrong_key = ""

clear_screen()

start_menu.print_vertical()

while True:
    user_key = input().lower()
    if user_key == "q":
        clear_screen()
        exit()
    elif user_key == "1":
        clear_screen()
        about_us.print_vertical()
    elif user_key == "2":
        clear_screen()
        food_menu.print_category_menu(mark=1)
        while True:
            user_key = input().lower()
            food_menu.print_item_menu()
            if user_key in ["1", "2", "3", "4", "5", "6"]:
                clear_screen()
                food_menu.print_category_menu(mark=int(user_key))
                food_menu.print_item_menu()
            elif user_key == "b":
                clear_screen()
                start_menu.print_vertical()
                break
            else:
                wrong_key = (
                    f"You have entered '{user_key}' a bad key, please do better."
                )
                print(wrong_key)

#     elif user_key == "3":
#         clear_screen()
#         print("This will be table order and administration")
#     elif user_key == "4":
#         clear_screen()
#         print("Pay and go")
#     elif user_key == "b":
#         clear_screen()
#         print_from_file(file_name="test.txt", start_sign="<<1>>", end_sign="<<2>>")
#     else:
#         wrong_key = f"You have entered '{user_key}' a bad key, please do better."
#         print(wrong_key)
