# Generated by Django 4.2 on 2023-04-20 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urna_app', '0002_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='urna_app.candidate'),
            preserve_default=False,
        ),
    ]
