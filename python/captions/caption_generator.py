from python.captions.animation import CaptionAnimation


class CaptionGenerator:

    def generate(

        self,

        subtitle_file

    ):

        animation = CaptionAnimation()

        return {

            "subtitle": subtitle_file,

            "animation": animation.word_by_word()

        }