# Generated by Django 4.0.4 on 2022-05-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, help_text='Number of Pages', null=True),
        ),
    ]
