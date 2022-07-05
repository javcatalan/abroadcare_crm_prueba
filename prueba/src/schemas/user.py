
def userEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "uuidApplication": item["uuidApplication"],
        "uuidQuestion": item["uuidQuestion"],
        "responseOptions": item["responseOptions"],
        "responseSpecify": item["responseSpecify"],
    }


def appicationEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "uuid": item["uuid"],
        "firstName": item["firstName"],
        "lastName": item["lastName"],
        "countryCode": item["lastName"],
        "phoneNumber": item["phoneNumber"],
        "email": item["email"],
        "history": item["history"],
        "utmData": item["utmData"]
    }

def questionEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "uuid": item["uuid"],
        "question": item["question"],
        "commentary": item["commentary"],
        # "options": str(item["options"]),
        # "specify": item["specify"],
        # "specifyWhen": str(item["specifyWhen"]),
        # "responseOptions": item["responseOptions"],
        "responseSpecify": item["responseSpecify"],
        "responseSpecifyType": item["responseSpecifyType"],
        "tags": item["tags"],
        "isOpen": item["isOpen"],
        "placeholder": item["placeholder"]

    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def questionsEntity(question) -> list:
    return [questionEntity(item) for item in question]

def appicationsEntity(applications) -> list:
    return [appicationEntity(item) for item in applications]

    
# def userEntity(item) -> dict:
#     return{
#         "id": str(item["_id"]),
#         "name": item["name"],
#         "email": item["email"],
#         "password": item["password"]
#     }

# def usersEntity(entity) -> list:
#     return [userEntity(item) for item in entity]