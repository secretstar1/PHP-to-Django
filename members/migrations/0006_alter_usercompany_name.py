# Generated by Django 4.2 on 2023-05-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_invoice_address_invoice_companycode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercompany',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
