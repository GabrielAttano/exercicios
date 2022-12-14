from fastapi import HTTPException

from repository.user.userRepository import UserRepository
from repository.user.userSchema import parse_user_to_schema

class UserService:
  
  @classmethod
  async def get_users(cls, ):
    userRepository = UserRepository.instance()
    if isinstance(userRepository, HTTPException):
      return userRepository
    
    return {
      "users": [parse_user_to_schema(user) for user in userRepository.get_users()]
    }

  @classmethod
  async def get_users_by_state(cls, states: list):
    if len(states) < 1:
      return HTTPException(400, "amount of states must be equal to or bigger than one.")
    
    userRepository = UserRepository.instance()
    if isinstance(userRepository, HTTPException):
      return userRepository

    users = list()
    for user in userRepository.get_users():
      parsedUser = parse_user_to_schema(user)
      if parsedUser.state in states:
        print(parsedUser)
        users.append(parsedUser)

    return users
