from django.db import migrations


def remove_duplicate_certifications(apps, schema_editor):
    Certification = apps.get_model("portfolio", "Certification")

    keep_ids = [1, 2, 3, 4, 5, 6]

    Certification.objects.exclude(id__in=keep_ids).delete()


def reverse_remove_duplicate_certifications(apps, schema_editor):
    # This cleanup is intentionally irreversible because the deleted
    # records are exact duplicates of the retained certifications.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0006_update_certification_logos"),
    ]

    operations = [
        migrations.RunPython(
            remove_duplicate_certifications,
            reverse_remove_duplicate_certifications,
        ),
    ]
