# Generated by Django 3.1.5 on 2021-06-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cv_Maker_App', '0003_auto_20210612_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicemodel',
            name='picture',
            field=models.ImageField(upload_to='pictures', verbose_name='Upload CV Picture'),
        ),
    ]
