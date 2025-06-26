from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from model.room import RoomCreateRequest, RoomCreateResponse
from service.store import create_room
import json
import uuid
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow frontend dev server to connect (change this later for prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_WS_BASE = os.getenv("API_WS_BASE", "ws://localhost:8000/ws")

@app.post("/room/create", response_model=RoomCreateResponse)
def create_room_route(req: RoomCreateRequest):
    room = create_room(req.participant_id)
    ws_url = f"{API_WS_BASE}/{room.room_id}"
    return RoomCreateResponse(room_id=room.room_id, ws_url=ws_url)

@app.websocket("/ws/{room_id}")
async def websocket_room_handler(websocket: WebSocket, room_id: str):
    await websocket.accept()
    print(f"🔌 WebSocket connected to room {room_id}")

    try:
        while True:
            raw = await websocket.receive_text()
            message = json.loads(raw)

            if message.get("type") == "message":
                msg_id = f"msg-{uuid.uuid4().hex[:8]}"
                timestamp = datetime.utcnow().isoformat()
                ack = {
                    "type": "ack",
                    "message_id": msg_id,
                    "timestamp": timestamp
                }
                await websocket.send_json(ack)
                print(f"✅ Ack sent for message: {msg_id}")

    except WebSocketDisconnect:
        print(f"❌ Disconnected from room {room_id}")
