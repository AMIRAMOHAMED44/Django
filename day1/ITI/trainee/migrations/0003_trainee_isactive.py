# Generated by Django 5.1.7 on 2025-03-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_trainee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
