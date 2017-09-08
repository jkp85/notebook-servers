# Jupyter Notebook + Tensorflow + Keras

## What it Gives You

* Tensorflow with GPU support
* Latest release of Keras

## Basic Use

The following command starts a container with the Notebook server listening for HTTP connections on port 8888 with a randomly generated authentication token configured.

```
docker run -it --rm -p 8888:8888 3blades/tensorflow-notebook
```

Take note of the authentication token included in the notebook startup log messages. Include it in the URL you visit to access the Notebook server or enter it in the Notebook login form.

## Tensorflow Single Machine Mode

As distributed Tensorflow is still immature, we currently only provide the single machine mode.

```
import tensorflow as tf

hello = tf.Variable('Hello World!')

sess = tf.Session()
init = tf.initialize_all_variables()

sess.run(init)
sess.run(hello)
```
