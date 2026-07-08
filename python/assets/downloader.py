import os
import requests


class Downloader:

    @staticmethod
    def download(url: str, output: str):

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )

        response = requests.get(
            url,
            stream=True,
            timeout=60
        )

        response.raise_for_status()

        with open(output, "wb") as file:

            for chunk in response.iter_content(8192):

                if chunk:
                    file.write(chunk)

        return output