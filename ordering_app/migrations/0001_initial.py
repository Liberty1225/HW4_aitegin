# Generated by Django 3.2 on 2022-12-07 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='ФИО')),
                ('card_number', models.IntegerField(max_length=16, verbose_name='Номер карточки')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование блюда')),
                ('start_price', models.IntegerField(verbose_name='Начальная стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование ингредиента')),
                ('extra_price', models.IntegerField(verbose_name='Надбавка стоимости')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='ФИО')),
                ('position', models.CharField(max_length=20, verbose_name='Должность')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ordering_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date_time', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordering_app.client')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordering_app.food')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordering_app.ingredient')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordering_app.worker')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ordering_app.user'),
        ),
    ]
