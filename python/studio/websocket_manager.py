from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):

        self.active_connections = {}


    async def connect(
        self,
        job_id: str,
        websocket: WebSocket
    ):

        await websocket.accept()

        self.active_connections[job_id] = websocket



    def disconnect(self, job_id):

        if job_id in self.active_connections:

            del self.active_connections[job_id]



    async def send_progress(
        self,
        job_id,
        data
    ):

        websocket = self.active_connections.get(job_id)

        if websocket:

            await websocket.send_json(data)



manager = ConnectionManager()