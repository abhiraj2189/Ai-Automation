from python.asset_selector.selector_engine import SelectorEngine


class SelectorService:

    def generate(

        self,

        keyword,

        videos

    ):

        return SelectorEngine().select(

            keyword,

            videos

        )