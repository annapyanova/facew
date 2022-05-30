import sys
import os

sys.path.append(sys.path[0][0:sys.path[0].rindex(os.sep)])


from app import app

class TestHtml:

    def setup(self):
        app.testing = True
        self.client = app.test_client()

    def test_index(self):
        response=self.client.get("/index")
        assert response.status_code == 200
        assert response.content_type == "text/html; charset=utf-8"

    def test_login(self):
        response=self.client.get("/login")
        assert response.status_code == 200
        assert response.content_type == "text/html; charset=utf-8"
    
