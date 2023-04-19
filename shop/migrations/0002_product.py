# Generated by Django 3.2 on 2023-04-06 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(blank=True, upload_to='')),
                ('descreption', models.TextField(max_length=190)),
                ('quantity', models.IntegerField()),
                ('trending', models.BooleanField(default=False, help_text='0-default, 1-trending')),
                ('price', models.FloatField()),
                ('tag', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
