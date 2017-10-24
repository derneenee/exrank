from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Exchange
from ..views import ExchangeListView


class HomeTests(TestCase):
    def setUp(self):
        self.exchange = Exchange.objects.create(name='Django', description='Django exchange.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, ExchangeListView)

    def test_home_view_contains_link_to_topics_page(self):
        exchange_topics_url = reverse('exchange_topics', kwargs={'pk': self.exchange.pk})
        self.assertContains(self.response, 'href="{0}"'.format(exchange_topics_url))
