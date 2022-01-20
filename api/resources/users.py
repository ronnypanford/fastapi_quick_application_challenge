from fastapi.responses import JSONResponse
from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, Body
from fastapi_restful import Resource
from database_config.database import db_session
from services import user_service


class Users(Resource):


    def post(self, NAME: str = Body(...), WEIGHT: float = Body(...), DESCRIPTION: Optional[str] = Body(...), session: Session = Depends(db_session) ):
        
        user = user_service.create_user( session, NAME, WEIGHT, DESCRIPTION)

        if user:
            response_data = jsonable_encoder(user)
            response = JSONResponse(content=response_data)
            response.status_code = 200
        else:
            response = JSONResponse(content={"message":"could not create user"})
            response.status_code = 400

        return response


    def get(self, action: str, ID: Optional[int] = None, session: Session = Depends(db_session)):

        if action == "all":
            users = user_service.get_all_users( session )

            response_data = jsonable_encoder(users)
            response = JSONResponse(content=response_data)
            response.status_code = 200
        
        elif action == "user":
            user = user_service.get_user_by_id( session, ID)

            if user:
                response_data = jsonable_encoder(user)
                response = JSONResponse(content=response_data)
                response.status_code = 200
            else:
                response = JSONResponse(content={"message":"could not find user"})
                response.status_code = 400
        else:
            response = JSONResponse(content={"message":"invalid route"})
            response.status_code = 400

        
        return response


    def put(self, action: str, ID: int, NAME: Optional[str] = Body(...), WEIGHT: Optional[float] = Body(...), DESCRIPTION: Optional[str] = Body(...), session: Session = Depends(db_session) ):

        if action == "user":
            user = user_service.edit_user( session, ID, NAME, WEIGHT, DESCRIPTION)

            if user:
                response_data = jsonable_encoder(user)
                response = JSONResponse(content=response_data)
                response.status_code = 200
            else:
                response = JSONResponse(content={"message":"could not find user"})
                response.status_code = 400
        else:
            response = JSONResponse(content={"message":"invalid route"})
            response.status_code = 400

        return response


    def delete(self, action: str, ID: Optional[int] = None, session: Session = Depends(db_session) ):

        if action == "all":
            deleted = user_service.delete_all_users( session)

            if deleted:
                response = JSONResponse(content={"message":"all users deleted"})
                response.status_code = 200
            else:
                response = JSONResponse(content={"message":"no users exist"})
                response.status_code = 400

            return response
        elif action == "user":
            deleted = user_service.delete_user( session, ID)

            if deleted:
                response = JSONResponse(content={"message":"user deleted"})
                response.status_code = 200
            else:
                response = JSONResponse(content={"message":"could not find user"})
                response.status_code = 400

        else:
            response = JSONResponse(content={"message":"invalid route"})
            response.status_code = 400
        
        return response
