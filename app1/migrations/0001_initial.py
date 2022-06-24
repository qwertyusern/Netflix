# Generated by Django 4.0.5 on 2022-06-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aktyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=120)),
                ('mamlakat', models.CharField(max_length=120)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('ayol', 'ayol')], max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('yil', models.DateField()),
                ('janr', models.CharField(choices=[('fantastika', 'fantastika'), ('badiy', 'badiy'), ('hujjatli', 'hujjatli')], max_length=120)),
                ('aktyorlar', models.ManyToManyField(to='app1.aktyor')),
            ],
        ),
    ]
