# Generated by Django 4.2 on 2024-11-03 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.FloatField(),
        ),
    ]