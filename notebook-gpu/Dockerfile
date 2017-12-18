# ==================================================================
# module list
# ------------------------------------------------------------------
# python        2.7    (apt)
# python        3.6    (apt)
# mxnet         latest (pip)
# tensorflow    latest (pip)
# keras         latest (pip)
# opencv        latest (git)
# ==================================================================


FROM 3blades/core-server:build-119 AS core
FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

MAINTAINER 3Blades <contact@3blades.io>

# ==================================================================
RUN rm -rf /var/lib/apt/lists/* \
    /etc/apt/sources.list.d/cuda.list \
    /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update

ENV DEBIAN_FRONTEND noninteractive

# ==================================================================
# tools
# ------------------------------------------------------------------

RUN apt-get install -y --no-install-recommends \
        apt-transport-https \
        build-essential \
        bzip2 \
        ca-certificates \
        cmake \
        emacs \
        fonts-dejavu \    
        fonts-liberation \
        inkscape \
        jed \
        gcc \
        gfortran \
        git \
        vim \        
        locales \        
        openmpi-bin \
        pandoc \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-fonts-extra \
        texlive-fonts-recommended \
        texlive-generic-recommended \
        texlive-xetex \
        unzip \        
        wget

# ==================================================================
# python 2.7
# ------------------------------------------------------------------

RUN apt-get install -y --no-install-recommends \
        python-pip \
        python-dev \
        && \
    pip --no-cache-dir install --upgrade \
        setuptools \
        pip \
        && \
    pip2 --no-cache-dir install --upgrade \
        numpy \
        scipy \
        pandas \
        scikit-learn \
        matplotlib \
        Cython \
        graphviz \
        h5py \
        nose \
        Pillow \
        pyyaml \
        sympy

# ==================================================================
# python 3.6
# ------------------------------------------------------------------

RUN apt-get install -y --no-install-recommends \
        software-properties-common \
        && \
    add-apt-repository ppa:jonathonf/python-3.6 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.6 \
        python3.6-dev \
        && \
    wget -O ~/get-pip.py \
        https://bootstrap.pypa.io/get-pip.py && \
    python3.6 ~/get-pip.py && \
    ln -s /usr/bin/python3.6 /usr/local/bin/python3 && \
    pip3 --no-cache-dir install --upgrade \
        setuptools \
        && \
    pip3 --no-cache-dir install --upgrade \
        numpy \
        scipy \
        pandas \
        scikit-learn \
        matplotlib \
        Cython \
        graphviz \
        h5py \
        nose \
        Pillow \
        pyyaml \
        sympy

# ==================================================================
# tensorflow
# ------------------------------------------------------------------

RUN pip --no-cache-dir install --upgrade \
        tensorflow_gpu \
        && \
    pip2 --no-cache-dir install --upgrade \
        tensorflow_gpu

# ==================================================================
# mxnet
# ------------------------------------------------------------------

RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev \
        graphviz \
        && \
    pip --no-cache-dir install --upgrade \
        mxnet-cu80 \
        graphviz \
        && \
    pip2 --no-cache-dir install --upgrade \
        mxnet-cu80 \
        graphviz

# ==================================================================
# keras
# ------------------------------------------------------------------

RUN pip --no-cache-dir install --upgrade \
        h5py \
        keras \
        && \
    pip2 --no-cache-dir install --upgrade \
        h5py \
        keras

# ==================================================================
# opencv
# ------------------------------------------------------------------

RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        && \        
    git clone --depth 10 https://github.com/opencv/opencv ~/opencv && \
    mkdir -p ~/opencv/build && cd ~/opencv/build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
          -D CMAKE_INSTALL_PREFIX=/usr/local \
          -D WITH_IPP=OFF \
          -D WITH_CUDA=OFF \
          -D WITH_OPENCL=OFF \
          -D BUILD_TESTS=OFF \
          -D BUILD_PERF_TESTS=OFF \
          .. && \
    make -j"$(nproc)" install

# Original stuff
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
RUN pip --no-cache-dir install --upgrade virtualenv && \
    pip3 --no-cache-dir install --upgrade virtualenv

# ==================================================================
# Upgrade pip
# ------------------------------------------------------------------
RUN pip install --upgrade pip && \
    pip3 install --upgrade pip

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

# ==================================================================
# config & cleanup
# ------------------------------------------------------------------

RUN ldconfig && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*

# Configure container startup as root
EXPOSE 8080
WORKDIR /home/work
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

# Configure ipython kernel to use matplotlib inline backend by default
RUN mkdir -p /root/.ipython/profile_default/startup

# Add local files as late as possible to avoid cache busting
COPY mplimporthook.py /root/.ipython/profile_default/startup/
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
COPY --from=core runner /runner
COPY start-notebook.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-notebook.sh
