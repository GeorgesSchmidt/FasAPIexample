from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    content: str

class NoteOut(NoteBase):
    id: int

    model_config = {"from_attributes": True}
