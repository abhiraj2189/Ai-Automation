from python.favorites.favorites_repository import FavoritesRepository


class FavoritesService:

    def add(self, user, favorite):

        repo = FavoritesRepository()

        repo.add_favorite(
            user["id"],
            favorite.tool_name,
            favorite.website
        )

        return {
            "message": "Favorite Added Successfully"
        }

    def get_all(self, user):

        repo = FavoritesRepository()

        data = repo.get_favorites(user["id"])

        result = []

        for item in data:

            result.append({
                "id": item[0],
                "tool_name": item[1],
                "website": item[2],
                "created_at": item[3]
            })

        return result

    def delete(self, favorite_id, user):

        repo = FavoritesRepository()

        repo.delete_favorite(
            favorite_id,
            user["id"]
        )

        return {
            "message": "Favorite Deleted Successfully"
        }