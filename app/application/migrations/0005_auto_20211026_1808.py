# Generated by Django 3.2.8 on 2021-10-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20211026_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(blank=True, default='', max_length=160),
        ),
        migrations.AlterField(
            model_name='application',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='reviewed_by',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='application',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
