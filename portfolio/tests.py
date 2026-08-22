from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Certification, Experience, Testimonial

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            description="This is a test project",
            technologies="Python, Django",
            status="completed"
        )

    def test_project_creation(self):
        self.assertEqual(self.project.title, "Test Project")
        self.assertEqual(self.project.status, "completed")
        self.assertTrue(isinstance(self.project, Project))

    def test_get_tech_list(self):
        tech_list = self.project.get_tech_list()
        self.assertEqual(tech_list, ["Python", "Django"])

    def test_project_str_method(self):
        self.assertEqual(str(self.project), "Test Project")


class CertificationModelTest(TestCase):
    def setUp(self):
        self.cert = Certification.objects.create(
            name="AWS Certified Developer",
            organization="Amazon Web Services",
            issue_date="2024-01-01"
        )

    def test_certification_creation(self):
        self.assertEqual(self.cert.name, "AWS Certified Developer")
        self.assertTrue(isinstance(self.cert, Certification))

    def test_certification_str_method(self):
        self.assertEqual(str(self.cert), "AWS Certified Developer - Amazon Web Services")


class ExperienceModelTest(TestCase):
    def setUp(self):
        self.exp = Experience.objects.create(
            company="Tech Corp",
            position="Software Developer",
            start_date="2023-01-01",
            current=True,
            description="Developing web applications"
        )

    def test_experience_creation(self):
        self.assertEqual(self.exp.company, "Tech Corp")
        self.assertTrue(self.exp.current)

    def test_experience_str_method(self):
        self.assertEqual(str(self.exp), "Software Developer at Tech Corp")


class TestimonialModelTest(TestCase):
    def setUp(self):
        self.testimonial = Testimonial.objects.create(
            name="John Doe",
            position="CEO",
            company="Tech Corp",
            content="Great developer!",
            featured=True
        )

    def test_testimonial_creation(self):
        self.assertEqual(self.testimonial.name, "John Doe")
        self.assertTrue(self.testimonial.featured)

    def test_testimonial_str_method(self):
        self.assertEqual(str(self.testimonial), "John Doe - CEO")