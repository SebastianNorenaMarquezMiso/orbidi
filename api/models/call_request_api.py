from pydantic import BaseModel


class CallRequestApi(BaseModel):
    endpoint: str
    params: dict
    result: str
