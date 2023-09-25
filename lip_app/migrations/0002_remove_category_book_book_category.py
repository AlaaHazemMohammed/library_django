# Generated by Django 4.2.5 on 2023-09-14 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lip_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Book',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lip_app.category'),
        ),
    ]
