# Generated by Django 4.0.3 on 2022-05-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_loanintrest_loan_limit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_Limit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_limit', models.PositiveIntegerField(blank=True, null=True)),
                ('Tag', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='loanintrest',
            old_name='reasons',
            new_name='Tag',
        ),
        migrations.RemoveField(
            model_name='loanintrest',
            name='loan_limit',
        ),
    ]