# Generated by Django 4.0.3 on 2022-05-31 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_bachat_year_alter_loan_installment_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='bachat',
            name='status_accountant',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loan_installment',
            name='status_accountant',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
