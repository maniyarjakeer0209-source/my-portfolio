from django.db import migrations


def sync_skills(apps, schema_editor):
    Skill = apps.get_model("core", "Skill")

    # Remove the skill we no longer want on the portfolio.
    Skill.objects.filter(name="Machine Learning").delete()

    # Make sure Django exists in production.
    Skill.objects.get_or_create(
        name="Django",
        defaults={
            "category": "programming",
            "proficiency": 70,
            "icon": "django",
            "order": 7,
        },
    )


def reverse_sync_skills(apps, schema_editor):
    Skill = apps.get_model("core", "Skill")

    Skill.objects.filter(name="Django").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_seed_profile"),
    ]

    operations = [
        migrations.RunPython(
            sync_skills,
            reverse_sync_skills,
        ),
    ]