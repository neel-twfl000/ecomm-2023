# Generated by Django 4.2.4 on 2023-10-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_subcategory_name_alter_subcategory_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='brand',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]