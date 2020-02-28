from twister2flow.twister2.job.PythonJobSubmitter import PythonJobSubmitter
from twister2flow.twister2.util.ArgUtil import ArgUtil

args = ArgUtil.pytorch_args()

pjs = PythonJobSubmitter()

pjs.submit()
