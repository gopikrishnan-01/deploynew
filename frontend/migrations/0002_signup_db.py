# Generated by Django 4.2.5 on 2023-10-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(blank=True, max_length=100, null=True)),
                ('u_mobile', models.IntegerField(blank=True, null=True)),
                ('u_email', models.CharField(blank=True, max_length=100, null=True)),
                ('u_username', models.CharField(blank=True, max_length=100, null=True)),
                ('u_password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]