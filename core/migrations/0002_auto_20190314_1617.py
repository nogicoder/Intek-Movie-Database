# Generated by Django 2.1.7 on 2019-03-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='created_at',
            field=models.DateField(),
        ),
    ]