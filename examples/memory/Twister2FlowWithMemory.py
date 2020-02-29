from twister2flow.twister2.pipeline import PipelineGraph
from twister2flow.twister2.task.Twister2Task import Twister2Task
from twister2flow.twister2.task.PythonTask import PythonTask

plg = PipelineGraph.PipelineGraph(name="UNNAMED_TASK")

download_task = PythonTask(name="download_task")
download_task.set_command("python3")
download_task.set_script_path(script_path="MnistDownload.py")
download_task.set_exec_path(exec_path=None)

twister2_task = Twister2Task(name="t2_task")
twister2_task.set_command("twister2 submit standalone python")
twister2_task.set_script_path(script_path="Twister2DistMnist.py")
twister2_task.set_exec_path(exec_path=None)

plg.add_task(download_task)
plg.add_task(twister2_task)

print(str(plg))

plg.execute()
