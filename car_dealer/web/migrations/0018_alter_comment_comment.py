# Generated by Django 4.1.3 on 2022-12-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=100),
        ),
    ]
