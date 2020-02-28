import os
from twister2flow.twister2.util.ArgUtil import ArgUtil


class PythonJobSubmitter:

    def __init__(self):
        args = ArgUtil.python_args()
        self.script = ArgUtil.script(args)
        self.executor = ArgUtil.executor(args)

    def submit(self):
        command = ""
        command += str(self.executor) + " "
        command += str(self.script) + " "
        print("Job Submitter : {}".format(command))
        os.system(command)


# if __name__ == "__main__":
#
#     pjs = PythonJobSubmitter()
#     pjs.submit()
