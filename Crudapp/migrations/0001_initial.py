# Generated by Django 3.0.8 on 2020-09-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.IntegerField()),
                ('Name', models.CharField(max_length=150)),
                ('Marks', models.IntegerField()),
                ('Address', models.CharField(max_length=150)),
            ],
        ),
    ]
