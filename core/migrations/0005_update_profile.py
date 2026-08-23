from django.db import migrations


def update_profile(apps, schema_editor):
    Profile = apps.get_model("core", "Profile")

    Profile.objects.filter(
        email="maniyarjakeer0209@gmail.com"
    ).update(
        bio=(
            "Computer Science & Engineering graduate and Software Developer "
            "focused on building practical, scalable, and reliable software.\n\n"
            "I work with Python, Django, FastAPI, Go, SQL, PostgreSQL, REST APIs, "
            "Redis, Git, and GitHub, with additional experience in Kotlin, "
            "Android Development, Jetpack Compose, and Firebase.\n\n"
            "I enjoy solving real-world problems through clean architecture, "
            "backend systems, databases, APIs, and production-oriented software "
            "engineering. I am particularly interested in backend development, "
            "scalable systems, and AI-powered applications."
        )
    )


def reverse_profile_update(apps, schema_editor):
    Profile = apps.get_model("core", "Profile")

    Profile.objects.filter(
        email="maniyarjakeer0209@gmail.com"
    ).update(
        bio=(
            "I'm a Computer Science & Engineering graduate and aspiring "
            "Software Developer with a strong interest in building practical, "
            "scalable, and user-focused applications. I work with Python, SQL, "
            "Kotlin, Android Development, Jetpack Compose, Firebase, Git, and "
            "GitHub, and I'm currently strengthening my backend development "
            "skills with FastAPI, PostgreSQL, and REST APIs.\n\n"
            "I enjoy solving real-world problems through software, learning new "
            "technologies, and building projects that combine clean design with "
            "reliable functionality. I'm particularly interested in backend "
            "development, AI-powered applications, and modern software engineering."
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_sync_skills"),
    ]

    operations = [
        migrations.RunPython(
            update_profile,
            reverse_profile_update,
        ),
    ]