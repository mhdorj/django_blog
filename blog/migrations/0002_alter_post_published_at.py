# Generated by Django 4.2.3 on 2023-07-03 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
