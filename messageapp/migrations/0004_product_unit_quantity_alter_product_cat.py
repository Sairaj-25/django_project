# Generated by Django 5.0 on 2024-02-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0003_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit_quantity',
            field=models.CharField(default=0, max_length=40, verbose_name='unit_quantity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Fruits'), (2, 'Vegetables'), (3, 'Dairy Products'), (4, 'Groceries'), (5, 'All')], verbose_name='category'),
        ),
    ]