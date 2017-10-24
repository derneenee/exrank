from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Exchange, Post, Topic
from ..views import PostListView


class TopicPostsTests(TestCase):
    def setUp(self):
        exchange = Exchange.objects.create(name='Django', description='Django exchange.')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        topic = Topic.objects.create(subject='Hello, world', exchange=exchange, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk': exchange.pk, 'topic_pk': topic.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/exchanges/1/topics/1/')
        self.assertEquals(view.func.view_class, PostListView)
