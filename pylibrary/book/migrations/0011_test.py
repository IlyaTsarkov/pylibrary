# Generated by Django 4.0.3 on 2022-05-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_book_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]