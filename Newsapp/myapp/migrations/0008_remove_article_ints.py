# Generated by Django 3.0.3 on 2020-02-20 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_article_ints'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='ints',
        ),
    ]
