import json
from sqlalchemy.orm import Session
from api.models.call_request_api import CallRequestApi
from database.models.api_call import ApiCall


class ContactRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_contact(self, request_data: CallRequestApi) -> CallRequestApi:
        call = ApiCall()
        call.endpoint = request_data.endpoint,
        call.params = json.dumps(request_data.params)
        call.result = request_data.result
        self.db.add(call)
        self.db.commit()
        self.db.refresh(call)
        return call
