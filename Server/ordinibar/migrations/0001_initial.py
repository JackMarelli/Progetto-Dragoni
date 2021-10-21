# Generated by Django 3.2.8 on 2021-10-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdottoDaVendere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('prezzo', models.FloatField(default=0.0)),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'ProdottoDaVendere',
                'verbose_name_plural': 'ProdottiDaVendere',
            },
        ),
    ]
