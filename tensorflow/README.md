# Jupyter Notebook Scientific Python Stack + Tensorflow

## What it Gives You

* Everything in [Scipy Notebook](https://github.com/3blades/notebook-servers/tree/master/scipy-notebook)
* Tensorflow for Python 2.7 and 3.5 (without GPU support)

## Basic Use

The following command starts a container with the Notebook server listening for HTTP connections on port 8888 with a randomly generated authentication token configured.

```
docker run -it --rm -p 8888:8888 3blades/tensorflow-notebook
```

Take note of the authentication token included in the notebook startup log messages. Include it in the URL you visit to access the Notebook server or enter it in the Notebook login form.

## Tensorflow Single Machine Mode

As distributed tensorflow is still immature, we currently only provide the single machine mode.

```
import tensorflow as tf

hello = tf.Variable('Hello World!')

sess = tf.Session()
init = tf.initialize_all_variables()

sess.run(init)
sess.run(hello)
```

## Notebook Options


```
docker run -d -p 8888:8888 jupyter/tensorflow-notebook start-notebook.sh --NotebookApp.password='sha1:74ba40f8a388:c913541b7ee99d15d5ed31d4226bf7838f83a50e'
```

For example, to set the base URL of the notebook server, run the following:

```
docker run -d -p 8888:8888 jupyter/tensorflow-notebook start-notebook.sh --NotebookApp.base_url=/some/path
```

For example, to disable all authentication mechanisms (not a recommended practice):

```
docker run -d -p 8888:8888 jupyter/tensorflow-notebook start-notebook.sh --NotebookApp.token=''
```
