import requests

from python.config.settings import settings


class PexelsService:

    BASE_URL = "https://api.pexels.com/videos/search"

    def search(
        self,
        keyword: str,
        count: int = 5
    ):

        print(f"Searching Pexels for: {keyword}")

        headers = {
            "Authorization": settings.PEXELS_API_KEY
        }

        params = {
            "query": keyword,
            "per_page": min(count * 3, 30)
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

        used = set()

        for video in data.get("videos", []):

            files = video.get("video_files", [])

            if not files:
                continue

            # Highest Resolution
            files = sorted(
                files,
                key=lambda x: (
                    x.get("width", 0),
                    x.get("height", 0)
                ),
                reverse=True
            )

            best = None

            for f in files:

                width = f.get("width", 0)
                height = f.get("height", 0)

                if width >= 720:

                    best = f
                    break

            if best is None:
                best = files[0]

            url = best["link"]

            if url in used:
                continue

            used.add(url)

            videos.append({

                "id": video["id"],

                "duration": video.get(
                    "duration",
                    0
                ),

                "url": url,

                "width": best.get(
                    "width",
                    0
                ),

                "height": best.get(
                    "height",
                    0
                ),

                "quality": "HD"

            })

            if len(videos) >= count:
                break

        print(f"Found {len(videos)} HD videos.")

        return videos