# Generated by Django 3.2.8 on 2021-11-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinibar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordine',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]