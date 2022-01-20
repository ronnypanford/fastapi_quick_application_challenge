from fastapi import FastAPI
from fastapi_restful import Api

from database_config import database


app = FastAPI()

api = Api(app)

import endpoints

# Create/Update database tables
database.create_models()
