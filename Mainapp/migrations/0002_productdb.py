# Generated by Django 4.2.5 on 2023-10-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='Product')),
            ],
        ),
    ]