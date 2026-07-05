from python.notes.notes_repository import NotesRepository


class NotesService:

    def create(self, user, note):

        repo = NotesRepository()

        repo.create_note(
            user["id"],
            note.title,
            note.content
        )

        return {
            "message": "Note Created Successfully"
        }

    def get_all(self, user):

        repo = NotesRepository()

        notes = repo.get_notes(user["id"])

        result = []

        for note in notes:

            result.append({
                "id": note[0],
                "title": note[1],
                "content": note[2],
                "created_at": note[3]
            })

        return result

    def update(self, note_id, user, note):

        repo = NotesRepository()

        repo.update_note(
            note_id,
            user["id"],
            note.title,
            note.content
        )

        return {
            "message": "Note Updated Successfully"
        }

    def delete(self, note_id, user):

        repo = NotesRepository()

        repo.delete_note(
            note_id,
            user["id"]
        )

        return {
            "message": "Note Deleted Successfully"
        }