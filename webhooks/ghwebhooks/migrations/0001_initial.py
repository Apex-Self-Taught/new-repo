# Generated by Django 3.0.4 on 2020-03-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreHooksData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('user_id', models.IntegerField(unique=True)),
                ('avatar_url', models.CharField(max_length=1000)),
            ],
        ),
    ]
