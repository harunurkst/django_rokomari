# Generated by Django 2.0.3 on 2020-08-24 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_carditem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='carditem',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Cart'),
            preserve_default=False,
        ),
    ]