# Generated by Django 2.2 on 2019-04-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_gallery', '0002_auto_20190413_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='video_link',
            field=models.CharField(max_length=200),
        ),
    ]