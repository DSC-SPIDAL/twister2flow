from bootstrap.Twister2JobSubmitter import Twister2JobSubmitter
from twister2flow.twister2.util.ArgUtil import ArgUtil

args = ArgUtil.twister2_args()

pjs = Twister2JobSubmitter(script=ArgUtil.script(args=args))

pjs.submit()
