FROM 3blades/core-server AS core
FROM 3blades/base-image AS base
FROM tensorflow/tensorflow:latest-gpu

MAINTAINER 3Blades <contact@3blades.io>

# Copy runner from core-server
COPY --from=core runner /runner

# Copy jupyter config and startup script from base-server
COPY --from=base /usr/local/bin/start-notebook.sh /usr/local/bin/start-notebook.sh
COPY --from=base /root/.jupyter/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

# Install Keras
RUN pip install -y keras
