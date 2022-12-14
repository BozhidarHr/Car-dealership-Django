# Generated by Django 4.1.3 on 2022-12-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_rename_text_comment_comment_remove_listing_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='color',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='engine',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
