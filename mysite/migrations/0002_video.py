# Generated by Django 3.1.2 on 2020-11-07 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('vid', models.CharField(max_length=20)),
                ('plist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.playlist')),
            ],
        ),
    ]
