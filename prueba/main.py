# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"hello": "world"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None]= None):
#     return {"item_id": item_id, "q": q}}


from fastapi import FastAPI
from src.routes.user import user
from fastapi.middleware import CORSMiddleware

app = FastAPI(
    title="Rest API with FastAPI and Mongodb",
    description= "API for Abroadcare",
    version="0.0.01"
)

origins = [
    "hhtp://127.0.0.1:8000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(user)

