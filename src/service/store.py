from typing import Dict
from model.room import Room
from datetime import datetime
from uuid import uuid4

room_store: Dict[str, Room] = {}

def create_room(human_id: str) -> Room:
    room_id = f"room-{uuid4().hex[:8]}"
    participants = [human_id, "agent-brainstormer", "agent-critic"]
    room = Room(room_id=room_id, participants=participants, created_at=datetime.utcnow())
    room_store[room_id] = room
    return room

def get_room(room_id: str) -> Room | None:
    return room_store.get(room_id)
