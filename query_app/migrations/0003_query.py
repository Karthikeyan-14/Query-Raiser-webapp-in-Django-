# Generated by Django 5.0.4 on 2024-05-27 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_app', '0002_rename_reg_register_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_type', models.CharField(choices=[('student', 'Student'), ('employee', 'Employee')], max_length=10)),
                ('query_priority', models.CharField(choices=[('high', 'High'), ('low', 'Low')], max_length=10)),
                ('query_title', models.CharField(max_length=50)),
                ('query_data', models.CharField(max_length=200)),
                ('query_date', models.DateField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query_app.register_data')),
            ],
        ),
    ]
