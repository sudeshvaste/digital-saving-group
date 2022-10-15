# Generated by Django 4.0.3 on 2022-06-04 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_bachat_status_accountant_alter_loan_approve_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bachat',
            name='status_accountant',
            field=models.BooleanField(blank=True, choices=[(None, 'Pending'), (True, 'Approved'), (False, 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='approve',
            field=models.BooleanField(blank=True, choices=[(None, 'Pending'), (True, 'Approved'), (False, 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status_accountant',
            field=models.BooleanField(blank=True, choices=[(None, 'Pending'), (True, 'Approved'), (False, 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status_president',
            field=models.BooleanField(blank=True, choices=[(None, 'Pending'), (True, 'Approved'), (False, 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status_secretary',
            field=models.BooleanField(blank=True, choices=[(None, 'Pending'), (True, 'Approved'), (False, 'Rejected')], default='Pending', null=True),
        ),
        migrations.AlterField(
            model_name='loan_installment',
            name='status_accountant',
            field=models.BooleanField(blank=True, choices=[(None, 'Pending'), (True, 'Approved'), (False, 'Rejected')], default='Pending', null=True),
        ),
    ]