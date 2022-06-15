# Generated by Django 3.2.12 on 2022-06-14 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'bname',
                'verbose_name_plural': 'bnames',
                'ordering': ('bname',),
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Subbranches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subname', models.CharField(max_length=250)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowershopapp.Branches')),
            ],
        ),
    ]
