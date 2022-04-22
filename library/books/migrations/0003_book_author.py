# Generated by Django 4.0 on 2022-04-20 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('books', '0002_rename_add_at_book_add_to_site_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
    ]