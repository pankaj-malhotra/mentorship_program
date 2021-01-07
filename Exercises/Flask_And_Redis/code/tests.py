import unittest
import random
import json
from students import app


class MyTestCase(unittest.TestCase):

    # Ensure the API returns correct response
    def test_api_response(self):
            tester = app.test_client(self)
            response = tester.get('/students')

            self.assertEqual(response.status_code, 200)

    # Ensure the API returns correct data
    def test_api_data(self):
            #import ipdb;
            #ipdb.set_trace()

            tester = app.test_client(self)
            response = tester.get('/students')

            self.assertTrue('students' in str(response.data))

    # Ensure API post & delete methods are working fine
    def test_api_post_delete(self):
            tester = app.test_client(self)

            #Get Students List
            response = tester.get('/students')
            rollNo = len(students_list(response)) + 1

            response = tester.post('/student/' + str(rollNo),
                    data = {'name': 'Manoj', 'age': 22, 'gender': 'Male'})
            self.assertIn(b'Manoj', response.data)

            response = tester.delete('/student/' + str(rollNo))
            self.assertIn(b'Student with rollNo', response.data)


def students_list(response):
    json_data = json.loads(response.data)
    json_dic = dict(json_data)

    if json_dic['students']:
        return json_dic['students']
    else:
        return []


if __name__ == '__main__':
    unittest.main()
