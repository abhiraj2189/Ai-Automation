import os

from python.assets.pexels_service import PexelsService
from python.assets.downloader import Downloader


class AssetService:

    def download(
        self,
        keyword: str,
        type: str = "video",
        count: int = 5
    ):

        if type != "video":
            raise Exception("Currently only video assets are supported.")

        service = PexelsService()

        print(f"Searching {count} videos for: {keyword}")

        videos = service.search(
            keyword,
            count
        )

        if not videos:
            raise Exception("No videos found from Pexels.")

        downloaded = []

        output_dir = os.path.join(
            "outputs",
            "assets",
            "videos"
        )

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        for index, video in enumerate(videos):

            filename = f"{keyword}_{index}.mp4"

            filename = filename.replace(" ", "_")

            output = os.path.join(
                output_dir,
                filename
            )

            print(f"Downloading {filename}...")

            Downloader.download(
                video["url"],
                output
            )

            downloaded.append({

                "keyword": keyword,

                "path": output,

                "duration": video.get("duration", 0),

                "source": "Pexels"

            })

        print("Asset Download Completed")

        return downloaded


    # Backward compatibility
    def generate(
        self,
        keyword,
        count
    ):

        return self.download(
            keyword=keyword,
            count=count
        )