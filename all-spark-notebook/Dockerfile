FROM 3blades/pyspark-notebook:latest

MAINTAINER 3Blades <contact@g3blades.io>

# RSpark config
ENV R_LIBS_USER $SPARK_HOME/R/lib

# R packages
RUN conda install --quiet --yes \
  'r-base=3.3.2' \
  'r-irkernel=0.7*' \
  'r-ggplot2=2.2*' \
  'r-sparklyr=0.5*' \
  'r-rcurl=1.95*' && \
  conda clean -tipsy

# Apache Toree kernel
RUN pip --no-cache-dir \
    install https://dist.apache.org/repos/dist/dev/incubator/toree/0.2.0/snapshots/dev1/toree-pip/toree-0.2.0.dev1.tar.gz \
 && jupyter toree install --sys-prefix

# Spylon-kernel
RUN conda install --quiet --yes 'spylon-kernel=0.4*' \
 && python -m spylon_kernel install --sys-prefix
