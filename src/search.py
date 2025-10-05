import csv

CSV_FILE = 'contacts.csv'

def read_contacts():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def search_contact(query):
    contacts = read_contacts()
    return [c for c in contacts if c['Name'] == query or c['Phone'] == query]
