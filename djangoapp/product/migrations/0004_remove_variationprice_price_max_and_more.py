# Generated by Django 4.2.11 on 2024-03-14 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_price_variationprice_price_max_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variationprice',
            name='price_max',
        ),
        migrations.RemoveField(
            model_name='variationprice',
            name='price_min',
        ),
        migrations.AddField(
            model_name='variationprice',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variationprice',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_variations', to='product.product'),
        ),
    ]