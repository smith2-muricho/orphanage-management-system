# Generated by Django 4.1.2 on 2021-07-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphan', '0003_rename_level_needy_case_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('help_offered', models.CharField(max_length=30)),
            ],
        ),
    ]
