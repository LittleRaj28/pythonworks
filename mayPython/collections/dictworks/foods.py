items = [
    {"name": "biriyani", "price": 130, "category": "nonveg"},
    {"name": "dosa", "price": 70, "category": "veg"},
    {"name": "vegfriedrice", "price": 130, "category": "veg"},
    {"name": "noodles", "price": 130, "category": "nonveg"},
    {"name": "burger", "price": 130, "category": "nonveg"},

]
#print all items

item_menu =list(map(lambda it:it.get("name"),items))
print(item_menu)


item_foods = [it.get("name")for it in items]
print(item_foods)

#print price of all items


item_price = list(map(lambda it:it.get("price"),items))
print(item_price)

list_price = [it.get("price")for it in items]
print(list_price)

#veg

item_veg =list(filter(lambda it:it.get("category")=="veg",items))
print(item_veg)

list_veg = [it.get("name")for it in items if it.get("category")=="veg"]
print(list_veg)

