import argparse
import sys


class ArgUtil:

    @staticmethod
    def python_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--script', type=str, default=None,
                            help='Path to Pytorch Script')
        parser.add_argument('--executor', type=str, default='python3',
                            help='Python3 executor (virtualenv path or default python3')
        args = parser.parse_args()
        return args


    @staticmethod
    def pytorch_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--script', type=str, default=None,
                            help='Path to Pytorch Script')
        parser.add_argument('--executor', type=str, default='python3',
                            help='Python3 executor (virtualenv path or default python3')
        parser.add_argument('--parallelism', type=int, default=4,
                            help='Parallelism of the job')
        parser.add_argument('--hostfile', type=str, default=None,
                            help='hostfile containing node information for the MPI Job')
        args = parser.parse_args()
        return args

    @staticmethod
    def twister2_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--script', type=str, default=None,
                            help='Path to Pytorch Script')

        args = parser.parse_args()
        return args

    @staticmethod
    def script(args):
        return args.script

    @staticmethod
    def executor(args):
        return args.executor

    @staticmethod
    def parallelism(args):
        return args.parallelism

    @staticmethod
    def hostfile(args):
        return args.hostfile




