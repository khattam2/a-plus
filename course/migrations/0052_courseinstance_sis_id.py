# Generated by Django 3.2.7 on 2021-11-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0051_auto_20210812_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinstance',
            name='sis_id',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='LABEL_SIS_IDENTIFIER'),
        ),
    ]
