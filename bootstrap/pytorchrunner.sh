#!/bin/bash
scriptPath=$1
executor=$2
parallelism=$3
hostfile=$4
echo "Pytorch Launcher"
#mpirun -n ${parallelism} ${executor} ${scriptPath}
echo "Script Path :"${scriptPath}
echo "Executor :"${executor}
echo "Parallelism :"${parallelism}
echo "Hostfile :"${hostfile}

mpirun -n ${parallelism} ${executor} ${scriptPath}