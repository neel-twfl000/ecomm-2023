# Generated by Django 4.2.4 on 2023-10-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_product_description_dealsoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealsoffer',
            name='off_rate',
            field=models.FloatField(default=0),
        ),
    ]
