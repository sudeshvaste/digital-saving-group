# Generated by Django 4.0.3 on 2022-10-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_alter_loan_installment_status_accountant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=25)),
                ('amount', models.PositiveIntegerField(max_length=25)),
            ],
        ),
    ]
