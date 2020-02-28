from bootstrap.PytorchJobSubmitter import PytorchJobSubmitter
from twister2flow.twister2.util.ArgUtil import ArgUtil

args = ArgUtil.pytorch_args()

pjs = PytorchJobSubmitter(script=ArgUtil.script(args=args), executor=ArgUtil.executor(args=args),
                          parallelism=ArgUtil.parallelism(args=args),
                          hostfile=ArgUtil.hostfile(args=args))

pjs.submit()
