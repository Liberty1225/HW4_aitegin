from ordering_app.models import *

# User.objects.create(email='nikname21@gmail.com', password='defender42')

client_1 = Client(
    user=User.objects.create(
        email='nikname21@gmail.com',
        password='defender42',
    ),
    name='Азат Соколов',
    card_number='4147 5657 9878 9009',
)
client_1.save()


# User.objects.create(email='altywa1998@gmail.com', password='nono34')

worker_1 = Worker(
    user=User.objects.create(
        email='altywa1998@gmail.com',
        password='nono34',
    ),
    name='Алтынай Алиева',
    position='Оператор',
)
worker_1.save()

food_1 = Food(name='Шаурма', start_price=50)
food_1.save()
food_2 = Food(name='Гамбургер', start_price=25)
food_2.save()
ingredient_1 = Ingredient(name='Сыр', extra_price=10)
ingredient_1.save()
ingredient_2 = Ingredient(name='Курица', extra_price=70)
ingredient_2.save()
ingredient_3 = Ingredient(name='Говядина', extra_price=80)
ingredient_3.save()
ingredient_4 = Ingredient(name='Салат', extra_price=15)
ingredient_4.save()
ingredient_5 = Ingredient(name='Фри', extra_price=15)
ingredient_5.save()

order_1 = food_1.ingredients.set([ingredient_1, ingredient_3, ingredient_4, ingredient_5],
                                 through_defaults={'client': client_1, 'worker': worker_1})
print(order_1)
order_2 = food_2.ingredients.set([ingredient_2, ingredient_4],
                                 through_defaults={'client': client_1, 'worker': worker_1})
print(order_2)

sum_1 = food_1.start_price + ingredient_1.extra_price + ingredient_3.extra_price \
        + ingredient_4.extra_price + ingredient_5.extra_price
print(sum_1)
sum_2 = food_2.start_price + ingredient_2.extra_price + ingredient_4.extra_price
print(sum_2)
sum_total = sum_1 + sum_2
print(sum_total)












# order_1 = Order.objects.create(
#     client=client_1,
#     worker=worker_1,
#     food=food_1,
#     ingredient=([ingredient_1, ingredient_3, ingredient_4, ingredient_5,]),
#     )
# order_1.save()
#
#
# order_2 = Order.objects.create(
#     client=client_1,
#     worker=worker_1,
#     food=food_2,
#     ingredient=([ingredient_2, ingredient_4]),
# )
# order_2.save()

