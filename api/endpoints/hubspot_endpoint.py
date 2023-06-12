from database.database import Database
from api.models.contact import ContactCreateRequest
from database.repositories.contact_repository import ContactRepository
from clients.hubspot_client import HubSpotClient
from api.models.call_request_api import CallRequestApi
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from log.logger import Logger
logger = Logger()

db = Database()
hubspot_router = APIRouter()
hubspot_client = HubSpotClient()
contact_repository = ContactRepository(db)


@hubspot_router.post("/contacts")
def create_contact(contact: ContactCreateRequest):
    try:
        hubspot_client.create_contact(contact)
        logger.info("The HubSpot request was successfully completed.")
        return JSONResponse(content={"message": "Contact created successfully"}, status_code=201)
    except Exception as e:
        logger.error("An error occurred while processing the HubSpot request.")
        contact_repository.create_contact(CallRequestApi(
            endpoint="/crm/v3/objects/contacts", params=contact.dict(), result=str(e)))
        raise HTTPException(status_code=500, detail="Error creating contact")
