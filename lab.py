class Menu:
    def __init__(self, file_name: str, start_sign: str, end_sign: str) -> None:
        self.file_name = file_name
        self.start_sign = start_sign
        self.end_sign = end_sign
        self.readed_data = None

    def print_from_file(self) -> "Menu":
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


menu_1 = Menu(file_name="test.txt", start_sign="<<3>>", end_sign="<<4>>")
menu_1.print_from_file().make_categories()
print(menu_1.readed_data)
print(menu_1.category_dict)

import sqlite3

conn = sqlite3.connect("restaurant.db")
c = conn.cursor()

query = [(category,) for category in tuple(menu_1.readed_data)]
print(query)

with conn:
    c.executemany("INSERT INTO menu (category) VALUES (?);", query)
