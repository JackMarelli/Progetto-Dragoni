# Generated by Django 3.2.9 on 2021-12-04 17:48

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
                ('aggiunte', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ProdottoDaVendere',
                'verbose_name_plural': 'ProdottiDaVendere',
            },
        ),
        migrations.CreateModel(
            name='ProdottoOrdinato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prodotto', models.IntegerField(default=0)),
                ('quantita', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'ProdottoOrdinato',
                'verbose_name_plural': 'ProdottiOrdinati',
            },
        ),
        migrations.CreateModel(
            name='Ordine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ketchup', models.IntegerField()),
                ('numero_maionesi', models.IntegerField()),
                ('id_utente', models.IntegerField(default=0)),
                ('stato', models.CharField(blank=True, max_length=25)),
                ('orario', models.TimeField(default=0)),
                ('data', models.DateField(auto_now=True)),
                ('lista_prodotti', models.ManyToManyField(to='ordinibar.ProdottoOrdinato')),
            ],
            options={
                'verbose_name': 'Ordine',
                'verbose_name_plural': 'Ordini',
            },
        ),
    ]