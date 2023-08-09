# Generated by Django 4.2.4 on 2023-08-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='products/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
