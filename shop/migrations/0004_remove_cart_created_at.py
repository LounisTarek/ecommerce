# Generated by Django 3.2 on 2023-04-12 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_at',
        ),
    ]
