# Generated by Django 4.1.7 on 2023-04-26 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0004_order_quantity_order_service_alter_order_order_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'verbose_name': 'Car Model', 'verbose_name_plural': 'Car Models'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='serviceprice',
            options={'verbose_name': 'Service Price', 'verbose_name_plural': 'Service Prices'},
        ),
    ]
