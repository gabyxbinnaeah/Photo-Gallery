# Generated by Django 3.2.5 on 2021-07-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]