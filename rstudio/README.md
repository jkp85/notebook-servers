# R IDE with Deep Learning

R IDE Images with Deep Learning

**Try online for free at [3blades.io](https://3blades.io/)!**

## What it Gives You

* Everything in [rocker/rstudio](https://hub.docker.com/r/rocker/rstudio/)
* Tensorflow for R
* MXNet for R

> R IDE is not enabled for GPU. Once you have your models developed you can train / deploy
your models using Tensorflow or MXNet frameworks, directly.

## Basic Use

The following commands start a container with the R IDE listening for HTTP connections on port 8888. User ID and password are set to `rstudio`.

### CPU Version

```
docker run -it --rm -p 8888:8888 3blades/rstudio-notebook
```
