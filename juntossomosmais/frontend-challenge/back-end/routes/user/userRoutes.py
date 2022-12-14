from fastapi import APIRouter
from pydantic import BaseModel

from service.user.userService import UserService

userRouter = APIRouter()

class get_user_parameters(BaseModel):
  states: list

@userRouter.get('/users')
async def get_users(parameters: get_user_parameters):
  if not parameters.states:
    return await UserService.get_users()
  else:
    print(parameters.states)
    return await UserService.get_users_by_state(parameters.states)

