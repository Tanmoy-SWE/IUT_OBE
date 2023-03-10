# Generated by Django 4.1 on 2023-03-03 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_assignedcourses_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='CO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coID', models.CharField(default=None, max_length=200)),
                ('description', models.CharField(default=None, max_length=2000)),
                ('CourseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.course')),
            ],
        ),
    ]
