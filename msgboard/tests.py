import pytest
from django.db.models.query import QuerySet

from .models import Message


@pytest.mark.django_db
class TestMessage:
    def test_main_feed(cls):
        out = Message.main_feed()
        assert isinstance(out, QuerySet)
        assert all(isinstance(m, Message) for m in out)
        assert list(out.values_list('author', 'text')) == [
            ('Test User2', 'Another simple test message'),
            ('Test User1', 'A simple test message'),
        ]
