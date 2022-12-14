# Generated by Django 4.0.3 on 2022-06-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_loan_status_accountant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status_accountant',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status_president',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status_secretary',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=10, null=True),
        ),
    ]
