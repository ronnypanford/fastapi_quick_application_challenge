import os

# api.cfg path
API_DIR = os.path.dirname((os.path.realpath(__file__))) #Where this constants file is located is in the api directory
API_CFG_FILE_NAME = 'api.cfg'
PATH_TO_API_CFG = os.path.join(API_DIR, API_CFG_FILE_NAME)




# Param names
ID = "ID"
NAME = "NAME"
WEIGHT = "WEIGHT"
DESCRIPTION = "DESCRIPTION"