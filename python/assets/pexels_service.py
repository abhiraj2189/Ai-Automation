import requests

from python.config.settings import settings


class PexelsService:

    BASE_URL = "https://api.pexels.com/videos/search"

    def search(
        self,
        keyword: str,
        count: int = 5
    ):

        headers = {
            "Authorization": settings.PEXELS_API_KEY
        }

        params = {
            "query": keyword,
            "per_page": count
        }

        response = requests.get(
            self.BASE_URL,
            headers=headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        videos = []

        for video in data.get("videos", []):

            if not video.get("video_files"):
                continue

            best = max(
                video["video_files"],
                key=lambda x: x.get("width", 0)
            )

            videos.append({
                "id": video["id"],
                "duration": video["duration"],
                "url": best["link"],
                "width": best["width"],
                "height": best["height"]
            })

        return videos