from abc import ABC
from abc import abstractmethod


class Task(ABC):

    def __init__(self, name="UNNAMED_TASK"):
        super().__init__()
        self.__task_name = name

    @abstractmethod
    def get_script_path(self):
        pass

    @abstractmethod
    def get_command(self):
        pass

    @abstractmethod
    def get_exec_path(self):
        pass

    @abstractmethod
    def set_script_path(self, script_path=None):
        pass

    @abstractmethod
    def set_command(self, command=None):
        pass

    @abstractmethod
    def set_exec_path(self, exec_path=None):
        pass

    @abstractmethod
    def execute(self):
        pass
