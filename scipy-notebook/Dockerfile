FROM 3blades/minimal-notebook

MAINTAINER 3Blades <contact@3blades.io>

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libav-tools \
      libgtk2.0-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python 3 packages
RUN conda install --quiet --yes \
    'nomkl' \
    'ipywidgets=6.0*' \
    'pandas=0.19*' \
    'numexpr=2.6*' \
    'matplotlib=2.0*' \
    'scipy=0.19*' \
    'seaborn=0.7*' \
    'scikit-learn=0.18*' \
    'scikit-image=0.12*' \
    'sympy=1.0*' \
    'cython=0.25*' \
    'patsy=0.4*' \
    'statsmodels=0.8*' \
    'cloudpickle=0.2*' \
    'dill=0.2*' \
    'numba=0.31*' \
    'bokeh=0.12*' \
    'sqlalchemy=1.1*' \
    'hdf5=1.8.17' \
    'h5py=2.6*' \
    'vincent=0.4.*' \
    'beautifulsoup4=4.5.*' \
    'xlrd' \
    'opencv' \
 && conda remove --quiet --yes --force qt pyqt \
 && conda clean -tipsy \
    # Activate ipywidgets extension in the environment that runs the notebook server
 && jupyter nbextension enable --py widgetsnbextension --sys-prefix

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /root/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot"

# Configure ipython kernel to use matplotlib inline backend by default
RUN mkdir -p /root/.ipython/profile_default/startup
COPY mplimporthook.py /root/.ipython/profile_default/startup/
