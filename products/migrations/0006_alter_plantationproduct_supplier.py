# Generated by Django 4.2.6 on 2023-10-30 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
        ('products', '0005_plantationproduct_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantationproduct',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='suppliers.plantationsupplier'),
        ),
    ]