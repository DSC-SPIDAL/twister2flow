import os
from twister2flow.twister2.task.Task import Task


class PytorchTask(Task):
    __script_path = None
    __command = None
    __pytorch_exec_path = None

    def __init__(self, name="UNNAMED_TASK"):
        Task.__init__(self, name=name)
        self.__name = name

    def set_script_path(self, script_path=None):
        self.__script_path = script_path

    def get_script_path(self):
        return self.__script_path

    def set_command(self, command=None):
        if command is None:
            self.__command = "mpirun -n 4 python3"
        else:
            self.__command = command

    def get_command(self):
        return self.__command

    def set_exec_path(self, exec_path):
        self.__pytorch_exec_path = exec_path

    def get_exec_path(self):
        return self.__pytorch_exec_path

    def execute(self):
        print("Executing Pytorch Task: " + self.get_command() + " " + self.get_script_path())
        os.system(self.get_command() + " " + self.get_script_path())

    def __str__(self):
        task_description = ""
        task_description += "\t\tName: \t\t\t\t{} \n".format(self.__name)
        task_description += "\t\tCommand: \t\t\t{} \n".format(self.__command)
        task_description += "\t\tExecution Path: \t{} \n".format(self.__pytorch_exec_path)
        return task_description
