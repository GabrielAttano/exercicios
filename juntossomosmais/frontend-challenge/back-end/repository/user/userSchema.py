from pydantic import BaseModel

class UserSchema(BaseModel):
  fullName: str
  street: str
  city: str
  state: str
  postcode: int
  picture: dict

def parse_user_to_schema(user: dict):
  name = user["name"]
  location = user["location"]
  pictures = user["picture"]

  return UserSchema(
    fullName = name["first"] + " " + name["last"],
    street = location["street"],
    city = location["city"],
    state = location["state"],
    postcode = location["postcode"],
    picture = {
      "large": pictures["large"],
      "medium": pictures["medium"],
      "thumbnail": pictures["thumbnail"]
    }
  )