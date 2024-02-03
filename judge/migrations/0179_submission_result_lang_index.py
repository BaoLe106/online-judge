# Generated by Django 3.2.18 on 2024-01-23 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0178_remove_user_script"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="submission",
            index=models.Index(
                fields=["language", "result"], name="judge_submi_languag_874af4_idx"
            ),
        ),
    ]