# 💡 What's the Product?

- 🤝 24/7 brainstorming superteam
- 🧑‍💼 Human-in-the-center flow
- 🕵️ Agent + observer structure
- 🚀 A FastAPI-based WebSocket backend service for real-time brainstorming sessions with AI agents.

## Overview

This backend service provides the infrastructure for real-time brainstorming sessions where users can interact with AI agents. It manages room creation and real-time communication through WebSocket connections.

## Features

- Room creation with unique IDs
- WebSocket-based real-time communication
- Support for multiple participants including AI agents
- Message acknowledgment system
- CORS support for local development

## Technical Stack

- FastAPI - Modern Python web framework
- WebSockets - For real-time bidirectional communication
- Pydantic - For data validation and serialization
- Python 3.x

## Project Structure

```
src/
├── main.py           # Main application entry point and API routes
├── model/
│   └── room.py      # Data models for rooms and API requests/responses
└── service/
    └── store.py     # Room storage and management service
```

## API Endpoints

### REST Endpoints

- `POST /room/create` - Create a new room
  - Request body: `{ "participant_id": string }`
  - Response: `{ "room_id": string, "ws_url": string }`

### WebSocket Endpoints

- `WS /ws/{room_id}` - WebSocket connection for real-time communication
  - Supports message sending and acknowledgment
  - Automatically handles disconnections

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn websockets python-dotenv
   ```

3. Set up environment variables:
   ```bash
   # Create a .env file with:
   API_WS_BASE=ws://localhost:8000/ws  # Adjust as needed
   ```

4. Run the server:
   ```bash
   uvicorn src.main:app --reload
   ```

The server will start at `http://localhost:8000` by default.

## Development

- The service is configured with CORS to allow connections from `http://localhost:5173` (frontend dev server)
- Messages are acknowledged with unique IDs and timestamps
- Room IDs are generated with UUID4 and truncated for readability

## Environment Variables

- `API_WS_BASE` - Base URL for WebSocket connections (default: `ws://localhost:8000/ws`)