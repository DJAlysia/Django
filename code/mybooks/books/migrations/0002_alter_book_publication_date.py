# Generated by Django 4.2.2 on 2023-07-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateTimeField(),
        ),
    ]