from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    task_id = models.CharField(max_length=200)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
