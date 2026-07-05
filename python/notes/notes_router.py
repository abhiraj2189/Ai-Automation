from fastapi import APIRouter, Depends

from python.auth.auth_dependency import get_current_user
from python.schemas.note_schema import NoteSchema
from python.notes.notes_service import NotesService

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.post("")
def create_note(
    note: NoteSchema,
    user=Depends(get_current_user)
):

    service = NotesService()

    return service.create(user, note)


@router.get("")
def get_notes(
    user=Depends(get_current_user)
):

    service = NotesService()

    return service.get_all(user)


@router.put("/{note_id}")
def update_note(
    note_id: int,
    note: NoteSchema,
    user=Depends(get_current_user)
):

    service = NotesService()

    return service.update(
        note_id,
        user,
        note
    )


@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    user=Depends(get_current_user)
):

    service = NotesService()

    return service.delete(
        note_id,
        user
    )