# Twister2Flow

Designing a dataflow pipeline to support high performance deep learning in Twister2. This is an experimental version of the initial High Performance Deep Learning Connect of Twister2. 

## Supporting Dataflow Operations

1. File Systems oriented dataflow operations
2. Remote Memory Access (Work In Progress)

## Supporting Frameworks

1. Twister2 (JVM Oriented Big Data Toolkit)
2. Pytorch (Deep Learning Library)
3. Python3

## Install

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps twister2flow-test
```


## Bootstrap Task Executor

```bash
python3 bootstrap/PytorchJobSubmitter.py\ 
    --script examples/disk/PytorchMnistDist.py\ 
    --executor python3\ 
    --parallelism 4 --hostfile hostfile
```

## Example Disk-based Dataflow


```python3
from twister2flow.twister2.pipeline import PipelineGraph
from twister2flow.twister2.task.Twister2Task import Twister2Task
from twister2flow.twister2.task.PytorchTask import PytorchTask
from twister2flow.twister2.task.PythonTask import PythonTask

plg = PipelineGraph.PipelineGraph(name="UNNAMED_TASK")

download_task = PythonTask(name="download_task")
download_task.set_command("python3")
download_task.set_script_path(script_path="MnistDownload.py")
download_task.set_exec_path(exec_path=None)

twister2_task = Twister2Task(name="t2_task")
twister2_task.set_command()
twister2_task.set_script_path(script_path="Twister2PytorchMnist.py")
twister2_task.set_exec_path(exec_path=None)

pytorch_task = PytorchTask(name="pytorch_task")
pytorch_task.set_command()
pytorch_task.set_script_path(script_path="PytorchMnistDist.py")
pytorch_task.set_exec_path(exec_path=None)

plg.add_task(download_task)
plg.add_task(twister2_task)
plg.add_task(pytorch_task)


print(str(plg))

plg.execute()
```

Running example

```bash
cd examples/disk
```

```python
python3 Twister2FlowWithDisk.py
```
## Run In-Memory Example

```bash
cd examples/memory
```

```python
python3 Twister2FlowWithMemory.py
```