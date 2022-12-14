import requests
from fastapi import HTTPException

class UserRepository:
  _instance = None

  def __init__(self, ):
    self._users = list()

  @classmethod
  def _load_users(cls, ):
    url = "https://jsm-challenges.s3.amazonaws.com/frontend-challenge.json"
    response = requests.get(url)
    if response.status_code == 200:
      users = response.json()["results"]
      return users

    return None 

  @classmethod
  def instance(cls, ):
    if cls._instance is None:
      cls._instance = cls()
      users = cls._load_users()
      if users is None:
        return HTTPException(503, "failed to load users.")
      cls._instance._users = users

    return cls._instance


  def get_users(self, ):
    return self._users

