# Generated by Django 2.2.10 on 2020-03-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinets', '0002_auto_20190729_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]