from django.test import TestCase

from ..models import Project


class ProjectTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Project.objects.create(
            name='Тестовый проект',
            description='test django example'
        )

    @classmethod
    def tearDownClass(cls):
        Project.objects.all().delete()
        super().tearDownClass()

    def test_list_project_page(self):
        response = self.client.get('/')
        print(response.context)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Список проектов')
        self.assertTrue('project_list' in response.context)
