import unittest
import json
from main import app

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_employees(self):
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 3)

    def test_get_employee_by_id(self):
        response = self.app.get('/employees/search/?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'name1')

    def test_get_employee_by_name(self):
        # response=self.app.get('http://127.0.0.1:5000/employees/search?name=name1')
        response = self.app.get('/employees/search/?name=name1')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['post'], 'SWE')

    def test_create_employee(self):
        new_employee = {'name': 'name4', 'post': 'HR'}
        response = self.app.post('/employees', data=json.dumps(new_employee), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'name4')

    def test_update_employee(self):
        updated_employee = {'name': 'name1_updated', 'post': 'SWE'}
        response = self.app.put('/employees/1', data=json.dumps(updated_employee), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'name1_updated')

    def test_delete_employee(self):
        response = self.app.delete('/employees/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['success'], 'employee deleted')

if __name__ == '__main__':
    unittest.main()
 