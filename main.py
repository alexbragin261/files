# from pprint import pprint

with open('recipes.txt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredient_count = int(file.readline())
        ingredients = []
        for i in range(ingredient_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients
# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish, ingrid in cook_book.items():
        if dish in dishes:
            for j in ingrid:
                j['quantity'] = int(j.get('quantity')) * person_count
                if j['ingredient_name'] not in shop_list:
                    shop_list[j.get('ingredient_name')] = j
                    j.pop('ingredient_name')
                else:
                    j['quantity'] = int(j.get('quantity')) + int(j.get('quantity'))
                    shop_list[j.get('ingredient_name')] = j
                    j.pop('ingredient_name')
    return shop_list


print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2))

