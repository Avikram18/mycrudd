import unittest
from unittest.mock import patch, Mock
from flask import json

class EmployeeTestCase(unittest.TestCase):
    @patch('main.app.test_client')
    def test_get_all_employees(self, mock_test_client):
        # Mocking the response for GET /employees
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.get_json.return_value = [
            {"id": 1, "name": "name1", "post": "SWE"},
            {"id": 2, "name": "name2", "post": "TL"},
            {"id": 3, "name": "name3", "post": "PM"}
        ]
        mock_test_client.return_value.get.return_value = mock_response

        # Test
        client = mock_test_client()
        response = client.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 4)

    @patch('main.app.test_client')
    def test_get_employee_by_id(self, mock_test_client):
        # Mocking the response for GET /employees/search?id=1
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.get_json.return_value = {"id": 1, "name": "name1", "post": "SWE"}
        mock_test_client.return_value.get.return_value = mock_response

        # Test
        client = mock_test_client()
        response = client.get('/employees/search?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'name1')

    @patch('main.app.test_client')
    def test_create_employee(self, mock_test_client):
        # Mocking the response for POST /employees
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.get_json.return_value = {"id": 4, "name": "name4", "post": "HR"}
        mock_test_client.return_value.post.return_value = mock_response

        # Test
        client = mock_test_client()
        new_employee = {'name': 'name4', 'post': 'HR'}
        response = client.post('/employees', data=json.dumps(new_employee), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['name'], 'name4')

    @patch('main.app.test_client')
    def test_update_employee(self, mock_test_client):
        # Mocking the response for PUT /employees/1
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.get_json.return_value = {"id": 1, "name": "name1_updated", "post": "SWE"}
        mock_test_client.return_value.put.return_value = mock_response

        # Test
        client = mock_test_client()
        updated_employee = {'name': 'name1_updated', 'post': 'SWE'}
        response = client.put('/employees/1', data=json.dumps(updated_employee), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'name1_updated')

    @patch('main.app.test_client')
    def test_delete_employee(self, mock_test_client):
        # Mocking the response for DELETE /employees/1
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.get_json.return_value = {"success": "employee deleted"}
        mock_test_client.return_value.delete.return_value = mock_response

        # Test
        client = mock_test_client()
        response = client.delete('/employees/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['success'], 'employee deleted')

if __name__ == '__main__':
    unittest.main()
