import os

from python.assets.pexels_service import PexelsService
from python.assets.downloader import Downloader


class AssetService:

    def generate(
        self,
        keyword,
        count
    ):

        service = PexelsService()

        videos = service.search(
            keyword,
            count
        )

        downloaded = []

        for index, video in enumerate(videos):

            filename = f"{keyword}_{index}.mp4"

            filename = filename.replace(" ", "_")

            output = os.path.join(
                "outputs",
                "assets",
                "videos",
                filename
            )

            Downloader.download(
                video["url"],
                output
            )

            downloaded.append({

                "keyword": keyword,

                "path": output,

                "duration": video["duration"]

            })

        return downloaded