# Generated by Django 4.2.6 on 2023-10-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantationOrderItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='plantationordermodel',
            name='card_information',
        ),
        migrations.RemoveField(
            model_name='plantationordermodel',
            name='products',
        ),
        migrations.AddField(
            model_name='plantationordermodel',
            name='collected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plantationordermodel',
            name='delivery_option',
            field=models.CharField(choices=[('D', 'Delivery'), ('C', 'Collect')], default='D', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plantationordermodel',
            name='payment_option',
            field=models.CharField(choices=[('C', 'Cash'), ('P', 'Paypal')], default='D', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plantationordermodel',
            name='cellphone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='plantationordermodel',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='plantationordermodel',
            name='order_number',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='PlantationCardInformation',
        ),
        migrations.AddField(
            model_name='plantationordermodel',
            name='items',
            field=models.ManyToManyField(blank=True, to='orders.plantationorderitemmodel'),
        ),
    ]
