from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from database.database import Database
from database.repositories.contact_repository import ContactRepository
from clients.clickup_client import ClickUpClient
from clients.hubspot_client import HubSpotClient
from api.models.call_request_api import CallRequestApi
from log.logger import Logger

logger = Logger()
sync_router = APIRouter()
hubspot_client = HubSpotClient()
clickup_client = ClickUpClient()
db = Database()
contact_repository = ContactRepository(db)


@sync_router.post("/contacts")
async def sync_contacts(background_tasks: BackgroundTasks):
    try:
        contacts = HubSpotClient().get_unsynced_contacts()
        if contacts:
            background_tasks.add_task(
                sync_contacts_to_clickup_recursive, contacts)
            return JSONResponse(content={"message": "Syncing contacts in the background"}, status_code=202)
        else:
            return JSONResponse(content={"message": "No contacts to sync"}, status_code=200)
    except Exception as e:
        logger.error("An error occurred while synchronizing the data."+e)


async def sync_contacts_to_clickup_recursive(contacts):
    try:
        for contact in contacts["results"]:
            task_data = {
                "name": contact["properties"]["firstname"] if 'firstname' in contact['properties'] else "" + " " + contact['properties']['lastname'] if 'lastname' in contact['properties'] else "",
                "custom_fields": [
                    {
                        "Email": contact['properties']['email'] if 'email' in contact['properties'] else "",
                        "Phone": contact['properties']['phone'] if 'phone' in contact['properties'] else "",
                        "Website": contact['properties']['website'] if 'website' in contact['properties'] else ""
                    }
                ]
            }
            try:
                clickup_client.create_task(task_data)
            except Exception as e:
                contact_repository.create_contact(CallRequestApi(
                    endpoint="/api/v2/list/task", params=contact, result=str(e)))
            HubSpotClient().update_status_synced(contact['id'])
        # Check if there is a "next" page available
        if "paging" in contacts and "next" in contacts["paging"]:
            next_contacts = HubSpotClient().get_unsynced_contacts()
            await sync_contacts_to_clickup_recursive(next_contacts)
    except Exception as e:
        logger.error("An error occurred while synchronizing the data."+e)
