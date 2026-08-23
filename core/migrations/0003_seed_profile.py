from django.db import migrations
from django.contrib.auth.hashers import make_password


def seed_profile(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Profile = apps.get_model("core", "Profile")

    # Create/find the Django user that owns the portfolio profile.
    user, created = User.objects.get_or_create(
        username="maniyarjakeer",
        defaults={
            "email": "maniyarjakeer0209@gmail.com",
            "first_name": "Mohammed",
            "last_name": "Jakeer F Maniyar",
            "is_staff": False,
            "is_active": True,
        },
    )

    # We don't know a production password here, so don't create
    # a usable password from the migration.
    if created:
        user.password = make_password(None)
        user.save()

    Profile.objects.update_or_create(
        user=user,
        defaults={
            "name": "Mohammed Jakeer F Maniyar",
            "title": "Software Developer | Computer Science Engineer",
            "bio": (
                "I'm a Computer Science & Engineering graduate and "
                "aspiring Software Developer with a strong interest in "
                "building practical, scalable, and user-focused applications. "
                "I work with Python, SQL, Kotlin, Android Development, "
                "Jetpack Compose, Firebase, Git, and GitHub, and I'm currently "
                "strengthening my backend development skills with FastAPI, "
                "PostgreSQL, and REST APIs.\n\n"
                "I enjoy solving real-world problems through software, "
                "learning new technologies, and building projects that combine "
                "clean design with reliable functionality. I'm particularly "
                "interested in backend development, AI-powered applications, "
                "and modern software engineering."
            ),
            "profile_image": "profile/profile_photo.png",
            "email": "maniyarjakeer0209@gmail.com",
            "phone": "6363310755",
            "location": "Bengaluru, Karnataka",
            "github": "https://github.com/maniyarjakeer0209-source",
            "linkedin": "https://www.linkedin.com/in/mdjakeer249/",
            "twitter": "",
            "youtube": "",
            "resume_file": "resume/MohammedJakeerResume.pdf",
        },
    )


def reverse_profile(apps, schema_editor):
    Profile = apps.get_model("core", "Profile")
    User = apps.get_model("auth", "User")

    profile = Profile.objects.filter(
        email="maniyarjakeer0209@gmail.com"
    ).first()

    if profile:
        user = profile.user
        profile.delete()

        # Only remove the user if this migration created the association.
        if user.username == "maniyarjakeer":
            user.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_seed_portfolio_data"),
    ]

    operations = [
        migrations.RunPython(
            seed_profile,
            reverse_profile,
        ),
    ]