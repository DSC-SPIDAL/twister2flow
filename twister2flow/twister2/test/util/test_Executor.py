from unittest import TestCase
from twister2flow.twister2.util.Executor import Executor
import subprocess


class TestExecutor(TestCase):


    def test_run_command(self):
        Executor.run_command(executor_prefix="mpirun -n 4",
                             executor="/home/vibhatha/venv/ENV37/bin/python3",
                             script="/home/vibhatha/github/forks/twister2/deeplearning/pytorch/src/main/python/PytorchMnistDist.py")

    # def test_run_some_command(self):
    #     process = subprocess.Popen(['ping', '-c 4', 'python.org'],
    #                                stdout=subprocess.PIPE,
    #                                universal_newlines=True)



