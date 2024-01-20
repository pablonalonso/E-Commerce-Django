# Generated by Django 4.2.6 on 2023-10-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_alter_product_mililitros'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(default='default_image.jpg', max_length=300, null=True, upload_to='images'),
        ),
    ]