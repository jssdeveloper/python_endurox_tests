# Generated by Django 4.2.6 on 2023-10-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionId', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
