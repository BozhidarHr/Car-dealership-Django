# Generated by Django 4.1.3 on 2022-12-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_reportlisting_email_alter_reportlisting_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=50),
        ),
    ]