from pydantic import BaseModel


class Response(BaseModel):
    code: int
    type: str
    message: str
