# Generated by Django 4.0.3 on 2022-06-04 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_bachat_month_alter_bachat_status_accountant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bachat',
            name='status_accountant',
            field=models.BooleanField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='approve',
            field=models.BooleanField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status_accountant',
            field=models.BooleanField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status_president',
            field=models.BooleanField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status_secretary',
            field=models.BooleanField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan_installment',
            name='status_accountant',
            field=models.BooleanField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', null=True),
        ),
    ]
