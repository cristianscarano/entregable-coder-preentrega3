# Generated by Django 5.0.7 on 2024-07-29 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0002_entregables_profesor_alter_curso_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
