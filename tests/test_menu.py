import unittest
from unittest.mock import patch
import os
import csv
from src.create import CSV_FILE
from src.main import menu

class TestMenuIntegration(unittest.TestCase):

    def setUp(self):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone'])

    def tearDown(self):
        os.remove(CSV_FILE)

    @patch('builtins.input', side_effect=['1', 'Luis', '0999999999', '3'])
    def test_create_contact_via_menu(self, mock_input):
        with patch('builtins.print') as mock_print:
            menu()
            output = [call.args[0] for call in mock_print.call_args_list]
            self.assertIn("✅ Contacto creado.", output)

    @patch('builtins.input', side_effect=['2', 'Luis', '3'])
    def test_search_contact_via_menu(self, mock_input):
        # Precrear contacto
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Luis', '0999999999'])
        with patch('builtins.print') as mock_print:
            menu()
            output = [call.args[0] for call in mock_print.call_args_list]
            self.assertIn("Luis - 0999999999", output)


if __name__ == '__main__':
    unittest.main()
