# Generated by Django 2.1.2 on 2018-10-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(max_length=225, null=True)),
                ('label', models.CharField(max_length=225, null=True)),
                ('textbox', models.CharField(max_length=225, null=True)),
                ('userid', models.IntegerField(max_length=25, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
