# Generated by Django 2.2.7 on 2019-11-23 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0003_electricity_expense_expense'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electricity_expense',
            old_name='expense',
            new_name='cost',
        ),
    ]