import os
import time
import requests


class Downloader:

    CHUNK_SIZE = 1024 * 1024  # 1 MB

    @staticmethod
    def download(
        url: str,
        output: str,
        retries: int = 3
    ):

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )

        # Already downloaded
        if os.path.exists(output):

            size = os.path.getsize(output)

            if size > 1024:
                print(f"Already Exists : {output}")
                return output

        attempt = 0

        while attempt < retries:

            try:

                print(f"Downloading : {os.path.basename(output)}")

                response = requests.get(
                    url,
                    stream=True,
                    timeout=120
                )

                response.raise_for_status()

                total = int(
                    response.headers.get(
                        "content-length",
                        0
                    )
                )

                downloaded = 0

                with open(output, "wb") as file:

                    for chunk in response.iter_content(
                        Downloader.CHUNK_SIZE
                    ):

                        if not chunk:
                            continue

                        file.write(chunk)

                        downloaded += len(chunk)

                        if total:

                            percent = downloaded * 100 / total

                            print(
                                f"\r{os.path.basename(output)} "
                                f"{percent:.0f}% ",
                                end=""
                            )

                print("\nDownload Complete")

                return output

            except Exception as e:

                attempt += 1

                print(
                    f"Retry {attempt}/{retries}"
                )

                if attempt >= retries:
                    raise Exception(
                        f"Download Failed : {e}"
                    )

                time.sleep(2)