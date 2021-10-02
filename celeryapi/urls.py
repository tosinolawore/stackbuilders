from django.urls import path, re_path
from .views import TaskCreateView, TaskDetailsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/', TaskCreateView.as_view(), name="create_task"),
    re_path(r'^tasks/(?P<pk>[0-9]+)/$',
        TaskDetailsView.as_view(), name="task_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)