from django.test import TestCase
import pytest
from celeryapi.models import Task
from rest_framework.views import status
from django.urls import reverse


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()

@pytest.fixture
def test_task():
    task = Task(name='any string',)
    task.save()
    return task


# Tests that the Task Model can create objects.
@pytest.mark.django_db
def test_task_count():
    """Tests that the Task Model can create objects."""

    task = Task(name='any string',)
    task.save()
    assert Task.objects.count() == 1


# Tests API POST View.
@pytest.mark.django_db
def test_api_start_task(api_client):
    """Tests the POST VIEW and immediate return."""

    response = api_client.post(reverse('create_task'), {"name":"some string"}, format="json")
    assert response.status_code == status.HTTP_201_CREATED


# Tests API GET View.
@pytest.mark.django_db
def test_api_get_task(api_client,test_task):
    """Tests the GET VIEW."""

    response = api_client.get('/tasks/', kwargs={'pk': test_task.id}, format="json")

    assert response.status_code, status.HTTP_200_OK


# Tests API UPDATE View.
@pytest.mark.django_db
def test_api_update_task(api_client, test_task):
    """Tests the UPDATE VIEW."""

    response = api_client.put(reverse('task_details',kwargs={'pk': test_task.id}),
            {"name":"new string"}, format="json")
    assert response.status_code == status.HTTP_200_OK


# Tests API DELETE View.
@pytest.mark.django_db
def test_api_delete_task(api_client,test_task):
    """Tests the DELETE VIEW."""

    response = api_client.delete(reverse('task_details',kwargs={'pk': test_task.id}), format="json", follow=True)
    assert response.status_code == status.HTTP_204_NO_CONTENT
