from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime

class RoomCreateRequest(BaseModel):
    participant_id: str

class RoomCreateResponse(BaseModel):
    room_id: str
    ws_url: str

class Room(BaseModel):
    room_id: str
    participants: list[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
