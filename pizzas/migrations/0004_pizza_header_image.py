# Generated by Django 3.2 on 2021-05-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
