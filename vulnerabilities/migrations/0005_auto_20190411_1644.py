# Generated by Django 2.2 on 2019-04-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0004_auto_20190407_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagereference',
            name='repository',
            field=models.CharField(blank=True, help_text='Repository URL eg:http://central.maven.org', max_length=100),
        ),
    ]
