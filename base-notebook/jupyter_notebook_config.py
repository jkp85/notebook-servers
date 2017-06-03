from jupyter_core.paths import jupyter_data_dir
import subprocess
import os
import errno
import stat

c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.tornado_settings = { 'headers': { 'Content-Security-Policy': "child-src * " } }
