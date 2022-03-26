# Generated by Django 4.0.3 on 2022-03-26 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articlescategories_categories_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlescategories',
            name='categories_title',
        ),
        migrations.AlterField(
            model_name='articles',
            name='create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='posted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.RemoveField(
            model_name='articlescategories',
            name='categories',
        ),
        migrations.AddField(
            model_name='articlescategories',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='articles.articles'),
        ),
        migrations.RemoveField(
            model_name='articlescategoriesmini',
            name='categories_mini',
        ),
        migrations.AddField(
            model_name='articlescategoriesmini',
            name='categories_mini',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='articles.articlescategories'),
        ),
        migrations.AlterField(
            model_name='articlescategoriesmini',
            name='categories_mini_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]