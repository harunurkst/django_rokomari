# Generated by Django 2.0.3 on 2020-08-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('in_stock', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('size', models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L')], max_length=5)),
                ('color', models.CharField(choices=[('red', 'Red'), ('white', 'White'), ('black', 'Black')], max_length=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='Writer',
        ),
    ]
