from app import api
from resources.users import Users


api.add_resource(Users(), "/users",  "/users/{action}", "/users/{action}/{ID}")