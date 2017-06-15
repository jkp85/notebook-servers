FROM 3blades/jupyterlab:iframe

MAINTAINER 3Blades <contact@3blades.io>

# Install Python 3 Tensorflow
RUN conda install --quiet --yes 'tensorflow=1.0*'

# Install Python 2 Tensorflow
RUN conda install --quiet --yes -n python2 'tensorflow=1.0*'

# Install Keras with conda-forge
RUN conda install -c conda-forge keras=2.0.4
