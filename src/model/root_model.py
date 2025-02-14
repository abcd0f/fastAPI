from pydantic import BaseModel, Field


class RootModel(BaseModel):
    title: str = Field("", max_length=100)
    txt: str = Field("", max_length=1000)
