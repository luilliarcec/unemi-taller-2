import unittest
import os
import csv
from search import search_contact, CSV_FILE
 
class TestSearchContact(unittest.TestCase):
 
    def setUp(self):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone'])
            writer.writerow(['Luis', '0999999999'])
            writer.writerow(['Ana', '0888888888'])
 
    def tearDown(self):
        os.remove(CSV_FILE)
 
    def test_search_by_name(self):
        results = search_contact('Luis')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['Phone'], '0999999999')
 
    def test_search_by_phone(self):
        results = search_contact('0888888888')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['Name'], 'Ana')
 
    def test_search_not_found(self):
        results = search_contact('0000000000')
        self.assertEqual(len(results), 0)
 
if _name_ == '_main_':
    unittest.main()
