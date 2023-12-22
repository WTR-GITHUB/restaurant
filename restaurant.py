import os
from sqlite import fetch_categories, fetch_food_by_category


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

    def make_categories(self) -> dict:
        return fetch_categories()

    def make_food_by_category(self, mark: int) -> dict:
        return fetch_food_by_category(mark)

    def print_vertical(self) -> None:
        self.read_from_file()
        for line in self.readed_data:
            print(line)
        print("\n")

    def print_category_menu(self, mark: int) -> None:
        new_categories = {}
        for key, value in self.make_categories().items():
            if key == mark:
                value = f"<< {value} >>"
            else:
                value = value
            new_categories[key] = value
        for key, value in new_categories.items():
            print(f"{key}: {value} | ", end="")
        print("\n")

    def print_item_menu(self, mark: int) -> None:
        for key, value in self.make_food_by_category(mark).items():
            print(f"{key}. {value[0]:30}{value[1]} €")
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
        food_menu.print_item_menu(1)
        while True:
            user_key = input().lower()
            if user_key in ["1", "2", "3", "4", "5", "6"]:
                clear_screen()
                food_menu.print_category_menu(mark=int(user_key))
                food_menu.print_item_menu(mark=int(user_key))
            elif user_key == "b":
                clear_screen()
                start_menu.print_vertical()
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
        start_menu.print_vertical()
    else:
        wrong_key = f"You have entered '{user_key}' a bad key, please do better."
        print(wrong_key)
