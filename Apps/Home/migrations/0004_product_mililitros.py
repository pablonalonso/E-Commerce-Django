# Generated by Django 4.2.6 on 2023-10-23 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_created_product_actualizado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mililitros',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
