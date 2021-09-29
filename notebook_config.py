# Configuration file for jupyter-notebook.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

c.NotebookApp.allow_origin = 'https://colab.research.google.com'
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.port_retries = 0
c.NotebookApp.nbserver_extensions = {
    'jupyter_http_over_ws': True,
    'widgetsnbextension': True
}

