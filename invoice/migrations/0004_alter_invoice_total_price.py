# Generated by Django 4.2.5 on 2023-09-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_rename_line_eight_quantity_invoice_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total (Ksh)'),
        ),
    ]