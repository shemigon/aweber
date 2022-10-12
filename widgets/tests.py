from django.test import TestCase
from rest_framework.reverse import reverse

from .models import Widget


class WidgetViewSetTestCase(TestCase):
    def setUp(self):
        self.widgets = Widget.objects.bulk_create([
            Widget(name="Test 1", part_number=1),
            Widget(name="Test 2", part_number=2),
            Widget(name="Test 3", part_number=3),
        ])

    def test_list(self):
        url = reverse('api:widget-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_insert(self):
        url = reverse('api:widget-list')
        response = self.client.post(url, {
            'name': 'Test 4',
            'part_number': 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Widget.objects.count(), 4)

    def test_update(self):
        widget = self.widgets[0]
        url = reverse('api:widget-detail', kwargs={'pk': widget.pk})
        response = self.client.patch(url, {
            'name': 'Test 11',
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        widget.refresh_from_db()
        self.assertEqual(widget.name, 'Test 11')

    def test_delete(self):
        widget = self.widgets[0]
        url = reverse('api:widget-detail', kwargs={'pk': widget.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Widget.objects.count(), 2)
