# Generated by Django 4.2 on 2023-04-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0006_alter_otp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='dis_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
