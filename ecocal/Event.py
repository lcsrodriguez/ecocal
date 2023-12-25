from .utils import *


class Event:
    __class__: str = "Event"
    __slots__: dict = ("name", )

    def __init__(self) -> None:
        # Taking a pd.Series in input
        ...
