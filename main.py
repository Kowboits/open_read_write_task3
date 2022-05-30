import pprint
with open('recipes.txt',encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        products = []
        dish = line
        lines_number = int(file.readline())
        for i in range(lines_number):
            ingri_list = file.readline().strip().split('|')
            products.append({'ingredient_name' : ingri_list[0], 'quantity': int(ingri_list[1]), 'measure' : ingri_list[2]})
        cook_book[dish.strip()] = products
        file.readline()
    # print(products)
    # pprint.pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count=1):
    shop_list = {}
    for dish in dishes:
        ingridients = cook_book.get(dish)
        for ingridient in range(len(ingridients)):
            new_key = ingridients[ingridient]['ingredient_name']
            # new_dict = ingridients[ingridient].copy()
            # del new_dict['ingredient_name']
            if new_key in shop_list.keys():
                shop_list[new_key] = {'quantity' : ingridients[ingridient]['quantity'] + shop_list[new_key]['quantity'],'measure' : shop_list[new_key]['measure']}
            else:
                shop_list[new_key] = {'quantity' : ingridients[ingridient]['quantity'], 'measure' : ingridients[ingridient]['measure']}
    if person_count > 1:
        for dish in shop_list.keys():
            shop_list[dish] = {'quantity' : shop_list[dish]['quantity'] * person_count, 'measure' : shop_list[dish]['measure']}

    return shop_list
pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
