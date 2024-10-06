# Generated by Django 5.1.1 on 2024-10-06 22:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('transaction', '0002_alter_transaction_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transactions', to='content.content'),
        ),
    ]
