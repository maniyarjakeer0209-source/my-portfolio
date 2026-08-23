from django.db import migrations


def seed_core_data(apps, schema_editor):
    Skill = apps.get_model("core", "Skill")
    Education = apps.get_model("core", "Education")

    Skill.objects.create(
        name='Python',
        category='programming',
        proficiency=85,
        icon='python',
        order=1,
    )

    Skill.objects.create(
        name='SQL',
        category='tools',
        proficiency=80,
        icon='Database',
        order=2,
    )

    Skill.objects.create(
        name='Kotlin',
        category='programming',
        proficiency=70,
        icon='Kotlin',
        order=3,
    )

    Skill.objects.create(
        name='Android Development',
        category='programming',
        proficiency=70,
        icon='android',
        order=4,
    )

    Skill.objects.create(
        name='Jetpack Compose',
        category='programming',
        proficiency=70,
        icon='jetpack-compose',
        order=5,
    )

    Skill.objects.create(
        name='FastAPI',
        category='programming',
        proficiency=70,
        icon='Backend',
        order=6,
    )

    Skill.objects.create(
        name='Firebase',
        category='programming',
        proficiency=70,
        icon='Database',
        order=7,
    )

    Skill.objects.create(
        name='PostgreSQL',
        category='tools',
        proficiency=70,
        icon='Database',
        order=8,
    )

    Skill.objects.create(
        name='Git & GitHub',
        category='tools',
        proficiency=80,
        icon='github',
        order=9,
    )

    Skill.objects.create(
        name='REST API',
        category='programming',
        proficiency=80,
        icon='Backend',
        order=10,
    )

    Skill.objects.create(
        name='Go',
        category='programming',
        proficiency=70,
        icon='go',
        order=6,
    )

    Skill.objects.create(
        name='Machine Learning',
        category='design',
        proficiency=60,
        icon='machine-learning',
        order=12,
    )

    Education.objects.create(
        institution='Dr. Sri Sri Sri Shivakumara Mahaswamy College of Engineering (Dr. SMCE)',
        degree='Bachelor of Engineering (B.E.)',
        field='Computer Science Engineering (CSE)',
        start_date='2022-12-02',
        end_date='2026-06-27',
        description='Pursued a Bachelor of Engineering (B.E.) in Computer Science Engineering, developing a strong foundation in programming, object-oriented programming, databases, software development, and problem-solving. Gained hands-on experience through academic projects and practical learning in Python, SQL, Android development, and modern software development tools. Graduated in 2026 with a CGPA of 7.75.',
        order=0,
    )


def reverse_core_data(apps, schema_editor):
    Skill = apps.get_model("core", "Skill")
    Education = apps.get_model("core", "Education")

    Skill.objects.all().delete()
    Education.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            seed_core_data,
            reverse_core_data,
        ),
    ]