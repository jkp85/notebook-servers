# Data Science Jupyter Notebook

Jupyter Notebook Data Science Image

**Try online for free at [3blades.io](https://3blades.io/)!**

## What it Gives You

* Latest version of [Jupyter Notebook](http://jupyter.org/)
* Latest version of [JupyterLab](https://github.com/jupyterlab/jupyterlab)
* Python2.7 and Python3.6 Kernels
* [Scipy](https://www.scipy.org/index.html) Packages
* [Scikit-learn](http://scikit-learn.org/stable/)
* [tini](https://github.com/krallin/tini) as the container entrypoint and [start-notebook.sh](./start-notebook.sh) as the default command

## Basic Use

The following command starts a container with the Notebook server listening for HTTP connections on port 8888 without authentication configured.

```
docker run -d -p 8888:8888 3blades/datascience-notebook
```
