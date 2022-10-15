# Generated by Django 4.0.3 on 2022-05-31 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_loan_member_loan_installment'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_installment',
            name='year',
            field=models.PositiveIntegerField(blank=True, choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039'), ('2040', '2040')], null=True),
        ),
    ]