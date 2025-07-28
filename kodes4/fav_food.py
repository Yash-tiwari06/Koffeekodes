favorite_foods = ("pizza", "maggiie", "burger", "chai", "pasta")
print(favorite_foods)
def food_list(*foods):
    for food in foods:
        print(food)
    return foods
ff_foods = food_list("pizza", "maggiie", "burger", "chai", "pasta")