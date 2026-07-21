from fastapi import WebSocket

class WebSocketManager:

    def __init__(self):

        self.connections = {}

    async def connect(self, job_id, websocket: WebSocket):

        await websocket.accept()

        self.connections[job_id] = websocket

    async def disconnect(self, job_id):

        if job_id in self.connections:

            del self.connections[job_id]

    async def send(self, job_id, data):

        ws = self.connections.get(job_id)

        if ws:

            await ws.send_json(data)

manager = WebSocketManager()