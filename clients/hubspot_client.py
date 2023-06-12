import os
import requests
from api.models.contact_search_request import ContactSearchRequest, FilterGroup, Filter
from dotenv import load_dotenv

load_dotenv('.env.local')


class HubSpotClient:
    def __init__(self):
        self.api_key = os.getenv("HUBSPOT_API_KEY",'')
        self.base_url = os.getenv("HUBSPOT_BASE_URL",'https://test')
        self.status_pending = os.getenv("HUBSPOT_STATUS_PENDING",'')
        self.status_added = os.getenv("HUBSPOT_STATUS_ADDED",'')

    def create_contact(self, contact_data):
        endpoint = "/crm/v3/objects/contacts"

        url = self.base_url + endpoint
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(url, headers=headers,
                                 json=contact_data.dict())
        response.raise_for_status()
        return response.json()

    def update_status_synced(self, contact_id):
        endpoint = f"/crm/v3/objects/contacts/{contact_id}"
        url = self.base_url + endpoint
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.patch(url, headers=headers, json={
                                  "properties": {"estado_clickup": self.status_added}})
        response.raise_for_status()
        return response.json()

    def get_unsynced_contacts(self):
        endpoint = "/crm/v3/objects/contacts/search"
        url = self.base_url + endpoint
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        contact_search_request = ContactSearchRequest(
            filterGroups=[
                FilterGroup(
                    filters=[
                        Filter(
                            value=self.status_pending,
                            propertyName="estado_clickup",
                            operator="EQ"
                        )
                    ]
                )
            ]
        )
        response = requests.post(url, headers=headers,
                                 json=contact_search_request.dict())
        response.raise_for_status()
        return response.json()
