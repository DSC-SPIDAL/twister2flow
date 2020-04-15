# Twister2Flow

Designing a dataflow pipeline to support high performance deep learning in Twister2. This is an experimental version of the initial High Performance Deep Learning Connect of Twister2. 

## Pytorch Setup On RHEL7


### Set Up Romeo (RHEL7) For Pytorch Parallel Compatibility

```bash
module load anaconda
module load cuda/10.0
module load cudnn/10.0-v7.4.1
module load gcc/6.4.0
export CUDNN_INCLUDE_DIR=/opt/cudnn-10.0-linux-x64-v7.4.1/cuda/include
export CUDNN_LIB_DIR=/opt/cudnn-10.0-linux-x64-v7.4.1/cuda/lib64
conda create -n py36 python=3.6
source activate py36
export CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"
export CMAKE_PREFIX_PATH="/opt/gcc-6.4.0;$CMAKE_PREFIX_PATH"
conda install -c anaconda libgcc-ng libstdcxx-ng
conda install -c conda-forge openmpi
conda install numpy ninja pyyaml mkl setuptools cmake cffi
conda install -c pytorch magma-cuda100
conda install -c mingfeima mkldnn
conda uninstall --force mkl
pip install mkl
pip install mkl_include
conda uninstall --force cmake
pip install cmake
chmod +x ~/.conda/envs/py36/lib/python3.6/site-packages/cmake/data/bin/*
git clone --recursive https://github.com/pytorch/pytorch
cd pytorch/
BUILD_TEST=0 python setup.py install
```

### Credits 

Allan Streib of Future Systems, Indiana University Bloomington designed the set up. 

## Setting Up RHEL7 (Romeo r-003)

```bash
module load anaconda
module load cuda/10.0
module load cudnn/10.0-v7.4.1
module load gcc/6.4.0
export CUDNN_INCLUDE_DIR=/opt/cudnn-10.0-linux-x64-v7.4.1/cuda/include
export CUDNN_LIB_DIR=/opt/cudnn-10.0-linux-x64-v7.4.1/cuda/lib64
```

### Note

```text
Private Note: This is for running in r-003 RHEL7
```

```bash
source activate ENV1
```

## Running Examples

### RHEL7 Compatible

```bash
mpirun -n <parallelism> python3 mnist/mnist_dist_rhel7.py
```

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

```python
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

```

```bash
cd examples/memory
```

```python
python3 Twister2FlowWithMemory.py
```
