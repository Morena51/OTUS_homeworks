import random

from django.test import TestCase
from ..models import E2ECoverage, Project


class E2ETest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Project.objects.create(
            name='otus',
            description='test django example'
        )

    def setUp(self):
        E2ECoverage.objects.create(
            project=Project.objects.get(id=1),
            manual=random.randint(1, 100000),
            automated=random.randint(1, 100000)
        )

    @classmethod
    def tearDownClass(cls):
        Project.objects.all().delete()
        E2ECoverage.objects.all().delete()
        super().tearDownClass()

    def test_get_coverage_non_negative(self):
        E2ECoverage.objects.all()[0]
        coverage_e2e = E2ECoverage.objects.all()[0].get_coverage_count()
        self.assertTrue(coverage_e2e >= 0)

    def test_get_coverage_correct_value(self):
        e2e_obj = E2ECoverage.objects.all()[0]
        coverage_e2e = e2e_obj.get_coverage_count()
        self.assertEqual(coverage_e2e, 100 - round(100 * e2e_obj.manual/(e2e_obj.manual + e2e_obj.automated),2))

    def test_e2e_page(self):
        response = self.client.get('/e2e')
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context['user'].is_anonymous)

