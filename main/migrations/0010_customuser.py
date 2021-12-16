# Generated by Django 4.0 on 2021-12-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=254)),
                ('username', models.CharField(default='', max_length=255)),
                ('role', models.CharField(default='', max_length=8)),
                ('password', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
