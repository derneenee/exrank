from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Exchange
from ..views import TopicListView


class ExchangeTopicsTests(TestCase):
    def setUp(self):
        Exchange.objects.create(name='Django', description='Django exchange.')

    def test_exchange_topics_view_success_status_code(self):
        url = reverse('exchange_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_exchange_topics_view_not_found_status_code(self):
        url = reverse('exchange_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_exchange_topics_url_resolves_exchange_topics_view(self):
        view = resolve('/exchanges/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    def test_exchange_topics_view_contains_navigation_links(self):
        exchange_topics_url = reverse('exchange_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(exchange_topics_url)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
