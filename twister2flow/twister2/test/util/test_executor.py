from twister2flow.twister2.util.Executor import Executor
import subprocess

# Executor.run_command(executor_prefix="mpirun -n 4",
#                              executor="/home/vibhatha/venv/ENV37/bin/python3",
#                              script="/home/vibhatha/github/forks/twister2/deeplearning/pytorch/src/main/python/PytorchMnistDist.py")


process = subprocess.Popen(['mpirun', '-n 4', '/home/vibhatha/venv/ENV37/bin/python3',
                            '/home/vibhatha/github/forks/twister2/deeplearning/pytorch/src/main/python/PytorchMnistDist.py'],
                                    stdout=subprocess.PIPE,
                                   universal_newlines=True)