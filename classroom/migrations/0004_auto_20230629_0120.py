# Generated by Django 2.2.7 on 2023-06-28 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_theory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theory',
            name='link',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='theory',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]