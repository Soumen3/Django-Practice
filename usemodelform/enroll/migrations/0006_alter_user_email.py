# Generated by Django 4.1.7 on 2023-04-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_user_hobby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
