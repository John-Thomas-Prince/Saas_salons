# Generated by Django 5.0.1 on 2024-02-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0018_alter_appointment_barber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='visitor_hash',
        ),
        migrations.RemoveField(
            model_name='review',
            name='visitor_hash',
        ),
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]