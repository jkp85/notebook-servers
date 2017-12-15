# ==================================================================
# module list
# ------------------------------------------------------------------
# python        2.7    (apt)
# chainer       latest (pip)
# cntk          2.3    (pip)
# mxnet         latest (pip)
# pytorch       0.3.0  (pip)
# tensorflow    latest (pip)
# keras         latest (pip)
# sonnet        latest (pip)
# ==================================================================

FROM 3blades/core-server:build-119 AS core
FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

MAINTAINER 3Blades <contact@3blades.io>

# ==================================================================
RUN rm -rf /var/lib/apt/lists/* \
    /etc/apt/sources.list.d/cuda.list \
    /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update

# ==================================================================
# tools
# ------------------------------------------------------------------

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        wget \
        git \
        vim \        
        locales

# ==================================================================
# python
# ------------------------------------------------------------------

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python-pip \
        python-dev \
        && \
    pip --no-cache-dir install --upgrade \
        setuptools \
        pip \
        && \
    pip --no-cache-dir install --upgrade \
        graphviz \
        h5py \
        matplotlib \
        nose \
        numpy \
        pandas \
        Pillow \
        pyyaml \
        scipy \
        scikit-learn \
        sympy

# ==================================================================
# tensorflow
# ------------------------------------------------------------------

RUN pip --no-cache-dir install --upgrade \
        tensorflow

# ==================================================================
# mxnet
# ------------------------------------------------------------------

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        libatlas-base-dev \
        graphviz \
        && \
    pip --no-cache-dir install --upgrade \
        mxnet \
        graphviz

# ==================================================================
# keras
# ------------------------------------------------------------------

RUN pip --no-cache-dir install --upgrade \
        h5py \
        keras

# Oringinal stuff
RUN echo 'en_US.UTF-8' > /etc/locale.gen && \
        locale-gen 

# ==================================================================
# Tini
# ------------------------------------------------------------------
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini \
        && echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - \
        && mv tini /usr/local/bin/tini \
        && chmod +x /usr/local/bin/tini

# ==================================================================
# virtualenv
# ------------------------------------------------------------------
RUN pip --no-cache-dir install --upgrade \
        virtualenv

# ==================================================================
# Upgrade pip
# ------------------------------------------------------------------
RUN pip install --upgrade pip

# ==================================================================
# Setup tools
# ------------------------------------------------------------------
RUN pip --no-cache-dir install --upgrade \
        setuptools

# ==================================================================
# Jupyter Notebook
# ------------------------------------------------------------------
RUN pip --no-cache-dir install --upgrade \
        jupyter \
        jupyterlab

# ==================================================================
# Python 2 kernel
# ------------------------------------------------------------------
RUN python2 -m pip install ipykernel && \
    python2 -m ipykernel install --user

# Configure container startup as root
EXPOSE 8080
WORKDIR /home/work
ENTRYPOINT ["tini", "--"]
CMD ["bash start-notebook.sh"]

# Configure ipython kernel to use matplotlib inline backend by default
RUN mkdir -p /root/.ipython/profile_default/startup

# Add local files as late as possible to avoid cache busting
COPY mplimporthook.py /root/.ipython/profile_default/startup/
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
COPY --from=core runner /runner
COPY start-notebook.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-notebook.sh
