# Generated by Django 3.2.9 on 2021-11-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.TextField(),
        ),
    ]