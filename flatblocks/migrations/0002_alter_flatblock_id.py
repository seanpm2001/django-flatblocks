# Generated by Django 3.2.11 on 2022-01-08 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatblocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatblock',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
