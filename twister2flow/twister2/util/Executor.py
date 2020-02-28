import subprocess

from twister2flow.twister2.util.StringUtil import StringUtil

class Executor:

    @staticmethod
    def run_command(executor_prefix=None, executor=None, script=None):
        executor_prefix_ = StringUtil.get_words(executor_prefix, " ")
        executor_prefix_.append(executor)
        executor_prefix_.append(script)
        print(executor_prefix_)
        process = subprocess.Popen(executor_prefix_,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        stdout, stderr
        print(stdout, stderr)