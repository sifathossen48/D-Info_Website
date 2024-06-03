# Generated by Django 4.2 on 2024-06-02 09:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_Updated', models.DateTimeField(auto_now=True)),
                ('interpretation', models.TextField()),
                ('definitions', ckeditor.fields.RichTextField()),
                ('acknowledgment', models.TextField()),
                ('others', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
