# Generated by Django 3.2.13 on 2022-05-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNews', models.CharField(max_length=10)),
                ('nick', models.CharField(max_length=45)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
