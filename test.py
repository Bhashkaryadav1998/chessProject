import unittest

from app import app
import json


class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        return app

    def test_home_get(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def test_home_post(self):
        data = [['Event1', '2021-01-01 00:00:00', '2021-01-01 00:00:01'],
                ['Event2', '2021-01-01 00:00:00', '2021-01-01 00:00:02']]
        data = json.dumps(data)
        response = self.app.post('/', data=data, content_type='application/json')
        assert response.status_code == 405
    def test_upload_empty(self):
        data=[]
        data=json.dumps(data)
        response = self.app.post('/upload', data=data, content_type='application/json')
        assert response.status_code == 302
if __name__ == '__main__':
    unittest.main()