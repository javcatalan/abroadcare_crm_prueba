
from fastapi import APIRouter, Response, status
from src.config.db import conn
from src.schemas.user import userEntity, usersEntity, appicationsEntity, questionsEntity, appicationEntity
from src.models.user import survey, applications,questions
from passlib.hash import sha256_crypt
from bson import  ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

#find users in survey
@user.get('/users', response_model=list, tags=["users"])
def find_survey():
    return usersEntity(conn.hairTransplant.survey.find())

#find users in applications
@user.get('/application', response_model=list, tags=["users"])
def find_application():
    return appicationsEntity(conn.hairTransplant.applications.find())

#find users in questions
@user.get('/questions' , response_model=list, tags=["users"])
def find_questions():
    return questionsEntity(conn.hairTransplant.questions.find())

# find user in application by id
# @user.get('/users/{id}', response_model=applications, tags=["users"])
# def find_user(id:str):
#     return appicationEntity(conn.hairTransplant.applications.find_one({"id": ObjectId(id)}))

#find user in application by uuid
@user.get('/users/{uuid}', response_model=applications, tags=["users"])
def find_user(uuid:str):
    return appicationEntity(conn.hairTransplant.applications.find_one({"uuid": uuid}))


# @user.get('/users', response_model=list, tags=["users"])
# def find_all_user():
#     return usersEntity(conn.local.user.find())

# @user.post('/users', response_model=User, tags=["users"])
# def create_user(user: User):
#     new_user = dict(user)
#     new_user["password"] = sha256_crypt.encrypt(new_user["password"])
#     del new_user["id"]
    
#     id = conn.local.user.insert_one(new_user).inserted_id

#     user = conn.local.user.find_one({"_id": id})
#     return userEntity(user)
    

# @user.get('/users/{id}', response_model=User, tags=["users"])
# def find_user(id:str):
#     return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

# @user.put('/users/{id}', response_model=User, tags=["users"])
# def update_user(id: str, user:User):
#     conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
#     return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

# @user.delete('/users{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
# def delete_user(id: str):
#     userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
#     return Response(status_code=HTTP_204_NO_CONTENT)
