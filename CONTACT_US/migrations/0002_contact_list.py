# Generated by Django 2.2 on 2019-04-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CONTACT_US', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
