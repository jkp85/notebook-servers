# Jupyter Notebooks for Deep Learning (CPU/GPU)

Jupyter Notebook Deep Learning Images

**Try online for free at [3blades.io](https://3blades.io/)!**

## What it Gives You

* Everything in [Data Science Notebook](https://github.com/3blades/notebook-servers/tree/master/datascience-notebook)

Plus:

* CNTK for Python 2.7 and 3.6
* Tensorflow for Python 2.7 and 3.6
* MXNet for Python 2.7
* Keras for Python 2.7 and 3.6

## Basic Use

The following commands start a container with the Notebook server listening for HTTP connections on port 8888.

### CPU Version

```
docker run -it --rm -p 8888:8888 3blades/deeplearning-notebook
```

### GPU Version

```
docker run -it --rm -p 8888:8888 3blades/deeplearning-notebook:latest-gpu
```
