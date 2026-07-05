from fastapi import APIRouter, Depends

from python.schemas.favorite_schema import FavoriteSchema
from python.auth.auth_dependency import get_current_user
from python.favorites.favorites_service import FavoritesService

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
)


@router.post("")
def add_favorite(
    favorite: FavoriteSchema,
    user=Depends(get_current_user)
):

    service = FavoritesService()

    return service.add(user, favorite)


@router.get("")
def get_favorites(
    user=Depends(get_current_user)
):

    service = FavoritesService()

    return service.get_all(user)


@router.delete("/{favorite_id}")
def delete_favorite(
    favorite_id: int,
    user=Depends(get_current_user)
):

    service = FavoritesService()

    return service.delete(
        favorite_id,
        user
    )