import csv
import os

CSV_FILE = 'contacts.csv'

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone'])

def read_contacts():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def contact_exists(phone):
    return any(c['Phone'] == phone for c in read_contacts())

def create_contact(name, phone):
    initialize_csv()
    if contact_exists(phone):
        return False
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
        return True
