# Задача 1. Заполнить недостающие поля товара
from pprint import pprint

product = {
    "title": "Lavazza Oro",
    "price": 850,
    "weight": 250
}

default_fields = {
    "category": "Без категории",
    "is_active": True,
    "discount": 0
}

# Нужно проверить, есть ли в product все ключи из default_fields.
# Если ключа нет — добавить его со значением по умолчанию.

for key in default_fields.keys():
    if key not in product:
        product[key] = None

pprint(product)
# Задача 2. Посчитать итоговую стоимость корзины
prices = {
    "coffee": 850,
    "milk": 120,
    "bread": 70
}

cart = {
    "coffee": 2,
    "milk": 1,
    "chocolate": 3
}
# Если товара из корзины нет в prices, вывести: Нет цены для товара: chocolate
# И не учитывать его в сумме.
#
# Ожидаемый вывод:
#
# Нет цены для товара: chocolate
# Итого: 1820

################ _____Решение_____
sum = 0

for key in cart:
    if key in prices:
        sum += prices[key] * cart[key]
    else:
        print(f'Нет цены для товара: {key}')

print(f'Итого: {sum}')
######################################
# Задача 3. Обновить профиль пользователя
from pprint import pprint

profile = {
    "name": "Alex",
    "age": 17,
    "city": "Moscow",
    "email": None
}

new_data = {
    "age": 18,
    "email": "alex@gmail.com",
    "phone": "+79990001122"
}
# Нужно обновить profile данными из new_data, но только если такой ключ уже есть в profile
# То есть:
# age обновить
# email обновить
# phone не добавлять, потому что такого ключа нет в profil

############## ___________Решение __________

for key in new_data:
    profile[key] = new_data[key]

pprint(profile)

###############################################
############## ___________Решение __________

for key in new_data:
    if key in profile:
        profile[key] = new_data[key]

pprint(profile)

###############################################