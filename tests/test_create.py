import unittest
import os
import csv
from src.create import create_contact, CSV_FILE
 
class TestCreateContact(unittest.TestCase):
 
    def setUp(self):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone'])
 
    def tearDown(self):
        os.remove(CSV_FILE)
 
    def test_create_unique_contact(self):
        result = create_contact('Luis', '0999999999')
        self.assertTrue(result)
 
    def test_create_duplicate_phone(self):
        create_contact('Luis', '0999999999')
        result = create_contact('Ana', '0999999999')
        self.assertFalse(result)
 
if __name__ == '__main__':
    unittest.main()
