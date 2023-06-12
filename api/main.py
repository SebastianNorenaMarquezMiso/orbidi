import uvicorn
from fastapi import FastAPI
from endpoints.hubspot_endpoint import hubspot_router
from endpoints.sync_endpoint import sync_router

app = FastAPI()

app.include_router(hubspot_router, prefix="/hubspot", tags=["HubSpot"])
app.include_router(sync_router, prefix="/sync", tags=["Sync"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
