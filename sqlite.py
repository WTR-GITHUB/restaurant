import sqlite3

conn = sqlite3.connect("restaurant.db")
c = conn.cursor()


def fetch_categories() -> list:
    c.execute("SELECT Category FROM menu")
    my_dict = {i + 1: item[0] for i, item in enumerate(c)}
    return my_dict


def fetch_food_by_category(mark: int) -> list:
    c.execute("SELECT food_name, price FROM food WHERE id_Category = ?", (mark,))
    my_dict = {i + 1: item for i, item in enumerate(c)}
    return my_dict
