# Generated by Django 4.1.3 on 2022-12-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_listing_user_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.CharField(choices=[('VS', 'Very satisfied'), ('S', 'Satisfied'), ('NS', 'Neither satisfied nor dissatisfied'), ('U', 'Unsatisfied'), ('VU', 'Very unsatisfied')], max_length=2),
        ),
    ]