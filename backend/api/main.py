from fastapi import FastAPI

from api.routers import records, problems

app = FastAPI()
app.include_router(records.router)
app.include_router(problems.router)
