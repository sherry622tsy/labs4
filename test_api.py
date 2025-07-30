import unittest
import json
from app import app  # Import your Flask app

class TaskApiTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.client = app.test_client()
        self.base_url = '/tasks'

    def test_get_all_tasks(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertIsInstance(data['data'], list)

    def test_create_task(self):
        new_task = {
            'title': 'Test Task',
            'description': 'This is a test'
        }
        response = self.client.post(
            self.base_url,
            data=json.dumps(new_task),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['title'], 'Test Task')

    def test_get_single_task(self):
        # Create a task and get its ID
        post_response = self.client.post(
            self.base_url,
            data=json.dumps({'title': 'Temp Task'}),
            content_type='application/json'
        )
        self.assertEqual(post_response.status_code, 201)
        task_id = post_response.get_json()['data']['id']

        # Retrieve the task by ID
        response = self.client.get(f'{self.base_url}/{task_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['data']['id'], task_id)

    def test_update_task(self):
        # First, create a task
        post_response = self.client.post(
            self.base_url,
            data=json.dumps({'title': 'Old Title'}),
            content_type='application/json'
        )
        task_id = post_response.get_json()['data']['id']
        print(f'{self.base_url}/{task_id}')
        # Update the task
        update_data = {'title': 'Updated Title', 'done': True}
        update_response = self.client.put(
            f'{self.base_url}/{task_id}',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        self.assertEqual(update_response.status_code, 200)
        data = update_response.get_json()
        self.assertEqual(data['data']['title'], 'Updated Title')
        self.assertTrue(data['data']['done'])

    def test_delete_task(self):
        # Create a task
        post_response = self.client.post(
            self.base_url,
            data=json.dumps({'title': 'Delete Me'}),
            content_type='application/json'
        )
        task_id = post_response.get_json()['data']['id']

        # delete the task
        delete_response = self.client.delete(f'{self.base_url}/{task_id}')
        self.assertEqual(delete_response.status_code, 200)

        # Confirm the task was deleted
        get_response = self.client.get(f'{self.base_url}/{task_id}')
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
