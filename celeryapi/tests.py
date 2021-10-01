from django.test import TestCase
import pytest
from celeryapi.models import Task


@pytest.mark.django_db
def test_task_count():
    """Tests that the Task Model can create objects."""
    task = Task(name='any string', task_id='any_string_of_numbers')
    task.save()
    assert Task.objects.count() == 1
