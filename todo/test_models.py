from django.test import TestCase
from .models import Item

# Create your tests here.
class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='We all are there')
        self.assertFalse(item.done)


    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='We all are there')
        self.assertEqual(str(item), 'We all are there')