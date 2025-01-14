# Generated by Django 4.2.3 on 2023-08-12 21:30

from django.db import migrations, models
import django.db.models.deletion
import pytigon_lib.schtools.schjson


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("schprofile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "jsondata",
                    models.JSONField(
                        blank=True,
                        decoder=pytigon_lib.schtools.schjson.ComplexDecoder,
                        editable=False,
                        encoder=pytigon_lib.schtools.schjson.ComplexEncoder,
                        null=True,
                        verbose_name="Json data",
                    ),
                ),
                (
                    "application",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        max_length=64,
                        null=True,
                        verbose_name="Application",
                    ),
                ),
                (
                    "table",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        max_length=64,
                        null=True,
                        verbose_name="Table",
                    ),
                ),
                (
                    "group",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        max_length=64,
                        null=True,
                        verbose_name="Group",
                    ),
                ),
                (
                    "parent_id",
                    models.IntegerField(
                        blank=True, db_index=True, null=True, verbose_name="Parent id"
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Comment"),
                ),
                (
                    "recipients",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="Recipients"
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Time"
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_recipient_set",
                        to="schprofile.userproxy",
                        verbose_name="Recipient",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_sender_set",
                        to="schprofile.userproxy",
                        verbose_name="Sender",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
                "ordering": ["id"],
                "default_permissions": ("add", "change", "delete", "list"),
            },
        ),
    ]
