# Generated by Django 4.1.7 on 2023-03-16 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('applied', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата регистрации')),
            ],
        ),
    ]