from dataclasses import dataclass


@dataclass
class TimelineItem:

    start: float

    end: float

    asset: str

    caption: str

    animation: str

    transition: str