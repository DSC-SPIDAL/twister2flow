import os
from twister2flow.twister2.util.ArgUtil import ArgUtil


class Twister2JobSubmitter:

    def __init__(self, script=None):
        args = ArgUtil.twister2_args()
        self.script = args.script

    def submit(self):
        command = "twister2 submit standalone python "
        command += self.script
        os.system(command)


# if __name__ == '__main__':
#     tjs = Twister2JobSubmitter()
#     tjs.submit()
