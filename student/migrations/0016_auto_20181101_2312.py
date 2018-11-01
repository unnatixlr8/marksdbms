# Generated by Django 2.1.2 on 2018-11-01 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20181101_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='Department',
        ),
        migrations.AddField(
            model_name='students',
            name='Department',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.Depart'),
            preserve_default=False,
        ),
    ]