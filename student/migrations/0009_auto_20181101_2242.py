# Generated by Django 2.1.2 on 2018-11-01 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20181101_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Depart'),
        ),
    ]