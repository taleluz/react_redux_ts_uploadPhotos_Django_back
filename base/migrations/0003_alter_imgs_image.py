# Generated by Django 4.0.6 on 2023-02-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_imgs_delete_apis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgs',
            name='image',
            field=models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to=''),
        ),
    ]