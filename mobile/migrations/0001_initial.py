# Generated by Django 3.0.7 on 2021-12-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrandName', models.CharField(max_length=222, unique=True)),
                ('Model', models.CharField(blank=True, max_length=222, null=True)),
                ('Color', models.CharField(blank=True, max_length=222, null=True)),
                ('JANCode', models.CharField(max_length=222, unique=True)),
                ('Image', models.ImageField(blank=True, upload_to='media/post_image')),
            ],
        ),
    ]