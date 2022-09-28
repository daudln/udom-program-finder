from django.test import TestCase
from .models import Program


class ProgramModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Program.objects.create(name='first Program',
                               description='a body here', years_of_study=3, fee=1000)

    def test_name_content(self):

        program = Program.objects.get(id=1)
        expected_object_name = f'{Program.name}'
        self.assertEquals(expected_object_name, 'first Program')

    def test_description_content(self):

        program = Program.objects.get(id=1)
        expected_object_name = f'{Program.description}'
        self.assertEquals(expected_object_name, 'a body here')
