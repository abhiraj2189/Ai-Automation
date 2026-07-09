from python.director.director_engine import DirectorEngine


class DirectorService:

    def generate(

        self,

        script,

        scenes

    ):

        engine = DirectorEngine()

        return engine.generate(

            script,

            scenes

        )