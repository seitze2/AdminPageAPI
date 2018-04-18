import unittest

from AdminPage.AdminPageAPI.adminPage import testReadJSON
from AdminPage.AdminPageAPI.adminPage import testAdmin


#Stubbed tests of the two main functions in the API

class TestAdminAPI(unittest.TestCase):

    def test_json_parse(self):
        data = testReadJSON()

        result = False

        if(data.__len__() > 0):
              result = True

        self.assertTrue(result)

    def test_render(self):
        result = testAdmin()

        self.assertTrue(result)
