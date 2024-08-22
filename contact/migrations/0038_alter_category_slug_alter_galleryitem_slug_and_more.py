# Generated by Django 5.0.1 on 2024-04-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0037_alter_barber_image_alter_galleryitem_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='galleryitem',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]