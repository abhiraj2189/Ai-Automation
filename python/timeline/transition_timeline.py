class TransitionTimeline:

    def apply(self, timeline):

        for item in timeline:

            item["transition"] = "fade"

        return timeline