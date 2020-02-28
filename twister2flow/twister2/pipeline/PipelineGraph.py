from twister2flow.twister2.graph import Graph
from twister2flow.twister2.task import Task


class PipelineGraph(Graph.Graph):
    __task_list = []

    def __init__(self, name="UNNAMED_TASK"):
        Graph.Graph.__init__(self, name=name)
        self.__name = name

    def add_task(self, cls):
        _type = Task.Task
        if isinstance(cls, _type):
            print("Task Added {} ".format(_type))
            self.__task_list.append(cls)

        else:
            raise Exception("Invalid Instance {} ".format(_type))

    def execute(self):
        for task in self.__task_list:
            print("{} {} ".format(task.get_command(),  task.get_script_path()))
            task.execute()

    def __str__(self):
        pipeline_description = ''
        for index, task in enumerate(self.__task_list):
            pipeline_description += "Task Id {},\n  {}".format(index, str(task)) + "\n"
        return pipeline_description

