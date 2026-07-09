from python.captions.caption_generator import CaptionGenerator


class CaptionService:

    def generate(

        self,

        subtitle

    ):

        generator = CaptionGenerator()

        return generator.generate(

            subtitle

        )