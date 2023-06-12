import os
import requests
from dotenv import load_dotenv

load_dotenv('.env.local')


class ClickUpClient:
    def __init__(self):
        self.api_key = os.getenv("CLICKUP_API_KEY", '')
        self.base_url = os.getenv("CLICKUP_BASE_URL", '')
        self.list_id = os.getenv("CLICKUP_LIST_ID", '')

    def create_task(self, task_data):
        endpoint = f"/api/v2/list/{self.list_id}/task"
        url = self.base_url + endpoint
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key
        }
        response = requests.post(url, headers=headers, json=task_data)
        response.raise_for_status()
        return response.json()
