import json
import random
import string
from models import PasswordRecord

class PasswordController:
    def __init__(self, file_path='data/passwords.json'):
        self.file_path = file_path
        self.records = self.load_data()

    def generate_password(self, length=12, use_symbols=True):
        chars = string.ascii_letters + string.digits
        if use_symbols:
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    def add_record(self, service, username, password):
        if not service or not username or not password:
            return False
        record = PasswordRecord(service, username, password)
        self.records.append(record)
        self.save_data()
        return True

    def delete_record(self, index):
        if 0 <= index < len(self.records):
            self.records.pop(index)
            self.save_data()
            return True
        return False

    def save_data(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump([r.to_dict() for r in self.records], f, indent=4)

    def load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [PasswordRecord(**d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []