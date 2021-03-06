# Generated by Django 3.1.2 on 2020-10-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('pub_date', models.DateField()),
                ('isbn', models.IntegerField(unique=True)),
                ('pages', models.IntegerField()),
                ('cover', models.URLField(blank=True)),
                ('lang', models.CharField(max_length=16)),
            ],
        ),
    ]
