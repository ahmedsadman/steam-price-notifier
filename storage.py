import csv
import os

FILENAME = 'data.csv'

class Storage:
    def __init__(self):
        self.fields = ['app_id', 'name', 'price']
        self._ensure_storage()

    def _get_reader(self, file):
        return csv.DictReader(file)

    def _get_writer(self, file):
        return csv.DictWriter(file, self.fields)

    def _ensure_storage(self):
        if not os.path.exists(FILENAME):
            with open(FILENAME, 'w', newline='') as f:
                writer = self._get_writer(f)
                writer.writeheader()

    def _get_existing_data(self):
        with open(FILENAME, 'r', newline='') as f:
            reader = self._get_reader(f)
            return [row for row in reader]

    def _write(self, rows):
        with open(FILENAME, 'w', newline='') as f:
            writer = self._get_writer(f)
            writer.writeheader()
            writer.writerows(rows)

    def get(self, app_id):
        data = self._get_existing_data()
        for item in data:
            if item['app_id'] == app_id:
                return item
        return None

    def upsert(self, app_id, name, new_price):
        found = False
        data = self._get_existing_data()
        for item in data:
            if item['app_id'] == app_id:
                item['price'] = new_price
                found = True
                break
        
        if not found:
            data.append({'app_id': app_id, 'name': name, 'price': new_price})

        self._write(data)

