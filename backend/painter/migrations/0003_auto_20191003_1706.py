# Generated by Django 2.1 on 2019-10-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painter', '0002_auto_20191003_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='avatars'),
        ),
    ]
