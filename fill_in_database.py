from app import db
from modules import FoodCategory, Food

# Function to add food categories to the database
def add_food_categories():
    categories = ["Snacks", "Soups", "Main dishes", "Desserts", "Drinks"]
    for category in categories:
        existing_category = FoodCategory.query.filter_by(category_name=category).first()
        if not existing_category:
            new_category = FoodCategory(category_name=category)
            db.session.add(new_category)
    db.session.commit()


def add_food():
    food_data = [
        {"food_name": "French fries", "food_price": "2.00", "category_id": 1},
        {"food_name": "Nachos", "food_price": "3.50", "category_id": 1},
        {"food_name": "Chicken winds", "food_price": "4.00", "category_id": 1},
        {"food_name": "Anti pasta", "food_price": "8.00", "category_id": 1},
        {"food_name": "Day soup", "food_price": "1.50", "category_id": 2},
        {"food_name": "Chili soup", "food_price": "4.10", "category_id": 2},
        {"food_name": "Pho soup", "food_price": "7.00", "category_id": 2},
        {"food_name": "Pork ribs", "food_price": "9.00", "category_id": 3},
        {"food_name": "Pork tenderloin", "food_price": "10.00", "category_id": 3},
        {"food_name": "Beef burger", "food_price": "6.50", "category_id": 3},
        {"food_name": "Chicken burger", "food_price": "6.10", "category_id": 3},
        {"food_name": "Pulled pork", "food_price": "6.00", "category_id": 3},
        {"food_name": "Belgian waffle", "food_price": "4.50", "category_id": 4},
        {"food_name": "Chocolate pie", "food_price": "4.20", "category_id": 4},
        {"food_name": "Ice cream", "food_price": "4.30", "category_id": 4},
        {"food_name": "Juice", "food_price": "3.00", "category_id": 5},
        {"food_name": "Water", "food_price": "1.00", "category_id": 5},
        {"food_name": "Kvass", "food_price": "2.70", "category_id": 5},
        {"food_name": "Espresso", "food_price": "2.50", "category_id": 5},
    ]

    for food_item in food_data:
        existing_food = Food.query.filter_by(food_name=food_item['food_name']).first()
        if not existing_food:
            food = Food(**food_item)
            db.session.add(food)
    db.session.commit()


