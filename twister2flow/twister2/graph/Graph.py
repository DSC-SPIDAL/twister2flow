from abc import ABC
from abc import abstractmethod


class Graph(ABC):

    def __init__(self, name="UNNAMED_GRAPH"):
        super().__init__()
        self.__name = name

    @abstractmethod
    def add_task(self, cls):
        pass
