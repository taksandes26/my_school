# Generated by Django 5.0.6 on 2024-10-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('graduated', 'Graduated'), ('transferred', 'Transferred')], default='active', max_length=20, null=True),
        ),
    ]
