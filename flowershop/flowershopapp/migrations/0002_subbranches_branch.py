# Generated by Django 3.2.12 on 2022-06-15 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowershopapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subbranches',
            name='branch',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='flowershopapp.Branches'),
            preserve_default=False,
        ),
    ]
