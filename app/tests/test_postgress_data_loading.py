import unittest
from helper import insert_data_to_postgress, get_vehicle_data


class TestPostgressInsert(unittest.TestCase):

    def setUp(self):
        self.data = get_vehicle_data()

    def test_show_skip_if(self):
        print("Length of data is " + str(len(self.data.index)))
        insert_data_to_postgress("test", self.data)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()