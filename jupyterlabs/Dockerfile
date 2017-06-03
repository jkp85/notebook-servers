FROM 3blades/datascience-notebook

MAINTAINER 3Blades <contact@3blades.io>

USER root

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Install Tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini && \
    echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# Install jupyter notebook and jupyterlabs
RUN pip3 install -U setuptools pip wheel
RUN pip3 install jupyterlab
RUN jupyter serverextension enable --py jupyterlab --sys-prefix

# Add local files as late as possible to avoid cache busting
COPY start-notebook.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-notebook.sh
