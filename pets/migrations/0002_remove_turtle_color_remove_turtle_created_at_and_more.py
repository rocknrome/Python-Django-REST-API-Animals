# Generated by Django 5.0.3 on 2024-03-23 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turtle',
            name='color',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='is_alive',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='length',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='species',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='weight',
        ),
    ]
