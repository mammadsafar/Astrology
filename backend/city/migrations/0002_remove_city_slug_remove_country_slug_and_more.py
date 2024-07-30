# Generated by Django 4.2.13 on 2024-07-13 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("city", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="city",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="country",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="province",
            name="slug",
        ),
        migrations.AddField(
            model_name="city",
            name="english_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="country",
            name="english_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="province",
            name="english_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="country",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="country",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]