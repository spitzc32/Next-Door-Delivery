# Generated by Django 3.1 on 2021-01-20 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userForm', '0002_auto_20210120_0830'),
        ('associates', '0003_auto_20210120_0653'),
        ('rider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='latitude',
            field=models.FloatField(default=121.0537),
        ),
        migrations.AddField(
            model_name='rider',
            name='longitude',
            field=models.FloatField(default=14.6193),
        ),
        migrations.AddField(
            model_name='rider',
            name='user',
            field=models.ManyToManyField(through='associates.UserRider', to='userForm.Users'),
        ),
        migrations.AlterField(
            model_name='rider',
            name='address',
            field=models.TextField(default='', max_length=2000),
        ),
    ]