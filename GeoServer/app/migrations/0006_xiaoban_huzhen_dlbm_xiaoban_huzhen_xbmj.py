# Generated by Django 5.0.3 on 2024-04-04 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_xiaoban_huzhen'),
    ]

    operations = [
        migrations.AddField(
            model_name='xiaoban_huzhen',
            name='dlbm',
            field=models.CharField(max_length=5, null=True, verbose_name='地类编码'),
        ),
        migrations.AddField(
            model_name='xiaoban_huzhen',
            name='xbmj',
            field=models.FloatField(null=True, verbose_name='小班面积'),
        ),
    ]
