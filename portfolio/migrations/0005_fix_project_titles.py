from django.db import migrations


def fix_project_titles(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")

    Project.objects.filter(
        title__startswith="Shishu-Sneh"
    ).update(
        title="Shishu-Sneh \u2014 Baby's First Year Guide"
    )

    Project.objects.filter(
        title__startswith="Rivyou"
    ).update(
        title="Rivyou \u2014 Product Search API"
    )

    Project.objects.filter(
        title__startswith="CuraLink"
    ).update(
        title="CuraLink \u2014 Healthcare Platform"
    )

    Project.objects.filter(
        title__startswith="Student Readiness"
    ).update(
        title="Student Readiness Analyzer"
    )

    Project.objects.filter(
        title__startswith="Foresight"
    ).update(
        title="Foresight \u2014 Predictive Kubernetes Autoscaling Engine"
    )


def reverse_project_titles(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")

    Project.objects.filter(
        title="Shishu-Sneh \u2014 Baby's First Year Guide"
    ).update(
        title="Shishu-Sneh û Baby's First Year Guide"
    )

    Project.objects.filter(
        title="Rivyou \u2014 Product Search API"
    ).update(
        title="Rivyou û Product Search API"
    )

    Project.objects.filter(
        title="CuraLink \u2014 Healthcare Platform"
    ).update(
        title="CuraLink û Healthcare Platform"
    )

    Project.objects.filter(
        title="Foresight \u2014 Predictive Kubernetes Autoscaling Engine"
    ).update(
        title="Foresight û Predictive Kubernetes Autoscaling Engine"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_seed_portfolio_data"),
    ]

    operations = [
        migrations.RunPython(
            fix_project_titles,
            reverse_project_titles,
        ),
    ]