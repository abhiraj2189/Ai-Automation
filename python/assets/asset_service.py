import os
import hashlib

from concurrent.futures import ThreadPoolExecutor, as_completed

from python.assets.pexels_service import PexelsService
from python.assets.downloader import Downloader


class AssetService:

    MAX_PARALLEL_DOWNLOADS = 5

    def __init__(self):

        self.output_dir = os.path.join(
            "outputs",
            "assets",
            "videos"
        )

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

    def _cache_filename(self, keyword, video, index):

        cleaned_keyword = "".join(
            char if char.isalnum() else "_"
            for char in str(keyword).strip().lower()
        )
        cleaned_keyword = cleaned_keyword.strip("_") or "asset"

        url = str(video.get("url", ""))
        video_id = video.get("id")

        if video_id:
            fingerprint = str(video_id)
        else:
            fingerprint = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]

        return f"{cleaned_keyword}_{fingerprint}.mp4"

    def _download_single(self, index, video, keyword):

        filename = self._cache_filename(keyword, video, index)
        output = os.path.join(self.output_dir, filename)

        if os.path.exists(output) and os.path.getsize(output) > 0:
            print(f"♻️ Using cached asset: {output}")
            return {
                "keyword": keyword,
                "path": output,
                "duration": video.get("duration", 0),
                "source": "Pexels",
                "cached": True,
            }

        try:
            Downloader.download(
                video["url"],
                output
            )
        except Exception as error:
            print(
                f"⚠️ Failed to download asset for '{keyword}' "
                f"(index {index}): {error}"
            )
            return None

        return {
            "keyword": keyword,
            "path": output,
            "duration": video.get("duration", 0),
            "source": "Pexels",
            "cached": False,
        }

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

        videos = service.search(keyword, count)

        if not videos:
            raise Exception("No videos found.")

        worker_count = min(self.MAX_PARALLEL_DOWNLOADS, len(videos))

        results = [None] * len(videos)

        with ThreadPoolExecutor(max_workers=worker_count) as executor:

            futures = {
                executor.submit(self._download_single, index, video, keyword): index
                for index, video in enumerate(videos)
            }

            for future in as_completed(futures):
                index = futures[future]
                results[index] = future.result()

        downloaded = [item for item in results if item is not None]

        if not downloaded:
            raise Exception(
                f"All video downloads failed for keyword '{keyword}'."
            )

        print(
            f"Asset Download Completed "
            f"({len(downloaded)}/{len(videos)} succeeded)"
        )

        return downloaded

    def generate(
        self,
        keyword: str,
        type: str = "video",
        count: int = 5
    ):

        return self.download(
            keyword=keyword,
            type=type,
            count=count
        )