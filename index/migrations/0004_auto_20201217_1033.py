# Generated by Django 3.1.4 on 2020-12-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20201217_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
