# Generated by Django 3.0.7 on 2020-06-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actnaturalapp', '0004_auto_20200611_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]