# Anaconda Virtual Enviroment
This is the document on how one can set their own virtual enviroment for python package management and control.

## Installation
Go to this Website to download anaconda: https://www.anaconda.com/download/


## Set Up
In documentation, there is the `anaconda_requirment.txt`

After the installation, go to Search Bar and find `Anaconda Prompt`.

To create the specific required virtual enviroments, use the command line: 

```
conda create --name myenv --file anaconda_requirment.txt
```

 Change `myenv` if you want your env to have another name.

## Set Anaconda Path
in `Anaconda Prompt`, use the command 
```
conda info -e
```
to find the path to your env. And set that path as your Python intepreter.


