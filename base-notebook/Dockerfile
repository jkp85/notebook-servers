# Core server based on Ubuntu Xenial (16.04)
FROM 3blades/core-server

MAINTAINER 3Blades <contact@3blades.io>

USER root

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -yq --no-install-recommends \
    python-dev \
    python3-dev \
    python-pip \
    python3-pip \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Install Tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini && \
    echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# Install Jupyter notebook
RUN conda install --quiet --yes \
    'notebook=4.4.*' \
    'jupyterlab=0.17.*' \
    && conda clean -tipsy

# Add a notebook profile.
RUN mkdir -p -m 700 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py

RUN pip3 install -q --upgrade pip wheel setuptools
RUN pip3 install \
    psycopg2 \
    pymongo \
    cassandra-driver \
    mysqlclient

# Configure container startup as root
EXPOSE 8888
WORKDIR /home/work
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

# Add local files as late as possible to avoid cache busting
COPY start-notebook.sh /usr/local/bin/
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
RUN chmod +x /usr/local/bin/start-notebook.sh
