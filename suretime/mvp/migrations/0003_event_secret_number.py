# Generated by Django 3.2.9 on 2021-11-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0002_auto_20211107_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='secret_number',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
