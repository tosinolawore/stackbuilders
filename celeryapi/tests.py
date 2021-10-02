from django.test import TestCase
import pytest
from celeryapi.models import Task
from rest_framework.views import status
from django.urls import reverse


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()

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
def test_api_start_task(api_client):
    """Tests the GET VIEW."""

    task = Task.objects.get()
    response = api_client.get('/tasks/', kwargs={'pk': task.id}, format="json")

    assert response.status_code, status.HTTP_200_OK
    assert response, task


# Tests API UPDATE View.
@pytest.mark.django_db
def test_api_start_task(api_client):
    """Tests the UPDATE VIEW."""

    response = api_client.post(reverse('task_details'), {"name":"some string"}, format="json")
    assert response.status_code == status.HTTP_201_CREATED


# Tests API DELETE View.
@pytest.mark.django_db
def test_api_start_task(api_client):
    """Tests the DELETE VIEW."""

    response = api_client.post(reverse('create_task'), {"name":"some string"}, format="json")
    assert response.status_code == status.HTTP_201_CREATED
