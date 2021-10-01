from django.test import TestCase
from tasks.task import generate_random_num
from unittest.mock import patch

@patch("tasks.task.generate_random_num.run")
def test_task(mock_run):
    assert generate_random_num.run()
    assert generate_random_num.run.call_count == 1
