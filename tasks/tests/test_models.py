import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestTask:
    def test_model(self):
        obj = mixer.blend('tasks.Task')
        assert obj.pk == 1, 'Should create a task instance'
