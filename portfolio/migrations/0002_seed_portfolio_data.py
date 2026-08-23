from django.db import migrations


def seed_portfolio_data(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    Certification = apps.get_model("portfolio", "Certification")
    Experience = apps.get_model("portfolio", "Experience")

    Project.objects.create(
        title="Shishu-Sneh — Baby's First Year Guide",
        description="Shishu-Sneh is an Android application designed to help new mothers monitor their baby's growth, developmental milestones, and vaccination schedule. The application provides an easy-to-use interface for tracking important information during a baby's first year. Developed with a focus on clean UI, usability, and structured application architecture.",
        image='',
        github_link='https://github.com/maniyarjakeer0209-source/ShishuSnehApp',
        demo_link='',
        technologies='Kotlin, Jetpack Compose, Android Studio, Firebase, MVVM',
        start_date='2026-02-02',
        end_date='2026-05-18',
        status='completed',
        featured=False,
        order=1,
        created_at='2026-08-22T11:14:43.016Z',
    )

    Project.objects.create(
        title='Rivyou — Product Search API',
        description='Rivyou is a backend product search API developed to provide structured product management and search functionality. The project uses Django with PostgreSQL for data persistence and exposes API endpoints for working with product information. Product data is imported from CSV and managed through a relational database, demonstrating practical experience with backend development, database modeling, migrations, and REST API development.',
        image='',
        github_link='https://github.com/maniyarjakeer0209-source/rivyou-product-search-api',
        demo_link='',
        technologies='Python, Django, PostgreSQL, REST API, SQL, CSV',
        start_date='2026-06-02',
        end_date='2026-06-10',
        status='completed',
        featured=False,
        order=2,
        created_at='2026-08-22T11:17:23.061Z',
    )

    Project.objects.create(
        title='CuraLink — Healthcare Platform',
        description='CuraLink is a healthcare-focused application designed to simplify access to healthcare-related services and information through a user-friendly digital platform. The project demonstrates application development, structured UI design, data handling, and integration of modern software development technologies.',
        image='',
        github_link='https://github.com/maniyarjakeer0209-source/curalink',
        demo_link='',
        technologies='TypeScript',
        start_date='2025-02-10',
        end_date='2025-02-20',
        status='completed',
        featured=False,
        order=3,
        created_at='2026-08-22T11:19:36.165Z',
    )

    Project.objects.create(
        title='Student Readiness Analyzer',
        description='A Python-based student readiness analyzer that evaluates academic performance and technical skills against predefined requirements. The application uses functions and collections to process student marks and skills, generate readiness summaries, and identify whether a student meets the required criteria.',
        image='',
        github_link='https://github.com/maniyarjakeer0209-source/preptrack-jakeer',
        demo_link='',
        technologies='Python, Functions, Lists, Dictionaries, Data Processing',
        start_date='2026-08-05',
        end_date='2026-08-06',
        status='completed',
        featured=False,
        order=4,
        created_at='2026-08-22T11:21:41.677Z',
    )

    Project.objects.create(
        title='Foresight — Predictive Kubernetes Autoscaling Engine',
        description='Foresight is a lightweight, pluggable Go service for predictive Kubernetes autoscaling. Instead of waiting for CPU or memory spikes, it analyzes business signals such as flash sales, traffic surges, and market volatility to predict increased demand and proactively scale workloads.\r\n\r\nThe system uses a concurrent worker-pool architecture with goroutines and channels, a pluggable rule engine for extensible scoring, Redis caching for faster repeated predictions, batch signal processing, health checks, structured logging, and graceful degradation when the cache is unavailable.\r\n\r\nBuilt with production-oriented software engineering principles, Foresight demonstrates practical experience in Go, concurrency, REST API design, caching, clean architecture, system design, and performance optimization.',
        image='',
        github_link='https://github.com/maniyarjakeer0209-source/foresight',
        demo_link='',
        technologies='Go, Redis, REST API, Kubernetes, Goroutines, Channels, Worker Pool, Rule Engine, Clean Architecture',
        start_date='2026-08-17',
        end_date='2026-08-20',
        status='completed',
        featured=True,
        order=5,
        created_at='2026-08-22T11:23:35.592Z',
    )

    Certification.objects.create(
        name='Google Cloud Skills Boost',
        organization='Google Cloud',
        issue_date='2026-05-18',
        expiry_date=None,
        credential_id='',
        credential_url='https://www.skills.google/public_profiles/941ce2de-d781-4ee0-8c50-458bacd9411f/badges/24245068',
        logo='',
        order=5,
    )

    Certification.objects.create(
        name='Salesforce Certification / Badge',
        organization='Salesforce',
        issue_date='2026-05-18',
        expiry_date=None,
        credential_id='',
        credential_url='https://www.salesforce.com/trailblazer/profile',
        logo='',
        order=4,
    )

    Certification.objects.create(
        name='Android Development Internship',
        organization='MindMatrix',
        issue_date='2026-05-18',
        expiry_date=None,
        credential_id='Mx26INT05034',
        credential_url='https://lms.mindmatrix.io/',
        logo='',
        order=3,
    )

    Certification.objects.create(
        name='Python Programming Bootcamp / 100 Days of Code: The Complete Python Pro Bootcamp',
        organization='Udemy',
        issue_date='2026-02-10',
        expiry_date=None,
        credential_id='UC-b2b5ac7c-f458-4cde-8cb9-f66c813c2268',
        credential_url='https://www.udemy.com/certificate/UC-b2b5ac7c-f458-4cde-8cb9-f66c813c2268/',
        logo='certifications/1781693272620.jpg',
        order=1,
    )

    Certification.objects.create(
        name='Python (Basic) Certificate',
        organization='HackerRank',
        issue_date='2026-06-10',
        expiry_date=None,
        credential_id='99698BC2827E',
        credential_url='https://www.hackerrank.com/certificates/99698bc2827e',
        logo='certifications/download_1.png',
        order=2,
    )

    Certification.objects.create(
        name='Frontend Developer (React)',
        organization='HackerRank',
        issue_date='2026-06-10',
        expiry_date=None,
        credential_id='21CD8D47A885',
        credential_url='https://www.hackerrank.com/certificates/iframe/21cd8d47a885',
        logo='certifications/download_2.png',
        order=3,
    )

    Experience.objects.create(
        company='MindMatrixEd',
        position='Android Development Intern',
        start_date='2026-02-02',
        end_date='2026-05-18',
        current=False,
        description='Worked as an Android Development Intern, building mobile applications using Kotlin and Jetpack Compose. Contributed to the development of Shishu-Sneh, a baby wellness application focused on growth tracking, developmental milestones, and vaccination management.\r\n\r\nGained hands-on experience with Android Studio, Firebase integration, UI/UX development, application prototyping, debugging, testing, and modern Android development practices. Collaborated on application design and implementation while exploring the use of Generative AI and Google Cloud tools to improve the development workflow.',
        achievements='Developed Shishu-Sneh Android application, Built responsive UI using Jetpack Compose, Integrated Firebase services, Implemented application screens and navigation, Applied MVVM architecture, Used Google AI Studio and Google Cloud tools, Performed debugging and application testing',
        order=1,
    )


def reverse_portfolio_data(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    Certification = apps.get_model("portfolio", "Certification")
    Experience = apps.get_model("portfolio", "Experience")

    Project.objects.all().delete()
    Certification.objects.all().delete()
    Experience.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            seed_portfolio_data,
            reverse_portfolio_data,
        ),
    ]
