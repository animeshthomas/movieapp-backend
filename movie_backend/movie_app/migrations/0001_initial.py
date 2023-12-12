# Generated by Django 4.1.13 on 2023-11-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateField()),
                ('actress', models.CharField(default='', max_length=100)),
                ('director', models.CharField(default='', max_length=100)),
                ('producer', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
