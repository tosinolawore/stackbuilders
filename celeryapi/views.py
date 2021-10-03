from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from tasks.task import generate_random_num
from celery.result import AsyncResult
from django.core.cache import cache

class TaskCreateView(APIView):
    """
     List all Tasks, create a task instance, initiate celery task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    # VIEW to process POST request and start Celery task
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            
            # get last saved task_id from cache
            task_id = cache.get('task_id','')

            # check if there's a current running task using fetched task_id. Return message if there is.
            if task_id and AsyncResult(task_id).status == 'PENDING':
                return Response({
                    'message': 'Task could not be started as there can only be one per time. Please try again soon.'
                })
            
            # generate random number asynchronously if serializer is valid 
            t = generate_random_num.delay()

            # set asynchronous task_id in cache
            cache.set('task_id', t.id, 150)
            
            serializer.save(task_id=t.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailsView(APIView):
    """
    Retrieve, update or delete a talk instance.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        task_id = task.task_id
        task_result = AsyncResult(task_id)
        res = {}
        
        # get the task status and result if its complete
        if task_result.status == 'SUCCESS':
            res['status'] = 'complete'
        elif task_result.status == 'PENDING':
            res['status'] = 'in_progress'

        res['name'] = task.name

        if task_result.result:
            res['result'] = task_result.result

        return Response(res)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)