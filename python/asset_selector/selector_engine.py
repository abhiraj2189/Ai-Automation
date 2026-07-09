class SelectorEngine:

    def select(

        self,

        keyword,

        videos

    ):

        if not videos:
            raise Exception("No videos found.")

        videos = sorted(

            videos,

            key=lambda x: (

                x.get("width", 0),

                x.get("height", 0),

                x.get("duration", 0)

            ),

            reverse=True

        )

        return videos[0]