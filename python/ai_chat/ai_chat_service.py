import ollama

from python.ai_chat.ai_chat_repository import AIChatRepository


class AIChatService:

    def chat(self, user, data):

        response = ollama.chat(

            model="llama3.2:3b",

            messages=[

                {
                    "role": "user",
                    "content": data.message
                }

            ]

        )

        answer = response["message"]["content"]

        repo = AIChatRepository()

        repo.save_chat(
            user["id"],
            data.conversation_id,
            data.message,
            answer
        )

        return {
            "question": data.message,
            "answer": answer
        }

    def history(self, user):

        repo = AIChatRepository()

        data = repo.get_history(user["id"])

        result = []

        for item in data:

            result.append({

                "id": item[0],
                "conversation_id": item[1],
                "question": item[2],
                "answer": item[3],
                "created_at": item[4]

            })

        return result

    def conversations(self, user):

        repo = AIChatRepository()

        data = repo.get_conversations(user["id"])

        result = []

        for item in data:

            result.append({

                "conversation_id": item[0],
                "title": item[1]

            })

        return result

    def delete(self, user, conversation_id):

        repo = AIChatRepository()

        repo.delete_conversation(
            user["id"],
            conversation_id
        )

        return {
            "message": "Conversation Deleted Successfully"
        }