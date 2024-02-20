from pydantic import BaseModel

class PostHelloWorld(BaseModel):
    data: str