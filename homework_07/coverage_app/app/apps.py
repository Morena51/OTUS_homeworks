from django.test import TestCase
from


class ProjectTest(TestCase):
    def setUpClass(cls):
        super().setUpClass()
        cls.project = {
            'name': 'testing'
        }


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


    def test_create_project(self):
        response = self.client.post(
            '/zauth/user/create/',
            data=self.user_data
        )
        self.assertEqual(302, response.status_code)


    def test_list_project(self):
        pass