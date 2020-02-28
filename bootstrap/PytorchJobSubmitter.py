import os
from twister2flow.twister2.util.ArgUtil import ArgUtil


class PytorchJobSubmitter:

    def __init__(self, script=None, executor=None, parallelism=1, hostfile=None):
        args = ArgUtil.pytorch_args()
        self.script = ArgUtil.script(args)
        self.executor = ArgUtil.executor(args)
        self.parallelism = ArgUtil.parallelism(args)
        self.hostfile = ArgUtil.hostfile(args)


    def submit(self):
        command = "sh bootstrap/pytorchrunner.sh "
        command += str(self.script) + " "
        command += str(self.executor) + " "
        command += str(self.parallelism) + " "
        # command += str(self.hostfile)
        print("Job Submitter : {}".format(command))
        # example "sh bootstrap/pytorchrunner.sh /home/vibhatha/github/forks/twister2/deeplearning/pytorch/src/main/python/PytorchMnistDist.py /home/vibhatha/venv/ENV37/bin/python3 4 hostfile"
        os.system(command)


if __name__ == "__main__":

    pjs = PytorchJobSubmitter()
    pjs.submit()
