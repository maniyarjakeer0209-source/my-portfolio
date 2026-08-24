from django.db import migrations


def update_certification_logos(apps, schema_editor):
    Certification = apps.get_model("portfolio", "Certification")

    logos = {
        "Google Cloud Skills Boost": "certifications/google_badge.png",
        "Salesforce Certification / Badge": "certifications/Screenshot_2026-08-24_174124.png",
        "Android Development Internship": "certifications/internship_certificate.png",
    }

    for name, logo in logos.items():
        Certification.objects.filter(name=name).update(logo=logo)


def reverse_update_certification_logos(apps, schema_editor):
    Certification = apps.get_model("portfolio", "Certification")

    Certification.objects.filter(
        name__in=[
            "Google Cloud Skills Boost",
            "Salesforce Certification / Badge",
            "Android Development Internship",
        ]
    ).update(logo="")


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0005_fix_project_titles"),
    ]

    operations = [
        migrations.RunPython(
            update_certification_logos,
            reverse_update_certification_logos,
        ),
    ]