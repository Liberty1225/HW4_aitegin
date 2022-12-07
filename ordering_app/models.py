from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = 'hashed_password'
        super().save(*args, **kwargs)
        print(f'Пользователь {self.email} сохранен')

    def __str__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name="ФИО")
    card_number = models.CharField(max_length=16, verbose_name="Номер карточки")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=20, verbose_name="ФИО")
    position = models.CharField(max_length=20, verbose_name="Должность")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}  в должности {self.position}'


class Ingredient(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование ингредиента")
    extra_price = models.IntegerField(verbose_name='Надбавка стоимости')

    class Meta:
        db_table = 'ingredients'
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование блюда")
    start_price = models.IntegerField(verbose_name='Начальная стоимость')
    ingredients = models.ManyToManyField(Ingredient, through='Order')

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client.name} - {self.order_date_time}'
