import json
import os
from datetime import datetime

class PasswordRecord:
    def __init__(self, service, username, password, created_at=None):
        self.service = service
        self.username = username
        self.password = password
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return self.__dict__