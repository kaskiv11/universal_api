import unittest
from app import app


class TaskCreationTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_task(self):
        new_task_data = {
            "title": "New Task",
            "description": "This is a test task"
        }

        response = self.app.post('/api/tasks', json=new_task_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.get_json()
        self.assertIn("id", response_data)

    def test_get_tasks(self):
        response = self.app.get('/api/tasks')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
