from django.test import TestCase
from django_starter.models import Task
from django_starter.forms import TaskForm
from django.utils import timezone

class ModelsTest(TestCase):
  def create_task(self, content='only a test'):
    return Task.objects.create(content=content, created=timezone.now(), updated=timezone.now())

  def test_task_creation(self):
    t = self.create_task()
    self.assertTrue(isinstance(t, Task))
    self.assertEqual('only a test', t.content)
