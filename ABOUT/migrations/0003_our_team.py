# Generated by Django 2.2 on 2019-04-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABOUT', '0002_auto_20190409_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our_Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
