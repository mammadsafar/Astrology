# Generated by Django 5.0.4 on 2024-04-24 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Home",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "persianName",
                    models.CharField(max_length=120, verbose_name="نام فارسی"),
                ),
                (
                    "nationalName",
                    models.CharField(max_length=120, verbose_name="نام انگلیسی"),
                ),
                (
                    "description",
                    models.TextField(max_length=3000, verbose_name="توضیحات"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش"),
                ),
            ],
            options={
                "verbose_name": "خانه",
                "verbose_name_plural": "خانه ها",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Plant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "persianName",
                    models.CharField(max_length=120, verbose_name="نام فارسی"),
                ),
                (
                    "nationalName",
                    models.CharField(max_length=120, verbose_name="نام انگلیسی"),
                ),
                (
                    "description",
                    models.TextField(max_length=3000, verbose_name="توضیحات"),
                ),
                (
                    "reinDescription",
                    models.TextField(
                        blank=True,
                        max_length=3000,
                        null=True,
                        verbose_name="توضیحات تقویت",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="chart/plant", verbose_name="تصویر"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش"),
                ),
            ],
            options={
                "verbose_name": "سیاره",
                "verbose_name_plural": "سیاره ها",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="PlantLayer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "persianName",
                    models.CharField(max_length=120, verbose_name="نام فارسی"),
                ),
                (
                    "nationalName",
                    models.CharField(max_length=120, verbose_name="نام انگلیسی"),
                ),
                (
                    "description",
                    models.TextField(max_length=3000, verbose_name="توضیحات"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش"),
                ),
            ],
            options={
                "verbose_name": "لایه",
                "verbose_name_plural": "لایه ها",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Zodiac",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "persianName",
                    models.CharField(max_length=120, verbose_name="نام فارسی"),
                ),
                (
                    "nationalName",
                    models.CharField(max_length=120, verbose_name="نام انگلیسی"),
                ),
                ("sign", models.CharField(max_length=120, verbose_name="علامت")),
                (
                    "description",
                    models.TextField(max_length=3000, verbose_name="توضیحات"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="chart/zodiac", verbose_name="تصویر"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش"),
                ),
            ],
            options={
                "verbose_name": "زودیاک",
                "verbose_name_plural": "زودیاک ها",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Detail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="نام")),
                (
                    "description",
                    models.TextField(max_length=3000, verbose_name="توضیحات"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش"),
                ),
                (
                    "home",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="chart.home",
                        verbose_name="خانه",
                    ),
                ),
                (
                    "plant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="chart.plant",
                        verbose_name="سیاره",
                    ),
                ),
                (
                    "plantLayer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="chart.plantlayer",
                        verbose_name="لایه سیاره",
                    ),
                ),
                (
                    "zodiac",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="chart.zodiac",
                        verbose_name="زودیاک",
                    ),
                ),
            ],
            options={
                "verbose_name": "جزییات",
                "verbose_name_plural": "جزییات ها",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Psychology",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="نام")),
                (
                    "description",
                    models.TextField(max_length=3000, verbose_name="توضیحات"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش"),
                ),
                (
                    "detail",
                    models.ManyToManyField(to="chart.detail", verbose_name="خانه"),
                ),
            ],
            options={
                "verbose_name": "موارد",
                "verbose_name_plural": "موارد ها",
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddField(
            model_name="plant",
            name="reinforcement",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="تقویت",
                to="chart.zodiac",
                verbose_name="تقویت",
            ),
        ),
    ]