# Generated by Django 2.1.2 on 2018-10-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='sub1',
            new_name='CED',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='sub2',
            new_name='CHE',
        ),
        migrations.AddField(
            model_name='marks',
            name='CIV',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='marks',
            name='ELN',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='marks',
            name='MAT',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='marks',
            name='PCD',
            field=models.IntegerField(null=True),
        ),
    ]
