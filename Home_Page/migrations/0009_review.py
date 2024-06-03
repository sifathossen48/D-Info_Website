# Generated by Django 4.2 on 2024-06-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0008_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='client')),
                ('profile_link', models.CharField(max_length=80)),
                ('message', models.TextField()),
            ],
        ),
    ]