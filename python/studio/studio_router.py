from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import WebSocket
from python.studio.jobs.websocket_manager import manager
from python.studio.jobs.job_manager import JobManager
from python.studio.studio_service import StudioService
from fastapi import WebSocket
from python.studio.websocket_manager import manager
from python.jobs.job_manager import JobManager


router = APIRouter(

    prefix="/studio",

    tags=["AI Studio"]

)


class StudioRequest(BaseModel):

    topic: str


@router.post("/")

def generate(

    data: StudioRequest

):

    service = StudioService()

    return service.generate(

        topic=data.topic

    )
@router.websocket("/ws/{job_id}")

async def workflow_socket(

    websocket: WebSocket,

    job_id: str

):

    await manager.connect(

        job_id,

        websocket

    )

    try:

        while True:

            status = JobManager.status(job_id)

            await manager.send(

                job_id,

                status

            )

            import asyncio

            await asyncio.sleep(1)

    except:

        await manager.disconnect(job_id)

    @router.websocket("/ws/{job_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    job_id: str
):

    await manager.connect(
        job_id,
        websocket
    )

    try:

        while True:

            status = JobManager.get(job_id)

            if status:

                await manager.send_progress(
                    job_id,
                    status
                )

            import asyncio

            await asyncio.sleep(1)


    except Exception:

        manager.disconnect(job_id)